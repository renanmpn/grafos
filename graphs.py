import exceptions

class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.neighbors = list()

    def add_neighbor(self, vertex):
        if vertex not in self.neighbors:
            self.neighbors.append(vertex)
            self.neighbors.sort()

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if not isinstance(vertex, Vertex):
            raise exceptions.InvalidVertex
        if vertex.name in self.vertices:
            raise exceptions.DuplicatedVertex
        self.vertices[vertex.name] = vertex
        return True
    
    def add_edge(self, vertex_a, vertex_b):
        if vertex_a not in self.vertices:
            raise exceptions.InvalidVertex('Vertex {} is invalid'.format(vertex_a))
        if vertex_b not in self.vertices:
            raise exceptions.InvalidVertex('Vertex {} is invalid'.format(vertex_b))
        for vertex_name, vertex in self.vertices.items():
            if vertex_name == vertex_a:
                vertex.add_neighbor(vertex_b)
            if vertex_name == vertex_b:
                vertex.add_neighbor(vertex_a)
        return True
    def print_graph(self):
        for vertex_name in sorted(list(self.vertices.keys())):
            print ('{} - {}'.format(vertex_name, str(self.vertices[vertex_name].neighbors)))
    

    