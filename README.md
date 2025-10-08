# Blueprint

## Overview
Blueprint is a tool that can be used to connect to a Kubernetes Cluster and generate a list of all Software currently running within the cluster to be used for auditing and housekeeping. The reports can be generated and output in a JSON format

### Configuration
Currently Supported Attributes for configuration:
- `kube_config` - Location of Kubernetes Configuration
- `output` - Output format of application (json)
- `objects` - Currently not configurable, added for future capability 

```YAML
---
kube_config: "kube_config.yml"
output: "json"
objects:
  - Nodes
  - Containers

```
### Environment Variables

The following Environment Variables are supported by the application:

- `BLUEPRINT_CONFIG` - Path to the YAML configuration file for the application defaults to: `blueprint.yml`




### Running via Locally

To run the software locally ensure you have python and pip installed and run the commands:
```shell
pip install -r requirements.txt
cd src
python app.py 
```

### Running via Docker
To run the software via docker you will need to build the image using the commands:
```shell
docker build . -t bluprint:development
docker run blueprint:development
```
Note: You will need to supply the `kube_config.yml` so that the image may be built correctly.