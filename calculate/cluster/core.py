__author__ = 'ict'

from calculate.cluster import connected_graph


method_set = {
    "connected graph": connected_graph,
}


def method(mtd, graph):
    if mtd not in method_set:
        raise Exception("No such cluster method")
    return method_set[mtd].compute(graph)


def names():
    return list(method_set)