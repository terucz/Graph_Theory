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
        line = line.replace(' ', '').replace('\n', '').split(':')
        edge = line[1].split('->')
        end = len(edge)-1
        for x in range(end):
            edges.append((edge[x], edge[x+1]))
    i = i + 1

graph = Graph(nodes, edges)
loops = graph.getLoops()

for loop in loops:
    print(loop)