import exceptions

class Grafo(object):
    @classmethod
    def cria_grafo(cls, numero_de_vertices, grau_maximo, eh_ponderado):
        pesos = None
        grau = [None for i in range(numero_de_vertices)]
        arestas = [None for i in range(numero_de_vertices)]
        for i in range(numero_de_vertices):
            arestas[i] = [None for j in range(grau_maximo)]
        if eh_ponderado:
            pesos = [None for j in range(numero_de_vertices)]
            for i in range(numero_de_vertices):
                pesos[i] = [None for j in range(grau_maximo)]
        return cls(numero_de_vertices=numero_de_vertices, grau_maximo=grau_maximo, eh_ponderado=eh_ponderado, grau=grau, arestas=arestas, pesos=pesos)

    def __init__(self, eh_ponderado=None, numero_de_vertices=None, grau_maximo=None, arestas=None, pesos=None, grau=None):
        self.eh_ponderado = eh_ponderado
        self.numero_de_vertices = numero_de_vertices
        self.grau_maximo = grau_maximo
        self.arestas = arestas
        self.pesos = pesos
        self.grau = grau

    def insere_aresta(self, origem, destino, eh_digrafo=False, peso=None):
        if origem < 0 or origem >= self.numero_de_vertices:
            raise exceptions.VerticeInvalido
        if destino < 0 or destino >= self.numero_de_vertices:
            raise exceptions.VerticeInvalido
        
