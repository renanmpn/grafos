import graphs
def main(my_graph):
    a = graphs.Vertex('A')
    my_graph.add_vertex(a)

    b = graphs.Vertex('B')
    my_graph.add_vertex(b)

    for i in range(ord('C'), ord('K')):
        my_graph.add_vertex(graphs.Vertex(chr(i)))
    
    edges = [('A','B'), ('A','E'), ('B','F'), ('C','G'), ('D', 'E'), ('D', 'H'), ('E','H'), ('F','G'), ('F','I'), ('F','J'), ('G', 'J'), ('H','I')]

    for edge in edges:
        my_graph.add_edge(edge[0], edge[1])
    my_graph.print_graph()

if __name__ == '__main__':
    adjacent_list_graph = graphs.GraphAdjacentList()
    main(adjacent_list_graph)
    print ('BFS')
    adjacent_list_graph.bfs('C')
    print ('')
    adjacent_list_graph = graphs.GraphAdjacentMatrix()
    main(adjacent_list_graph)
    