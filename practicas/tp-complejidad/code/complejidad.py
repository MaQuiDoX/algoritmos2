from linkedlist import *
import math

def ContieneSuma(A, n):
  lenA = lengthList(A)
  lenB = lengthList(A)
  currentNode = A.head
  currentNode2 = A.head
  
  for i in range(lenA):
    valor = currentNode2.value
    for j in range(lenB-1):
      currentNode = currentNode.nextNode
      if valor + currentNode.value == n:
        return True
    currentNode2 = currentNode2.nextNode
    currentNode = currentNode2
    lenB = lenB - 1
  return False

def orderHalfMinors(A):
  lenA = lengthList(A)
  midPosition = math.trunc(lenA/2)-1
  midValue = accessList(A, midPosition)
  minorsFirstHalf = 0
  minorsSecondHalf = 0
  position = 0
  currentNode1 = A.head
  listMayorPositions = []
  listMinorPositions = []

  #Calculo cantidad de menores al valor del medio que hay en la primera mitad
  for i in range(midPosition):
    if currentNode1.value < midValue:
      minorsFirstHalf += 1
    currentNode1 = currentNode1.nextNode
  currentNode1 = A.head

  #Calculo cantidad de menores al valor del medio que hay en la segunda mitad
  for j in range(midPosition, lenA):
    if currentNode1.value < midValue:
      minorsSecondHalf += 1
    currentNode1 = currentNode1.nextNode
  currentNode1 = A.head

  for k in range(lenA):
    if currentNode1.value < midValue:
      listMinorPositions.append(position)
      position += 1
    elif currentNode1.value >= midValue:
      listMayorPositions.append(position)
      position += 1

    
  '''
  Solucionar (Puede que hasta la mitad haya mas menores al valor del medio que en toda la lista, condicional, 2 casos)

  En vez de calcular la mitad truncada de la mitad de la lista, mejor me conviene calcular los menores que se encuentran en la izquierda y en la derecha,
  y al momento de swapear los nodos dependiendo de cada caso, realizar la operacion correspondiente (sumar de un lado, rstar del otro) hasta que queden parejos y terminar el while...

  Hacer 2 arrays que guaden la posicion de los nodos mayores y menores, al momento de acceder a los nodos con las respectivas posiciones, eliminar las posiciones ya utilizadas.
  '''


A = LinkedList()
addList(A,1)
addList(A,1)
addList(A,2)
addList(A,8)
addList(A,4)
addList(A,7)
addList(A,1)
addList(A,6)

printlinkedlist(A)

orderHalfMinors(A)

printlinkedlist(A)