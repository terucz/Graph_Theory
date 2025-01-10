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
around = []

for node in graph.nodes:
    around.append((node, len(graph.getEdgesFrom(node)), len(graph.getEdgesTo(node)))) # export prvni, import druhy
exp = sorted(around, key=lambda n:n[1], reverse=True)[:1]
imp = sorted(around, key=lambda n:n[2], reverse=True)[:1]

print('Export: ' + exp[0][0] + ' (' + str(exp[0][1]) + ')')
print('Import: ' + imp[0][0] + ' (' + str(imp[0][2]) + ')')

