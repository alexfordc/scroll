__author__ = 'ict'

from DAL.driver.base import Base


class RG(Base):
    def __init__(self, graph=None):
        Base.__init__(self)
        self.graph = graph

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

    def save(self, dal_driver):
        pass