import linkedlist
from algo1 import *
from graph import *

Vertices = linkedlist.LinkedList()
Aristas = linkedlist.LinkedList()


Vert = [0,1,2,3,4,5,6]
Arist = [(0,1), (1,2),(2,3),(2,5),(3,1),(4,2),(4,5),(5,6)]

'''
Vert = [0,1,2,3,4,5,6,7]
Arist = [(0,1), (1,2),(2,3),(4,5),(5,6)]
'''

for i in Vert:
    linkedlist.addList(Vertices, i)
for i in Arist:
    linkedlist.addList(Aristas, i)

Grafo = createGraph(Vertices,Aristas)

for i in range(len(Vert)):
    print(Grafo[i])

edges = []
    
Grafoaux, edges = convertTree(Grafo)

print("")
for i in range(len(Vert)):
    print(Grafoaux[i])

print(edges)

camino = bestRoad(Grafo, 0, 6)

print(camino)

'''
print("")
print("GRAFO BFS")
print("")
GrafoBFS = convertToBFSTree(Grafo, 0)

for i in range(len(Grafo)):
    print(GrafoBFS[i])

'''
print("")
print("GRAFO DFS")
print("")
GrafoDFS = convertToDFSTree(Grafo, 0)

for i in range(len(Grafo)):
    print(GrafoDFS[i])
