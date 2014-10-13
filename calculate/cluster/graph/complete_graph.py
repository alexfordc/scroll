__author__ = 'ict'


def compute(graph):
    links = graph.nodes_link()
    node_mcg = set()
    for node in graph.get_node():
        node_link = set(links[node])
        for link in node_link:
            tmp_set = set()
            tmp_set.add(node)
            tmp_set.add(link)
            tmp_link = set(node_link)
            tmp_link.remove(link)
            while True:
                if len(tmp_link) == 0:
                    break
                other_node = tmp_link.pop()
                tmp_set.add(other_node)
                tmp_link &= links[other_node]
            node_mcg.add(frozenset(tmp_set))
    return node_mcg