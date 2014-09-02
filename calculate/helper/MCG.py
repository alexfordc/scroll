__author__ = 'ict'

from calculate.graph import Graph


def new_mcg(graph):
    g = Graph()
    link = []
    for node_tuple in graph.get_edge():
        set_a = None
        set_b = None
        for i in range(len(link)):
            if node_tuple[0] in link[i]:
                set_a = i
            if node_tuple[1] in link[i]:
                set_b = i
        if set_a is None and set_b is None:
            link.append(set(node_tuple))
        if set_a is not None and set_b is None:
            link[set_a].add(node_tuple[1])
        if set_a is None and set_b is not None:
            link[set_b].add(node_tuple[0])
        if set_a is not None and set_b is not None:
            if set_a != set_b:
                link[set_a] |= link[set_b]
                del link[set_b]
    maxsize = 0
    maxset = None
    for eachset in link:
        if len(eachset) > maxsize:
            maxsize = len(eachset)
            maxset = eachset
    for node_tuple in graph.get_edge():
        if node_tuple[0] in maxset and node_tuple[1] in maxset:
            g.add_edge(node_tuple, graph.edge(node_tuple))
    return g