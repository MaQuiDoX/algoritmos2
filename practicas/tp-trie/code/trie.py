class Trie:
    root = None

class TrieNode:
    parent = None
    children = None
    key = None
    isEndOfWord = None
    
    
'''
insert(T,element) 
Descripción: insert un elemento en T, siendo T un Trie.
Entrada: El Trie sobre la cual se quiere agregar el elemento (Trie)  y el valor del elemento (palabra) a  agregar.
Salida:  No hay salida definida
'''
    
def insert(T, element):
    #Si el árbol está vacio se crea una nueva lista para el nodo root
    if T.root == None:
        S = []
        T.root = S
    #Si el árbol no está vacio se utiliza la lista ya existente
    else:
        S = T.root
    return insertR(T.root, S, element)

def insertR(lastNode, S, element):
    #Revisa cada nodo de la lista S buscando un nodo con la misma key que el elemento que se está insertando
    for node in S:
        if node.key == element[0]:
            #Si se encuentra un nodo con la misma key, lo seleccionamos como nodo y continuamos la recursion
            trieNode = node
            break
    else:
        #Si no se encuentra un nodo con la misma key, se crea un nuevo nodo y se agrega a la lista S
        trieNode = TrieNode()
        trieNode.key = element[0]
        trieNode.parent = lastNode

        if len(element) == 1:
            trieNode.children = []
        else:
            trieNode.children = None
        S.append(trieNode)

    if len(element) != 1:
        #Si todavía hay elementos en la palabra, se llama recursivamente a la función insertR con los elementos restantes y la lista de hijos del nodo actual
        element = element[1:]
        if trieNode.children is None:
            # Si el nodo actual es una hoja, se crea un nuevo nodo vacío para sus hijos
            trieNode.children = []
        insertR(trieNode, trieNode.children, element)
    else:
        #Si se insertaron todos los elementos de la palabra se marca al nodo como el final de la palabra
        trieNode.isEndOfWord = True
        
'''
search(T,element)
Descripción: Verifica que un elemento se encuentre dentro del Trie
Entrada: El Trie sobre la cual se quiere buscar el elemento (Trie)  y el valor del elemento (palabra)
Salida: Devuelve False o True  según se encuentre el elemento.
'''

def search(T, element):
    return searchR(T.root, element)

def searchR(S, element):
    #Si la lista S es None el elemento no se encuentra en la lista
    if S == None:
        return False
    
    #Iteramos sobre los elementos de la lista S
    for i in range(len(S)):
        #Si encontramos un elemento cuya key es igual a la primera letra del elemento buscado, almacenamos su índice en la variable 'index' y salimos del bucle con 'break'
        if S[i].key == element[0]:
            index = i
            break
    else:
        #Si no encontramos ningún elemento cuya key sea igual a la primera letra del elemento buscado, significa que el elemento no se encuentra en el trie
        return False
    
    #Si todavía quedan letras por buscar en el elemento continuamos buscando en la lista de hijos
    if len(element) != 1:
        element = element[1:]
        return searchR(S[index].children, element)
    else:
        #Si ya no quedan letras por buscar en el elemento y el nodo actual es un nodo final de palabra entonces hemos encontrado el elemento buscado
        if S[index].isEndOfWord == True:
            return True
        else:
            return False
'''
delete(T,element)
Descripción: Elimina un elemento se encuentre dentro del Trie
Entrada: El Trie sobre la cual se quiere eliminar el elemento (Trie)  y el valor del elemento (palabra) a  eliminar.
Salida: Devuelve False o True  según se haya eliminado el elemento.
'''

'''
Implementar un algoritmo que dado un árbol Trie T, un patrón p y un entero n, escriba todas las palabras del árbol que 
empiezan por p y sean de longitud n. 
'''

def searchWords(T, patron, long):
    mainlist = getWords(T)
    for i in range(len(mainlist)):
        if len(mainlist[i]) == long and mainlist[i][0] == patron:
            print(mainlist[i])
    return

'''
Implementar un algoritmo que dado los Trie T1 y T2 devuelva True si estos pertenecen al mismo documento y False en caso contrario.
Se considera que un  Trie pertenecen al mismo documento cuando:
Ambos Trie sean iguales (esto se debe cumplir)
El Trie T1 contiene un subconjunto de las palabras del Trie T2 
Si la implementación está basada en LinkedList, considerar el caso donde las palabras hayan sido insertadas en un orden diferente.

En otras palabras, analizar si todas las palabras de T1 se encuentran en T2. 

Analizar el costo computacional.
'''
def getWords(T):
    words = []
    if T.root is not None:
        stack = [(node, '') for node in T.root]
        while stack:
            node, prefix = stack.pop()
            word = prefix + node.key
            if node.isEndOfWord:
                words.append(word)
            if node.children is not None:
                for child in reversed(node.children):
                    stack.append((child, word))
    return words

def sameWords(Trie1, Trie2):
    listTrie1 = sorted(getWords(Trie1))
    listTrie2 = sorted(getWords(Trie2))
    count = 0
    
    if len(listTrie1) != len(listTrie2):
        return False

    for i in range(len(listTrie1)):
        if listTrie1[i] == listTrie2[i]:
            count += 1
            if len(listTrie1) == count:
                return True
    
    return False
'''
Ejercicio 6
Implemente un algoritmo que dado el Trie T devuelva True si existen en el documento T dos cadenas invertidas. 
Dos cadenas son invertidas si se leen de izquierda a derecha y contiene los mismos caracteres que si se lee de derecha a izquierda, 
ej: abcd y dcba son cadenas invertidas, gfdsa y asdfg son cadenas invertidas, sin embargo abcd y dcka no son invertidas ya que difieren 
en un carácter.
'''

def twiceStringInverted(T):
    wordslist = getWords(T)

    for i in range(len(wordslist)):
        reversedword = "".join(reversed(wordslist[i]))
        for j in range(i, len(wordslist)):
            if reversedword == wordslist[j]:
                return True
    
    return False
'''
Ejercicio 7
Un corrector ortográfico interactivo utiliza un Trie para representar las palabras de su diccionario. 
Queremos añadir una función de auto-completar (al estilo de la tecla TAB en Linux): cuando estamos a medio escribir una palabra, 
si sólo existe una forma correcta de continuarla entonces debemos indicarlo. 
Implementar la función autoCompletar(Trie, cadena) dentro del módulo trie.py, que dado el árbol Trie T y la cadena “pal” 
devuelve la forma de auto-completar la palabra. Por ejemplo, para la llamada autoCompletar(T, ‘groen’) devolvería “land”, 
ya que podemos tener “groenlandia” o “groenlandés” (en este ejemplo la palabra groenlandia y groenlandés pertenecen al documento 
que representa el Trie). Si hay varias formas o ninguna, devolvería la cadena vacía. Por ejemplo, autoCompletar(T, ma’) devolvería “” si T 
presenta las cadenas “madera” y “mama”. 
'''
