import exceptions

class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.neighbors = list()

    def add_neighbor(self, vertex):
        if vertex not in self.neighbors:
            self.neighbors.append(vertex)
            self.neighbors.sort()

class GraphAdjacentList:
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
    
class GraphAdjacentMatrix:
    def __init__(self):
        self.vertices = {}
        self.edges = []
        self.edge_indices = {}

    def add_vertex(self, vertex):
        if not isinstance(vertex, Vertex):
            raise exceptions.InvalidVertex
        if vertex.name in self.vertices:
            raise exceptions.DuplicatedVertex
        self.vertices[vertex.name] = vertex
        for row in self.edges:
            row.append(0)
        self.edges.append([0] * (len(self.edges) + 1))
        self.edge_indices[vertex.name] = len(self.edge_indices)
        return True
    
    def add_edge(self, vertex_a, vertex_b, weight=1):
        if vertex_a not in self.vertices:
            raise exceptions.InvalidVertex('Vertex {} is invalid'.format(vertex_a))
        if vertex_b not in self.vertices:
            raise exceptions.InvalidVertex('Vertex {} is invalid'.format(vertex_b))
        self.edges[self.edge_indices[vertex_a]][self.edge_indices[vertex_b]] = weight
        self.edges[self.edge_indices[vertex_b]][self.edge_indices[vertex_a]] = weight
        return True
    def print_graph(self):
        print ('    ', end='')
        for v, i in sorted(self.edge_indices.items()):
            print (v + ' ', end='')
        print('')
        for v, i in sorted(self.edge_indices.items()):
            print (v + ' - ', end='')
            for j in range(len(self.edges)):
                print (str(self.edges[i][j]) + ' ', end='')
            print (' ')
    

    