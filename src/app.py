# Import Python OS
import os

# Import Configurations
from configuration.configuration import Configuration
from configuration.kubernetes import Kubernetes

# Import Models
from models.nodes import Nodes
from models.containers import Containers

# Import Output
from output import Output



if __name__ == "__main__":

    # Setup Configuration
    CONFIG = os.getenv("BLUEPRINT_CONFIG", default="blueprint.yml")
    configuration = Configuration(CONFIG)
    
    api = Kubernetes.connect(None)
    containers = Containers.get_containers(api)
    nodes = Nodes.get_nodes(api)

    # Build Data for Ouput
    data = {}
    data['containers'] = containers
    data['nodes'] = nodes

    Output(data, configuration.get_output())
    exit(0)