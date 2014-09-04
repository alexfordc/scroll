__author__ = 'ict'


class RG:
    def __init__(self, graph=None):
        self.data = []
        self.graph = graph
        self.tag = str(graph)
        self.loaded = False

    def load(self, opt="edge", graph=None):
        if graph is None:
            graph = self.graph
        if graph is None:
            raise Exception("Need input a graph")
        self.tag = str(graph)
        opt_multi = opt.split(" ")
        if len(opt_multi) == 0:
            raise Exception("Need input options")
        if opt_multi[0] == "node":
            if len(opt_multi) > 1:
                if opt_multi[1] == "value":
                    self.data = list(graph.get_node().items())
                else:
                    raise Exception("invalid option")
            else:
                self.data = list(graph.get_node())
            self.loaded = True
        elif opt_multi[0] == "edge":
            if len(opt_multi) > 1:
                if opt_multi[1] == "value":
                    self.data = [[nodes[0], nodes[1], value] for nodes, value in graph.get_edge().items()]
                else:
                    raise Exception("invalid option")
            else:
                self.data = [[nodes[0], nodes[1]] for nodes in graph.get_edge()]
            self.loaded = True
        else:
            raise Exception("invalid option")

    def clean(self):
        self.data = []
        self.tag = None
        self.loaded = False

    def save(self, dal_driver):
        pass

    def data(self, index):
        if index < 0 or index > len(self.data):
            return None
        return self.data[index]

    def get_data(self):
        return self.data

    def get_tag(self):
        return self.tag

    def done(self):
        return self.loaded