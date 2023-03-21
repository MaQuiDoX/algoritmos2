from linkedlist import *

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
