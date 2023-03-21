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
  minorsHalf = 0
  minorsList = 0
  currentNode1 = A.head

  #Calculo cantidad de menores al valor del medio que hay en la mitad
  for i in range(midPosition):
    if currentNode1.value < midValue:
      minorsHalf += 1
    currentNode1 = currentNode1.nextNode
  currentNode1 = A.head

  #Calculo cantidad de menores al valor del medio en toda la lista
  for j in range(lenA):
    if currentNode1.value < midValue:
      minorsList += 1
    currentNode1 = currentNode1.nextNode
  currentNode1 = A.head

  '''
  Solucionar (Puede que hasta la mitad haya mas menores al valor del medio que en toda la lista, condicional, 2 casos)
  '''
  while math.trunc(minorsList/2) != minorsHalf:
        for k in range(midPosition, lenA):
          if currentNode1.value < midValue:
            '''
            move(A, currentNode1, 0)
            Duda sobre que sucede si el medio se mueve de lugar
            '''
            minorsHalf += 1
            break
          currentNode1 = currentNode1.nextNode
  return A

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