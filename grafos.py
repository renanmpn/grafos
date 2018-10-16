class Grafo(object):
    @classmethod
    def cria_grafo(cls, numero_de_vertices, grau_maximo, eh_ponderado):
        return cls(numero_de_vertices=numero_de_vertices, grau_maximo=grau_maximo, eh_ponderado=eh_ponderado)

    def __init__(self, eh_ponderado=None, numero_de_vertices=None, grau_maximo=None, arestas=None, pesos=None, grau=None):
        self.eh_ponderado = eh_ponderado
        self.numero_de_vertices = numero_de_vertices
        self.grau_maximo = grau_maximo
        self.arestas = arestas
        self.pesos = pesos
        self.grau = grau