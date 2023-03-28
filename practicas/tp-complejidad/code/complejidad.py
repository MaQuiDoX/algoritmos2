from linkedlist import *
import math
import random

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
  currentNode1 = currentNode1.nextNode

  #Calculo cantidad de menores al valor del medio que hay en la segunda mitad
  for j in range(midPos+1, lenA):
    if currentNode1.value < midValue:
      minorsSecondHalf += 1
    currentNode1 = currentNode1.nextNode
  currentNode1 = A.head

  return minorsFirstHalf, minorsSecondHalf

def updatePositionLists(A, midPosition, midValue, listMinorFirstHalf, listMinorSecondHalf, listMayorFirstHalf, listMayorSecondHalf):
  currentNode1 = A.head
  position = 0
  lenA = lengthList(A)
  
  #Asigno a 1 lista las posiciones de los valores mayores al valor del medio de la primera mitad y a la otra lista y los valores menores
  for k in range(midPosition):
    if currentNode1.value < midValue:
      listMinorFirstHalf.append(position)
      position += 1
    elif currentNode1.value >= midValue:
      listMayorFirstHalf.append(position)
      position += 1
    currentNode1 = currentNode1.nextNode
    
  currentNode1 = currentNode1.nextNode
  position += 1

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

  return listMinorFirstHalf, listMinorSecondHalf, listMayorFirstHalf, listMayorSecondHalf
  
def orderHalfMinors(A):
  lenA = lengthList(A)-1
  midPosition = math.trunc(lenA/2)
  midValue = accessList(A, midPosition)
  minorsFirstHalf = 0
  minorsSecondHalf = 0
  listMayorFirstHalf = []
  listMinorFirstHalf = []
  listMayorSecondHalf = []
  listMinorSecondHalf = []

  minorsFirstHalf, minorsSecondHalf = checkMinorsBothSides(A, midValue, midPosition, minorsFirstHalf, minorsSecondHalf)
  listMinorFirstHalf, listMinorSecondHalf, listMayorFirstHalf, listMayorSecondHalf = updatePositionLists(A, midPosition, midValue, listMinorFirstHalf, listMinorSecondHalf, listMayorFirstHalf, listMayorSecondHalf)

  differenceMinors = minorsFirstHalf - minorsSecondHalf
  print("Pivote: ", midValue, ". Posición: ", midPosition)
  
  #A partir de la diferencia entre los menores que se encuentren a la izquierda y a la derecha del pivote,
  #a partir del lado que tienga mas menores realizo intercambios de estos con los mayores que se encuentren del otro lado
  while differenceMinors != 0 and differenceMinors != 1 and differenceMinors != -1:
    if minorsFirstHalf > minorsSecondHalf:
      swapNodes(A, listMinorFirstHalf[0], listMayorSecondHalf[0])
      listMinorSecondHalf.insert(0, listMinorFirstHalf.pop(0))
      listMayorFirstHalf.insert(0, listMayorSecondHalf.pop(0))
      minorsFirstHalf = 0
      minorsSecondHalf = 0
      minorsFirstHalf, minorsSecondHalf = checkMinorsBothSides(A, midValue, midPosition, minorsFirstHalf, minorsSecondHalf)
      differenceMinors = minorsFirstHalf - minorsSecondHalf
    elif minorsFirstHalf < minorsSecondHalf:
      swapNodes(A, listMayorFirstHalf[0], listMinorSecondHalf[0])
      listMinorFirstHalf.insert(0, listMinorSecondHalf.pop(0))
      listMayorSecondHalf.insert(0, listMayorFirstHalf.pop(0))
      minorsFirstHalf = 0
      minorsSecondHalf = 0
      minorsFirstHalf, minorsSecondHalf = checkMinorsBothSides(A, midValue, midPosition, minorsFirstHalf, minorsSecondHalf)
      differenceMinors = minorsFirstHalf - minorsSecondHalf
    else:
      return A
  else: 
    return A

A = LinkedList()

for i in range(20):
  addList(A, random.randint(1, 20))

printlinkedlist(A)
A = orderHalfMinors(A)
printlinkedlist(A)