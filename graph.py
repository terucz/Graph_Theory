class Graph:

    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges

    def getMinSpanningTree(self, startnode):
        tree = []
        treenodes = []
        currentnode = startnode
        while len(treenodes) != len(self.nodes):
            currentedges = []
            for edge in self.edges:
                if (edge[0] == currentnode) or (edge[1] == currentnode):
                   currentedges.append(edge)
            sortededges = sorted(currentedges, key=lambda n:n[2])
            newedge = sortededges[0]
            i = 1
            while ((newedge in tree) or ((newedge[0] in treenodes) and (newedge[1] in treenodes))) and (i <= len(sortededges)):
                newedge = sortededges[i]
            tree.append(newedge)
            if len(treenodes)==0:
                treenodes.append(newedge[0])
                treenodes.append(newedge[1])
            else:
                if newedge[1] == currentnode: 
                    treenodes.append(newedge[0])
                else:
                    treenodes.append(newedge[1])

            if newedge[1] == currentnode: 
                currentnode = newedge[0]
            else:
                currentnode = newedge[1]
        return tree


    def findEdgesNotOriented (self, node):
        edges = []
        if node in self.nodes:
             for edge in self.edges:
                if (edge[0] == node) or (edge[1] == node):
                   edges.append(edge)
        return edges

    def labyrinth  (self, startnode, endnode):
        path = [] # cela cesta, kterou jsem prosla
        currentnode = startnode
        possible = True
        while (currentnode != endnode) or (possible == True) : # dokud jsme nenalezli východ nebo jsme nedosli do mistnosti kde je vsude oznaceno OUT
            edges = self.findEdgesNotOriented(currentnode)
            for edge in edges:
                rightdirection = []
                if edge[1] == currentnode: # pokud je hrana zapsana ve špatném směru
                    rightdirection.append((edge[1], edge[0]))
                else:
                    rightdirection.append(edge)
            i = 0
            outedge = None
            while (outedge == None) and (i < len(rightdirection)): #dokud nemáme vybranou cestu OUT nebo dokud máme z čeho vybírat
                if rightdirection[i] not in path:
                    outedge = rightdirection[i] # mame vybrany, kterou hranou jdeme ven
                    currentnode = outedge[1] #předěláme uzel, ve kterýmn se právě nacházímne
                    path.append(outedge) # přidáme hranu do cesty, označíme dveře OUT
                i = i + 1
                if i == len(rightdirection): # všechny dveře jsou označené OUT
                    possible = False
        return path