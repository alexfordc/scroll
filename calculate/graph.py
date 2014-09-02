__author__ = 'ict'


class Graph:
    def __init__(self, sym=False):
        self.node = {}
        self.edge = {}
        self.sym = sym

    def add_node(self, node_id, node_value):
        self.node[node_id] = node_value

    def del_node(self, node_id):
        for key in self.node:
            if (node_id, key) in self.edge:
                self.del_edge((node_id, key))

    def add_edge(self, node_tuple, edge_value):
        missnode = None
        node_a = node_tuple[0]
        node_b = node_tuple[-1]
        if node_a not in self.node:
            missnode = node_a
        if node_b not in self.node:
            missnode = node_b
        if missnode is not None:
            raise Exception("No such node: " + str(missnode))
        if self.sym:
            if node_a > node_b:
                tmp = node_a
                node_a = node_b
                node_b = tmp
        self.edge[(node_a, node_b)] = edge_value

    def del_edge(self, node_tuple):
        if self.sym:
            if node_tuple[0] > node_tuple[1]:
                tmp = node_tuple[0]
                node_tuple[0] = node_tuple[1]
                node_tuple[1] = tmp
        if node_tuple not in self.edge:
            raise Exception("No such edge: " + str(node_tuple))
        del self.edge[node_tuple]

    def node_link(self, node):
        link = set()
        for other_node in self.node:
            if other_node > node:
                if (node, other_node) in self.edge:
                    link.add(other_node)
            else:
                if (other_node, node) in self.edge:
                    link.add(other_node)
        return link

    def nodes_link(self):
        links = {}
        for edge in self.edge:
            if edge[0] not in links:
                links[edge[0]] = set()
            if edge[1] not in links:
                links[edge[1]] = set()
            links[edge[0]].add(edge[1])
            links[edge[1]].add(edge[0])
        return links

    def node(self, node_id):
        if node_id not in self.node:
            return None
        return self.node[node_id]

    def edge(self, node_tuple):
        if self.sym:
            if node_tuple[0] > node_tuple[1]:
                tmp = node_tuple[0]
                node_tuple[0] = node_tuple[1]
                node_tuple[1] = tmp
        if node_tuple not in self.edge:
            return None
        return self.edge[node_tuple]

    def get_node(self):
        return self.node

    def get_edge(self):
        return self.edge