class Nodes:
    def get_nodes(api):
        ret = api.list_node(watch=False)
        nodes = []
        for i in ret.items:
            node = {}
            node['name'] = i.metadata.name
            node['id'] = i.status.node_info.machine_id
            node['version'] = i.status.node_info.kubelet_version
            ready_condition = next((condition for condition in i.status.conditions if condition.type == "Ready"), None)
            if ready_condition:
                node['status'] = "Ready"
            else:
                node['status'] = "NotReady"
            node['os'] = i.status.node_info.os_image
            node['kernel'] = i.status.node_info.kernel_version
            nodes.append(node)
        return nodes
