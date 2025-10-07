from kubernetes import client, config

class Kubernetes:

    def connect(configuration):
    # Configs can be set in Configuration class directly or using helper utility
        config.load_kube_config(config_file="./kube_config.yml")
        v1 = client.CoreV1Api()
        return v1