class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Vertex:
    def __init__(self,key):
        self.id = key
        self.visited = False
        self.connectedTo = []

    def addNeighbor(self,nbr):
        self.connectedTo.append(nbr)

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def addEdge(self,fromV,toV):
        if fromV not in self.vertList:
            nv = self.addVertex(fromV)
        if toV not in self.vertList:
            nv = self.addVertex(toV)
        self.vertList[fromV].addNeighbor(self.vertList[toV])

    def printEdges(self):
        for ver in self.vertList.values():
            print("from {} to: {}".format(ver.id, [vc.id for vc in ver.connectedTo]))

    def findRoute(self, fromV, toV):
        if fromV == toV:
            return True
        q = Queue()
        q.enqueue(self.getVertex(fromV))
        while not q.isEmpty():
            vertex = q.dequeue()
            vertex.visited = True
            if vertex.id == toV:
                return True
            for ngh in vertex.connectedTo:
                if not ngh.visited:
                    q.enqueue(ngh)
        return False

graph = Graph()
graph.addEdge('a', 'b')
graph.addEdge('a', 'd')
graph.addEdge('d', 'e')
graph.addEdge('e', 'k')
graph.addEdge('c', 'b')
graph.printEdges()
print(graph.findRoute('a','c'))
