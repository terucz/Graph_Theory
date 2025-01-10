class Graph:

    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges

    def areNeighbours(self, node1, node2): # zkontorlováno - je to ok
        result = False
        for edge in self.edges:
            if ((node1 == edge[0]) and (node2 == edge[1])) or ((node1 == edge[1]) and (node2 == edge[0])):
                result = True
        #print("---------" + node1 + " vs "+ node2 + "----------")
        #print(result)
        return result

    def neighboursCount(self, node): # zkontorlováno - je to ok
        result = 0
        for edge in self.edges:
            if (((node == edge[0]) or (node == edge[1])) and (edge[0] != edge[1])):
                result = result + 1
        return result

    def getNeighbours(self, node):
        result = []
        for edge in self.edges:
            if ((node == edge[0]) and (edge[0] != edge[1])):
                result.append(edge[1])
            if ((node == edge[1]) and (edge[0] != edge[1])):
                result.append(edge[0])
        return result

    def isComplete(self):
        result = False
        oknodes = 0
        for node in self.nodes:
            neighbours = self.neighboursCount(node)
            if (neighbours == len(self.nodes)-1):
                oknodes = oknodes + 1
        if (oknodes == len(self.nodes)):
            result = True
        return result

    def coloringNodes(self):
        newnodes = []
        newedges = []
        newnodes = self.nodes
        newedges = self.edges
        newgraph = Graph(newnodes, newedges)
       
        while not newgraph.isComplete():
            possibleforstick = []
            i = 0
            while len(possibleforstick) == 0:
                possibleforstick = []
                for node in newnodes:
                    if not newgraph.areNeighbours(newnodes[i], node):
                        if node != newnodes[i]:
                            possibleforstick.append(node)
                if len(possibleforstick) == 0:
                    i = i + 1
            newname = newnodes[i] + "." + possibleforstick[0]
            helpnodes = newnodes
            helpedges = newedges
            newnodes = []
            newedges = []
            newnodes.append(newname)
            for node in helpnodes:
                if ((node != helpnodes[i]) and ( node != possibleforstick[0])):
                    newnodes.append(node)
            for edge in helpedges:
                if( (edge[0] != helpnodes[i]) and (edge[1] != helpnodes[i]) and (edge[0] != possibleforstick[0]) and (edge[1] != possibleforstick[0])):
                    newedges.append(edge)
            neighbours1 = newgraph.getNeighbours(helpnodes[i])
            neighbours2 = newgraph.getNeighbours(possibleforstick[0])
            for neigh in neighbours1:
                newedges.append((newname,neigh))
            for neigh in neighbours2:
                if (newname,neigh) not in newedges:
                    newedges.append((newname,neigh))
            newgraph.edges = newedges
            newgraph.nodes = newnodes


        return newnodes
        