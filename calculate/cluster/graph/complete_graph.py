__author__ = 'ict'


def compute(graph):
    links = graph.nodes_link()
    node_mcg = {}
    for node in graph.get_node():
        node_link = set(links[node])
        while len(node_link) != 0:
            tmp_set = set()
            tmp_set.add(node)
            if node in node_link:
                node_link.remove(node)
            tmp_link = set(node_link)
            for other_node in tmp_link.copy():
                tmp_set.add(other_node)
                if other_node in node_link:
                    node_link.remove(other_node)
                if node in links[other_node]:
                    links[other_node].remove(node)
                tmp_link &= links[other_node]
            if node not in node_mcg:
                node_mcg[node] = set()
            if len(tmp_set) > len(node_mcg[node]):
                node_mcg[node] = tmp_set
    rst = set()
    for _, mcg in node_mcg.items():
        rst.add(frozenset(mcg))
    return rst