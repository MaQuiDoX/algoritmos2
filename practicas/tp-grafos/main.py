import linkedlist
from algo1 import *
from graph import *

Vertices = linkedlist.LinkedList()
Aristas = linkedlist.LinkedList()

Vert = [0,1,2,3]
Arist = [(0,1), (1,2),(2,3)]

for i in Vert:
    linkedlist.addList(Vertices, i)
for i in Arist:
    linkedlist.addList(Aristas, i)

Grafo = createGraph(Vertices,Aristas)

for i in range(len(Vert)):
    print(Grafo[i])
    
print("")
linkedlist.printlinkedlist(convertTree(Grafo))
