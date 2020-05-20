import fileinput
from more_itertools import take, map_except

class Graph:
    def __init__(self, numVertices):
        self.__numVertices = numVertices;
        self.__numEdges = 0;
        self.__adjacencyLists = [];
        
        for _ in range(numVertices):
            self.__adjacencyLists.append([])

    @classmethod
    def fromFile(self, file):
        f = fileinput.input(file)
        header = take(2, f)
        numVertices = int(header[0])
        numEdges = int(header[1])
        graph = Graph(numVertices)
        for line in take(numEdges, f):
            vw = map_except(int, line, ValueError, TypeError)
            vwList = list(vw)
            v = vwList[0]
            w = vwList[1]
            graph.addEdge(v, w)

        fileinput.close()
        return graph

    def get_numVertices(self):
        return self.__numVertices

    def get_numEdges(self):
        return self.__numEdges

    numVertices = property(get_numVertices)
    numEdges = property(get_numEdges)

    def addEdge(self, v, w):
        self.__adjacencyLists[v].append(w)
        self.__adjacencyLists[w].append(v)
        self.__numEdges = self.__numEdges + 1

    def adjacencyList(v):
        self.__adjacencyLists[v]