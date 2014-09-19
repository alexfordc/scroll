__author__ = 'ict'

import pickle


class Graph:
    def __init__(self, sym=False):
        self.__node = {}
        self.__edge = {}
        self.__sym = sym
        self.__comp = False
        self.__value = 0

    def add_node(self, node_id, node_value=0):
        self.__node[node_id] = node_value

    def del_node(self, node_id):
        for key in self.__node:
            if (node_id, key) in self.__edge:
                self.del_edge((node_id, key))

    def add_edge(self, node_tuple, edge_value=0):
        missnode = None
        node_a = node_tuple[0]
        node_b = node_tuple[-1]
        if node_a not in self.__node:
            missnode = node_a
        if node_b not in self.__node:
            missnode = node_b
        if missnode is not None:
            raise Exception("No such node: " + str(missnode))
        if self.__sym:
            if node_a > node_b:
                tmp = node_a
                node_a = node_b
                node_b = tmp
        self.__edge[(node_a, node_b)] = edge_value

    def del_edge(self, node_tuple):
        if self.__comp:
            self.common()
        if self.__sym:
            if node_tuple[0] > node_tuple[1]:
                node_tuple = (node_tuple[1], node_tuple[0])
        if node_tuple not in self.__edge:
            return
        del self.__edge[node_tuple]

    def node_link(self, node):
        link = set()
        for other_node in self.__node:
            if (node, other_node) in self.__edge:
                link.add(other_node)
            if self.__sym:
                if (other_node, node) in self.__edge:
                    link.add(other_node)
        return link

    def nodes_link(self):
        links = {}
        for edge in self.__edge:
            if edge[0] not in links:
                links[edge[0]] = set()
            if edge[1] not in links:
                links[edge[1]] = set()
            links[edge[0]].add(edge[1])
            if self.__sym:
                links[edge[1]].add(edge[0])
        return links

    def node(self, node_id):
        if node_id not in self.__node:
            return None
        return self.__node[node_id]

    def edge(self, node_tuple):
        if self.__comp:
            return self.__value
        if self.__sym:
            if node_tuple[0] > node_tuple[1]:
                node_tuple = (node_tuple[1], node_tuple[0])
        if node_tuple not in self.__edge:
            return None
        return self.__edge[node_tuple]

    def get_node(self):
        return self.__node

    def get_edge(self):
        if self.__comp:
            edges = []
            for node_a in self.__node:
                for node_b in self.__node:
                    if node_a != node_b:
                        edges.append((node_a, node_b))
            return edges
        if self.__sym:
            reversed_edges = {}
            for edge, value in self.__edge.items():
                reversed_edges[(edge[1], edge[0])] = value
            rst_dict = dict(self.__edge)
            rst_dict.update(reversed_edges)
            return rst_dict
        return self.__edge

    def is_symmetric(self):
        return self.__sym

    def complete(self, value=0):
        self.__comp = True
        self.__value = value

    def common(self):
        for i_a in range(len(self.__node)):
            for i_b in range(i_a):
                self.add_edge((self.__node[i_a], self.__node[i_b]), self.__value)
        self.__comp = False

    def is_complete(self):
        return self.__comp

    def save(self, file):
        with open(file, "wb") as fp:
            pickle.dump([self.__node, self.__edge, self.__sym, self.__comp, self.__value], fp)

    def load(self, file):
        with open(file, "rb") as fp:
            tmp = pickle.load(fp)
            self.__node = tmp[0]
            self.__edge = tmp[1]
            self.__sym = tmp[2]
            self.__comp = tmp[3]
            self.__value = tmp[4]