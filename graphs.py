import exceptions

class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.neighbors = list()

    def add_neighbor(self, vertex):
        if vertex not in self.neighbors:
            self.neighbors.append(vertex)
            self.neighbors.sort()
