import fileinput
from more_itertools import take, map_except

class Graph:
    __numVertices = 0
    __numEdges = 0
    __adjacencyLists = []

    def __init__(self, numVertices):
        self.__numVertices = numVertices
        for _ in range(numVertices):
            self.__adjacencyLists.append([])

    @classmethod
    def fromFile(self, file):
        f = fileinput.input(file)
        header = take(2, f)
        numVertices = int(header[0])
        numEdges = int(header[1])
        graph = Graph(numVertices)
        lines = take(numEdges, f)
        linesList = list(lines)
        linesList.reverse()
        for line in linesList:
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

    def adjacencyList(self, v):
        return self.__adjacencyLists[v]


class DepthFirstSearch:
    __count = 0
    __marked = []

    def __init__(self, graph, s):
        for _ in range(graph.numVertices):
            self.__marked.append(False)
        self.__dfs(graph, s)
    
    def __dfs(self, graph, v):
        self.__marked[v] = True;
        self.__count = self.__count + 1
        for w in graph.adjacencyList(v):
            if (self.__marked[w] != True):
                self.__dfs(graph, w)


    def isMarked(self, w):
        return self.__marked[w]

    def get_count(self):
        return self.__count

    count = property(get_count)
        



        