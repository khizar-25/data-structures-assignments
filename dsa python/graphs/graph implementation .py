class Graph:
    def __init__(self):
        self.graph = {}

    def addVertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def addEdge(self, src, dest):
        self.addVertex(src)
        self.addVertex(dest)
        self.graph[src].append(dest)
        self.graph[dest].append(src)

    def printGraph(self):
        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")
            
if __name__ == "__main__":
    G = Graph()
    G.addEdge('A', 'B')
    G.addEdge('A', 'C')
    G.addEdge('B', 'C')
    G.addEdge('C', 'D')

    G.printGraph()
