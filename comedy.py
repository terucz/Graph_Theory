from Graph import Graph
import fileinput

nodes = []
edges = []
i = 0

for line in fileinput.input():
    if i==0:
        nodes = line.replace(' ', '').replace('\n', '').split(',')
    else:
        edgenode = []
        line = line.replace(' ', '').replace('\n', '')
        edgenode = line.split(',')
        edges.append((edgenode[0], edgenode[1]))
        edges.append((edgenode[0], edgenode[2]))
        edges.append((edgenode[2], edgenode[1]))
    i = i + 1

graph = Graph(nodes, edges)
result = []

colors = graph.coloringNodes()
for color in colors:
    print(color.replace('.', ', '))