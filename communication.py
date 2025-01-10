from graph import Graph
import fileinput

nodes = []
edges = []
i=0

for line in fileinput.input():
    if i==0:
        line = line.replace(' ', '').replace('\n', '').split(':')
        nodes = line[1].split(',')
    else:
        edge = line.replace(' ', '').replace('\n', '').split('->')
        edges.append((edge[0], edge[1]))
    i = i + 1

graph = Graph(nodes, edges)
result = []

for node in graph.nodes:
    whoIWrite = graph.getEdgesFrom(node)
    whoWritesMe = graph.getEdgesTo(node)
    for friend in whoIWrite:
        if friend not in whoWritesMe:
            result.append((friend,node))

for badcomunication in result:
    print(badcomunication[0], " -> ", badcomunication[1])
        
