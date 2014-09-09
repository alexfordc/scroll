__author__ = 'ict'

from calculate.graph import Graph


def number_node(graph, base=0):
    g = Graph(graph.is_symmetric())
    nodes = graph.get_node().items()
    edges = graph.get_edge().items()
    mapping = {}
    count = base
    for node in nodes:
        g.add_node(count, node[1])
        mapping[node[0]] = count
        count += 1
    for edge in edges:
        g.add_edge((mapping[edge[0][0]], mapping[edge[0][1]]), edge[1])
    return g