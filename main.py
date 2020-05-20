class Graph:
    def __init__(self, vertices):
        self.__vertices = vertices;
        self.__edges = 0;
        self.__adjacencyLists = [];
        
        for vertex in range(vertices):
            self.__adjacencyLists.append([])


    def Vertices(self):
        return self.__vertices

    def Edges(self):
        return self.__edges


graph1 = Graph(1)
print(graph1.Vertices())
print(graph1.Edges())
