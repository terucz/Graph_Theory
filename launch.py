from graph import Graph
import fileinput

nodes = []
edges = []
i = 0

for line in fileinput.input():
    if i==0:
        line = line.replace(' ', '').replace('\n', '').split(':')
        nodes = line[1].split(',')
    else:
        line = line.replace(' ', '').replace('\n', '')
        edge = line.split('-')
        price = int(edge[1].split(':')[1].replace('s', ''))
        if len(edge)>1:
            edges.append((edge[0], edge[1].split(':')[0], price))
    i = i + 1

graph = Graph(nodes, edges)
result = []
#sortedEdges = sorted(edges, key=lambda n:n[2])

result = graph.getMinSpanningTree("navigace")

for edge in result:
	print(edge[0], " - ", edge[1])