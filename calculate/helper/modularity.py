__author__ = 'ict'


def value_q(graph, partition_set):
    nodes = graph.get_node()
    q = 0
    m = 0
    k = {}
    c = {}
    count = 0
    for one_set in partition_set:
        for node in one_set:
            if node not in c:
                c[node] = set()
            c[node].add(count)
        count += 1
    for node_i in nodes:
        k[node_i] = 0
        for node_j in nodes:
            v = graph.edge((node_i, node_j))
            if v is not None:
                k[node_i] += v
                m += v
    m /= 2
    for node_i in nodes:
        for node_j in nodes:
            if node_i not in c or node_j not in c:
                continue
            if len(c[node_i] & c[node_j]) != 0:
                a_ij = graph.edge((node_i, node_j))
                if a_ij is None:
                    a_ij = 0
                q += a_ij - ((k[node_i] * k[node_j]) / (2 * m))
    if m == 0:
        return -1
    return q / (2 * m)