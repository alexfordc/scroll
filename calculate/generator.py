__author__ = 'ict'

import calculate.feature.core
import calculate.similarity.core

from calculate.graph import Graph


def graph(data, ft_mtd, sim_mtd):
    g = Graph(True)
    data_list = list(data.items())
    ft_dict = {}
    for key, odata in data_list:
        ft_dict[key] = calculate.feature.core.method(ft_mtd, odata)
    for i in range(len(data_list)):
        for j in range(i + 1):
            id_a = data_list[i][0]
            id_b = data_list[j][0]
            if g.node(id_a) is None:
                g.add_node(id_a)
            if g.node(id_b) is None:
                g.add_node(id_b)
            g.add_edge((id_a, id_b), calculate.similarity.core.method(sim_mtd, ft_dict[id_a], ft_dict[id_b]))
    return g