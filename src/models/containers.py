class Containers():
    
    def get_containers(api):
        ret = api.list_pod_for_all_namespaces(watch=False)
        containers = []
        for i in ret.items:
            for x in i.spec.containers:
                container = {}
                container['name']      =  i.metadata.name
                container['namespace'] =  i.metadata.namespace
                container['image']     =  x.image
                container['status']    =  i.status.phase
                containers.append(container)
        return containers