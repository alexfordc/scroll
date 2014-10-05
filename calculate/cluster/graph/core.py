from calculate.cluster.graph import complete_graph

__author__ = 'ict'

method_set = {
    "complete graph": complete_graph,
}


def method(mtd, graph):
    if mtd not in method_set:
        raise Exception("No such cluster method")
    return method_set[mtd].compute(graph)


def names():
    return list(method_set)