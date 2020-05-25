from graph import Graph, DepthFirstSearch

graph1 = Graph(6)
graph1.addEdge(0, 5)
graph1.addEdge(2, 4)
graph1.addEdge(2, 3)
graph1.addEdge(1, 2)
graph1.addEdge(0, 1)
graph1.addEdge(3, 4)
graph1.addEdge(3, 5)
graph1.addEdge(0, 2)

graph2 = Graph.fromFile('tinyCG.txt')
print(graph1.numVertices == graph2.numVertices)
print(graph1.numEdges == graph2.numEdges)


graph3 = Graph.fromFile('tinyCG.txt')
depthFirstSearch = DepthFirstSearch(graph3, 0)
# "{} and {}".format("string", 1)
print("depthFirstSearch.count: {}".format(depthFirstSearch.count))