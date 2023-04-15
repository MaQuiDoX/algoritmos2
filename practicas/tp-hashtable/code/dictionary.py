import linkedlist
from algo1 import *

def dictionary(long):
    d = Array(long, linkedlist.LinkedList())
    return d

def hash(key, mod):
    return key % mod

# --------------------------------------------- PARTE 1 ---------------------------------------------

#EJERCICIO 2

'''
insert(D,key, value)
Descripción: Inserta un key en una posición determinada por la función de hash (1)  en el diccionario (dictionary). Resolver colisiones por encadenamiento. En caso de keys duplicados se anexan a la lista.
Entrada: el diccionario sobre el cual se quiere realizar la inserción  y el valor del key a insertar 
Salida: Devuelve D
'''

def insert(D, key, value):
    newNode = (key, value)
    newKey = hash(key, len(D))

    if D[newKey] == None:
        newList = linkedlist.LinkedList()
        linkedlist.addList(newList, newNode)
        D[newKey] = newList
    else:
        linkedlist.addList(D[newKey], newNode)
    return D
        
'''
search(D,key)
	Descripción: Busca un key en el diccionario
Entrada: El diccionario sobre el cual se quiere realizar la búsqueda (dictionary) y el valor del key a buscar.
Salida: Devuelve el value de la key.  Devuelve None si el key no se encuentra.
'''

def searchinList(D, key, newKey):
    currentNode = D[newKey].head
    while currentNode != None:
        if currentNode.value[0] == key:
            return currentNode.value[1]
        currentNode = currentNode.nextNode
    return None

def search(D, key):
    newKey = hash(key, len(D))
    
    if D[newKey] == None:
        return None
    else:
        return searchinList(D, key, newKey)
    return None
'''
delete(D,key)
Descripción: Elimina un key en la posición determinada por la función de hash (1) del diccionario (dictionary) 
Poscondición: Se debe marcar como nulo  el key  a eliminar.  
Entrada: El diccionario sobre el se quiere realizar la eliminación  y el valor del key que se va a eliminar.
Salida: Devuelve D
'''

def delete(D,key):
    newKey = hash(key, len(D))
    
    if D[newKey] == None:
        return D
    
    if D[newKey].head.value[0] == key:
        D[newKey].head = D[newKey].head.nextNode
        if D[newKey].head == None:
            D[newKey] = None
        return D
    
    currentNode = D[newKey].head
    while currentNode.nextNode != None:
        if currentNode.nextNode.value[0] == key:
            currentNode.nextNode = currentNode.nextNode.nextNode
            return D
        currentNode = currentNode.nextNode
    return D

# --------------------------------------------- PARTE 2 ---------------------------------------------


# EJERCICIO 4

'''
Implemente un algoritmo lo más eficiente posible que devuelva True o False a la siguiente proposición: 
dado dos strings s1...sk  y p1...pk, se quiere encontrar si los caracteres de p1...pk corresponden a una permutación de s1...sk. 
Justificar el coste en tiempo de la solución propuesta.
'''

def isPermutation(S, P):
    if len(S) != len(P):
        return False
    
    stringDict = dictionary(ord("z") - ord("a"))
    
    for i in range(len(S)):
        keyS = ord(S[i]) - ord("a")
        insert(stringDict, keyS, S[i])
    
    for j in range(len(P)):
        keyD = ord(P[j]) - ord("a")
        delete(stringDict, keyD)
        
    for k in range(len(stringDict)):
        if stringDict[k] != None:
            return False
    return True
    

# EJERCICIO 5

'''
Implemente un algoritmo que devuelva True si la lista que recibe de entrada tiene todos sus elementos únicos, 
y Falso en caso contrario. Justificar el coste en tiempo de la solución propuesta.
'''

def Unique(L):
    
    listDict = dictionary(len(L))
    
    for i in range(len(L)):
        key = hash(L[i], len(L))
        if search(listDict, key) != None:
            return False
        else:
            insert(listDict, key, L[i])
    return True

# EJERCICIO 6

'''
Los nuevos códigos postales argentinos tienen la forma cddddccc, donde c indica un carácter (A - Z) y d indica un dígito 0, . . . , 9. 
Por ejemplo, C1024CWN es el código postal que representa a la calle XXXX a la altura 1024 en la Ciudad de Mendoza. Encontrar e implementar 
una función de hash apropiada para los códigos postales argentinos.
'''

def hashPostal(codigopostal, mod):
    sumatoria = 0
    i = 1
    for c in codigopostal:
        if c.isalpha():
            sumatoria = sumatoria + ord(c) * i
            i += 1
        elif c.isdigit():
            sumatoria = sumatoria + int(c) * i
            i += 1
            
    return sumatoria % mod
            
# EJERCICIO 7

'''
Implemente un algoritmo para realizar la compresión básica de cadenas utilizando el recuento de caracteres repetidos. Por ejemplo, 
la cadena ‘aabcccccaaa’ se convertiría en ‘a2blc5a3’. Si la cadena "comprimida" no se vuelve más pequeña que la cadena original, 
su método debería devolver la cadena original. Puedes asumir que la cadena sólo tiene letras mayúsculas y minúsculas (a - z, A - Z). 
Justificar el coste en tiempo de la solución propuesta.
'''

def Compile(P):
    compileDict = dictionary(len(P))
    key = 0
    
    insert(compileDict, key, P[0])
    for i in range(1, len(P)):
        if P[i] == P[i-1]:
            insert(compileDict, key, P[i])
        else:
            key += 1
            insert(compileDict, key, P[i])
    
    stringFinal = ""
    contador = key
    
    for j in range(contador):
        stringFinal = stringFinal + compileDict[j].head.value[1]
        stringFinal = stringFinal + str(linkedlist.lengthList(compileDict[j]))
        
    if len(stringFinal) >= len(P):
        return P
    return stringFinal

# EJERCICIO 8

'''
Se requiere encontrar la primera ocurrencia de un string p1...pk en uno más largo a1...aL. 
Implementar esta estrategia de la forma más eficiente posible con un costo computacional menor a O(K*L) (solución por fuerza bruta).  
Justificar el coste en tiempo de la solución propuesta.
'''

def subString(S, P):
    longS = len(S)
    longP = len(P)
    
    if longS < longP:
        return None
    
    hashP = sum(ord(P[i]) for i in range(longP))
    hashS = sum(ord(S[i]) for i in range(longP))
    
    if hashP == hashS and P == S[:longP]:
        return 0
    
    for i in range(longP, longS):
        hashS += ord(S[i]) - ord(S[i-longP])
        
        if hashP == hashS and P == S[i-longP+1:i+1]:
            return i-longP+1
    return None

# EJERCICIO 9

'''
Considerar los conjuntos de enteros S = {s1, . . . , sn} y T = {t1, . . . , tm}. Implemente un algoritmo que utilice una tabla de hash 
para determinar si S ⊆ T (S subconjunto de T). ¿Cuál es la complejidad temporal del caso promedio del algoritmo propuesto?
'''

def isSubset(S, T):
    subSetDict = dictionary(len(T))
    
    for i in range(len(T)):
        insert(subSetDict, hash(T[i], len(T)), T[i])
        
    for j in range(len(S)):
        if search(subSetDict, S[j]) == None:
            return False
    
    return True