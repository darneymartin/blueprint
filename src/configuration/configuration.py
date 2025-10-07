import yaml
import os

class Configuration:
    """
    Handles application configuration from a YAML file,
    with overrides from environment variables.
    """
    def __init__(self, yaml_path: str):
        """
        Initializes the configuration loader.

        Args:
            yaml_path (str): The path to the configuration YAML file.
        """
        self._config = self._load_from_yaml(yaml_path)
        self._override_with_env(self._config)

    def _load_from_yaml(self, yaml_path: str) -> dict:
        """Loads the base configuration from a YAML file."""
        try:
            with open(yaml_path, 'r') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            raise Exception(f"Configuration file not found at: {yaml_path}")
        except yaml.YAMLError as e:
            raise Exception(f"Error parsing YAML file: {e}")

    def _override_with_env(self, config_dict: dict, prefix: str = ''):
        """
        Recursively overrides configuration with environment variables.
        Example: config {'database': {'host': 'localhost'}}
        can be overridden by an env var DATABASE_HOST='remote.db'.
        """
        for key, value in config_dict.items():
            env_var_name = f"{prefix}{key}".upper()
            if isinstance(value, dict):
                # Recurse for nested dictionaries
                self._override_with_env(value, prefix=f"{env_var_name}_")
            else:
                # Check for environment variable override
                env_value = os.getenv(env_var_name)
                if env_value is not None:
                    # Try to cast env var to the original type (e.g., int, bool)
                    original_type = type(value)
                    try:
                        config_dict[key] = original_type(env_value)
                    except ValueError:
                        config_dict[key] = env_value # Keep as string if cast fails

    def get(self, key_path: str, default=None):
        """
        Retrieves a configuration value using dot notation.
        Example: get('database.host')
        """
        keys = key_path.split('.')
        value = self._config
        try:
            for key in keys:
                value = value[key]
            return value
        except (TypeError, KeyError):
            return default

