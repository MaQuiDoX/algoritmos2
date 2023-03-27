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

def checkMinorsBothSides(A, midValue, midPos, minorsFirstHalf, minorsSecondHalf):
  currentNode1 = A.head
  lenA = lengthList(A)
  #Calculo cantidad de menores al valor del medio que hay en la primera mitad
  for i in range(midPos):
    if currentNode1.value < midValue:
      minorsFirstHalf += 1
    currentNode1 = currentNode1.nextNode
  currentNode1 = A.head

  #Calculo cantidad de menores al valor del medio que hay en la segunda mitad
  for j in range(midPos+1, lenA):
    if currentNode1.value >= midValue:
      minorsSecondHalf += 1
    currentNode1 = currentNode1.nextNode
  currentNode1 = A.head

  return minorsFirstHalf, minorsSecondHalf

def orderHalfMinors(A):
  lenA = lengthList(A)
  midPosition = math.trunc(lenA/2)-1
  midValue = accessList(A, midPosition)
  minorsFirstHalf = 0
  minorsSecondHalf = 0
  position = 0
  currentNode1 = A.head
  listMayorFirstHalf = []
  listMinorFirstHalf = []
  listMayorSecondHalf = []
  listMinorSecondHalf = []

  minorsFirstHalf, minorsSecondHalf = checkMinorsBothSides(A, midValue, midPosition, minorsFirstHalf, minorsSecondHalf)

  #Asigno a 1 lista las posiciones de los valores mayores al valor del medio de la primera mitad y a la otra lista y los valores menores
  for k in range(midPosition):
    if currentNode1.value < midValue:
      listMinorFirstHalf.append(position)
      position += 1
    elif currentNode1.value >= midValue:
      listMayorFirstHalf.append(position)
      position += 1
    currentNode1 = currentNode1.nextNode
  currentNode1 = A.head  

  #Asigno a 1 lista las posiciones de los valores mayores al valor del medio de la segunda mitad y a la otra lista y los valores menores
  for k in range(midPosition+1, lenA):
    if currentNode1.value < midValue:
      listMinorSecondHalf.append(position)
      position += 1
    elif currentNode1.value >= midValue:
      listMayorSecondHalf.append(position)
      position += 1
    currentNode1 = currentNode1.nextNode
  currentNode1 = A.head

  while (abs(minorsFirstHalf - minorsSecondHalf) != [1,0]):
    if minorsFirstHalf < minorsSecondHalf:
      swapNodes(A, listMinorFirstHalf[0], listMayorSecondHalf[0])
      minorsFirstHalf, minorsSecondHalf = checkMinorsBothSides(A, midValue, midPosition, minorsFirstHalf, minorsSecondHalf)
    elif minorsFirstHalf > minorsSecondHalf:
      swapNodes(A, listMinorFirstHalf[0], listMayorSecondHalf[0])
      minorsFirstHalf, minorsSecondHalf = checkMinorsBothSides(A, midValue, midPosition, minorsFirstHalf, minorsSecondHalf)
    else:
      return A
  return A

'''
Solucionar (Puede que hasta la mitad haya mas menores al valor del medio que en toda la lista, condicional, 2 casos)
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
A = orderHalfMinors(A)
printlinkedlist(A)