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
  position=0

  while (current != None):
    if (current.value == element):
      return position
      
    current=current.nextNode
    position += 1

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
  print("]\n")