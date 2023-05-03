class LinkedList:
  head=None

class Node:
  value=None
  nextNode=None

# O(1)
def addList(L, element):
  current=L.head
  newNode=Node()
  newNode.value=element
  
  if (current==None):
    L.head=newNode
  else:
    newNode.nextNode=current
    L.head=newNode
  return None

# O(n)
def searchList(L, element):
  current=L.head

  while (current != None):
    if (current.value == element):
      return True
      
    current=current.nextNode

# O(n)
def insertList(L, element, position):
  current=L.head
  pos=0
  
  if (position==0):
    addList(L, element)
    return position
  elif (position > 0):
    if (current == None):
      return None
    newNode=Node()
    newNode.value=element
    while (current.nextNode != None):
      if (pos+1 != position):
        current=current.nextNode
        pos += 1
      else:
        newNode.nextNode=current.nextNode
        current.nextNode=newNode
        return position
    current.nextNode=newNode
    return pos+1
  return None

# O(n)
def deleteList(L, element):
  current=L.head
  position=searchList(L, element)
  if (position == None):
    return None
  if (position == 0):
    L.head = L.head.nextNode
    return position

  for i in range(0, position-1):
    current=current.nextNode
  current.nextNode=current.nextNode.nextNode
  return position

# O(n)
def lengthList(L):
  current=L.head
  position=0

  while (current != None):
    current = current.nextNode
    position += 1
  return position

# O(n)
def accessList(L, position):
  current=L.head
  if (position >= 0):
    for n in range(0,position):
      if (current==None):
        return None
      current=current.nextNode
    return current.value
  else:
    return None

# O(n)
def updateList(L, element, position):
  current=L.head
  if (position >= 0):
    for n in range(0, position):
      current=current.nextNode
      if (current==None):
        return None
    current.value = element
    return position
  return

def printlinkedlist(L):
  current = L.head
  print("[ ", end="")
  while current:
    print (current.value, end=" ")
    current = current.nextNode
  print("]")

    
def swapNodes(A, pos1, pos2):
  if pos1 == pos2:
    return

  PrevNodo1 = None
  nodo1 = A.head
  for i in range(pos1):
    if nodo1 is None:
      return
    PrevNodo1 = nodo1
    nodo1 = nodo1.nextNode

  PrevNode2 = None
  nodo2 = A.head
  for i in range(pos2):
    if nodo2 is None:
      return
    PrevNode2 = nodo2
    nodo2 = nodo2.nextNode

  if PrevNodo1 != None:
    PrevNodo1.nextNode = nodo2
  else:
    A.head = nodo2

  if PrevNode2 != None:
    PrevNode2.nextNode = nodo1
  else:
    A.head = nodo1

  temp = nodo1.nextNode
  nodo1.nextNode = nodo2.nextNode
  nodo2.nextNode = temp
