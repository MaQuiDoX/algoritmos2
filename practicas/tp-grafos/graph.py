from algo1 import *
import linkedlist

# ------------------------------ PARTE 1 ------------------------------

'''
EJERCICIO 1

def createGraph(List, List) 
Descripción: Implementa la operación crear grafo
Entrada: LinkedList con la lista de vértices y LinkedList con la lista de aristas donde por cada par de elementos representa 
una conexión entre dos vértices.
Salida: retorna el nuevo grafo
'''

def createGraph(ListVertices, ListAristas):
    longVert = linkedlist.lengthList(ListVertices) + 1
    Grafo = [ [] for _ in range(longVert) ]
    
    for i in range(len(Grafo)):
        Grafo[i] = []
        
    currentNode = ListAristas.head
    while currentNode != None:
        Grafo[currentNode.value[0]].append(currentNode.value[1])
        Grafo[currentNode.value[1]].append(currentNode.value[0])
        currentNode = currentNode.nextNode
    return Grafo
'''
EJERCICIO 2

def existPath(Grafo, v1, v2): 
Descripción: Implementa la operación existe camino que busca si existe un camino entre los vértices v1 y v2 
Entrada: Grafo con la representación de Lista de Adyacencia, v1 y v2 vértices en el grafo.
Salida: retorna True si existe camino entre v1 y v2, False en caso contrario.
'''

def existPath(Grafo, v1, v2):
    visitados = [False] * len(Grafo)-1
    return searchPath(Grafo, v1, v2, visitados)

def searchPath(Grafo, v, v2, visitados):
    visitados[v] = True
    
    if v == v2:
        return True
    
    for u in Grafo[v]:
        if not visitados[u]:
            if searchPath(Grafo, u, v2, visitados):
                return True
    return False

'''
EJERCICIO 3

def isConnected(Grafo): 
Descripción: Implementa la operación es conexo 
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: retorna True si existe camino entre todo par de vértices, False en caso contrario.
'''

def isConnected(Grafo):
    longVert = len(Grafo)-1
    visitados = []
    
    searchIfConnected(visitados, Grafo, 0)

    if len(visitados) == longVert:
        return True
    return False

def searchIfConnected(visitados, Grafo, vertice):
    visitados.append(vertice)
    for element in Grafo[vertice]:
        if element not in visitados:
            searchIfConnected(visitados, Grafo, element)

'''
EJERCICIO 4

def isTree(Grafo): 
Descripción: Implementa la operación es árbol 
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: retorna True si el grafo es un árbol.
'''

def isTree(Grafo):
    if isConnected(Grafo) == False:
        return False
    
    visitado = [False] * (len(Grafo)-1)
    if hasCycle(Grafo,0,visitado,-1) == True:
        return False
    return True

def hasCycle(Grafo,currentNode,visitado,parent):
    visitado[currentNode] = True
    
    for i in range(len(Grafo[currentNode])):
        aux = Grafo[currentNode][i]
        
        if not visitado[aux]:
            if hasCycle(Grafo, aux, visitado, currentNode):
                return True
            
        elif aux != parent:
            return True
    return False
'''
EJERCICIO 5

def isComplete(Grafo): 
Descripción: Implementa la operación es completo 
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: retorna True si el grafo es completo.
'''

def isComplete(Grafo):
    vertices = len(Grafo)-1

    for i in range(vertices):
        if vertices-1 != len(Grafo[i]):
            return False
    return True

'''
EJERCICIO 6

def convertTree(Grafo)
Descripción: Implementa la operación es convertir a árbol 
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: LinkedList de las aristas que se pueden eliminar y el grafo resultante se convierte en un árbol.
'''

def convertTree(Grafo):
    if isTree(Grafo)==True:
        return linkedlist.LinkedList()
    

# ------------------------------ PARTE 2 ------------------------------

'''
EJERCICIO 7

def countConnections(Grafo):
Descripción: Implementa la operación cantidad de componentes conexas 
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: retorna el número de componentes conexas que componen el grafo.
'''

'''
EJERCICIO 8

def convertToBFSTree(Grafo, v):
Descripción: Convierte un grafo en un árbol BFS
Entrada: Grafo con la representación de Lista de Adyacencia, v vértice que representa la raíz del árbol
Salida: Devuelve una Lista de Adyacencia con la representación BFS del grafo recibido usando v como raíz.
'''

'''
EJERCICIO 9

def convertToDFSTree(Grafo, v):
Descripción: Convierte un grafo en un árbol DFS
Entrada: Grafo con la representación de Lista de Adyacencia, v vértice que representa la raíz del árbol
Salida: Devuelve una Lista de Adyacencia con la representación DFS del grafo recibido usando v como raíz.
'''

'''
EJERCICIO 10

def bestRoad(Grafo, v1, v2):
Descripción: Encuentra el camino más corto, en caso de existir, entre dos vértices.
Entrada: Grafo con la representación de Lista de Adyacencia, v1 y v2 vértices del grafo.
Salida: retorna la lista de vértices que representan el camino más corto entre v1 y v2. La lista resultante 
contiene al inicio a v1 y al final a v2. En caso que no exista camino se retorna la lista vacía.
'''