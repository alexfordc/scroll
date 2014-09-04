__author__ = 'ict'


def edge_thr(graph, thr, reverse=False):
    edge_list = list(graph.get_edge().items())
    for node_tuple, value in edge_list:
        if reverse:
            if value > thr:
                graph.del_edge(node_tuple)
        else:
            if value < thr:
                graph.del_edge(node_tuple)


def node_thr(graph, thr, reverse=False):
    edge_list = list(graph.get_edge().items())
    for node, value in edge_list:
        if reverse:
            if value > thr:
                graph.del_node(node)
        else:
            if value < thr:
                graph.del_node(node)