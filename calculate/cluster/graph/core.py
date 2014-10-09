from calculate.cluster.graph import complete_graph

__author__ = 'ict'

callback_index = 0
option_indx = 1

method_set = {
    "complete graph": (complete_graph, False),
}


def method(mtd, graph, option=None):
    mtd_list = mtd.split(",")
    for i in range(len(mtd_list)):
        while True:
            if len(mtd_list[i]) == 0:
                raise Exception("Miss method")
            if mtd_list[i][0] == " ":
                mtd_list[i] = mtd_list[i][1:]
            if mtd_list[i][-1] == " ":
                mtd_list[i] = mtd_list[i][:-1]
            if mtd_list[i][0] != " " and mtd_list[i][-1] != " ":
                break
    if len(mtd_list) == 1:
        option = [option]
    if option is None:
        option = [None] * len(mtd_list)
    rst = []
    for i in range(len(mtd_list)):
        if mtd_list[i] not in method_set:
            raise Exception("No such cluster method:" + mtd_list[i])
        if method_set[mtd_list[i]][option_indx] and option[i] is not None:
            rst.append(method_set[mtd_list[i]][callback_index].compute(graph, option[i]))
        else:
            rst.append(method_set[mtd_list[i]][callback_index].compute(graph))
    if len(rst) == 1:
        return rst[0]
    else:
        return rst


def names():
    return list(method_set)