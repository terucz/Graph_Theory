class Graph:

    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges

    def edgeCountNotOriented (self, node):
        edgeCount = 0
        for edge in self.edges:
            if edge[0] == node or edge[1] == node:
                edgeCount = edgeCount + 1
        return edgeCount

    def getdoubleEdgesOriented (self):
        doubleedges = []
        for edge in self.edges:
            if self.edges.count(edge) > 1 and doubleedges.count(edge) == 0 :
                doubleedges.append(edge)
        return doubleedges

    def getIsolatedNode(self):
        isolatedNode = []
        for node in self.nodes:
            hasEdge = False
            for edge in self.edges:
                if edge[0] == node or edge[1] == node:
                    hasEdge = True
            if not hasEdge:
                isolatedNode.append(node)
        return isolatedNode

    def getLoops(self):
        loops = []
        for edge in self.edges:
            isLoop = False
            if edge[0] == edge[1]:
            	isLoop = True
            if isLoop:
                loops.append(edge[0])
        return loops

    def getEdgesFrom(self,node):
        edgesfrom = []
        if node in self.nodes:
             for edge in self.edges:
                if edge[0] == node:
                   edgesfrom.append(edge[1])
        return edgesfrom

    def getEdgesTo(self,node):
        edgesto = []
        if node in self.nodes:
            for edge in self.edges:
                if edge[1] == node:
                    edgesto.append(edge[0])
        return edgesto
