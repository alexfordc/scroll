__author__ = 'ict'


def edge_thr(graph, thr, reverse=False):
    for node_tuple, value in graph.get_edge():
        if reverse:
            if value < thr:
                graph.del_edge(node_tuple)
        else:
            if value > thr:
                graph.del_edge(node_tuple)


def node_thr(graph, thr, reverse=False):
    for node, value in graph.get_node():
        if reverse:
            if value < thr:
                graph.del_node(node)
        else:
            if value > thr:
                graph.del_node(node)