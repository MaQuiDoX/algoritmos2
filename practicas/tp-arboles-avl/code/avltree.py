class AVLTree:
    root = None

class AVLNode:
    parent = None
    leftnode = None
    rightnode = None
    key = None
    value = None
    bf = None

'''
search(B,element)
Descripción: Busca un elemento en el TAD árbol binario.
Entrada: el árbol binario B en el cual se quiere realizar la búsqueda (BinaryTree) y el valor del elemento (element) a buscar.
Salida: Devuelve la key asociada a la primera instancia del elemento. Devuelve None si el elemento no se encuentra.
'''

def search(B, element):
   node = searchR(B.root, element)
   if node == None:
      return
   else:
      return node.key

def searchR(node, element):
   if node == None:
      return None
   if node.value == element:
      return node

   right = searchR(node.rightnode, element)
   if right != None:
      return right
   left = searchR(node.leftnode, element)
   if left != None:
      return left
   
'''
insert(B,element,key)
Descripción: Inserta un elemento con una clave determinada del TAD árbol binario.
Entrada: el árbol B sobre el cual se quiere realizar la inserción (BinaryTree), el valor del elemento (element) a insertar y la clave (key) con la que se lo quiere insertar.
Salida: Si pudo insertar con éxito devuelve la key donde se inserta el elemento. En caso contrario devuelve None.
'''

def insertAVL(AVLTree, element, key):
  newNode = AVLNode()
  newNode.value = element
  newNode.key = key

  if AVLTree.root == None:
    AVLTree.root = newNode
  else:
    return insertR(newNode,AVLTree.root)
  return key

def insertR(newNode, currentNode):
  if newNode.key > currentNode.key:
    if currentNode.rightnode == None:
      currentNode.rightnode = newNode
      newNode.parent = currentNode
      return newNode.key
    currentNode = currentNode.rightnode
    return insertR(newNode, currentNode)
  elif newNode.key < currentNode.key:
    if currentNode.leftnode == None:
      currentNode.leftnode = newNode
      newNode.parent = currentNode
      return newNode.key
    currentNode = currentNode.leftnode
    return insertR(newNode, currentNode)
  else:
    return None

'''
delete(B,element)
Descripción: Elimina un elemento del TAD árbol binario.
Poscondición: Se debe desvincular el Node a eliminar.
Entrada: el árbol binario B sobre el cual se quiere realizar la eliminación (BinaryTree) y el valor del elemento (element) a eliminar.
Salida: Devuelve clave (key) del elemento a eliminar. Devuelve None si el elemento a eliminar no se encuentra.
'''

def deleteAVL(B, element):
  node = searchR(B, element)
  if node == None:
    return
  else:
    return deleteR(B, node)

def deleteR(B, AVLNode):
   if AVLNode.rightnode == None:
     if AVLNode.leftnode == None:
       #eliminar hijo
       if AVLNode.parent.leftnode != None and AVLNode.parent.leftnode == AVLNode:
         AVLNode.parent.leftnode = None
         return AVLNode.key
       elif AVLNode.parent.rightnode != None and AVLNode.parent.rightnode == AVLNode:
         AVLNode.parent.rightnode = None
         return AVLNode.key
       
     #hijo del lado izquierdo
     if AVLNode.parent.leftnode != None and AVLNode.parent.leftnode == AVLNode:
       AVLNode.parent.leftnode = AVLNode.leftnode
       return AVLNode.key
     elif AVLNode.parent.rightnode != None and AVLNode.parent.rightnode == AVLNode:
       AVLNode.parent.rightnode = AVLNode.leftnode
       return AVLNode.key
   else:
     
     #hijo del lado derecho
     if AVLNode.leftnode == None:
       if AVLNode.parent.leftnode == AVLNode:
         AVLNode.parent.leftnode = AVLNode.rightnode
         return AVLNode.key
       elif AVLNode.parent.rightnode == AVLNode:
         AVLNode.parent.rightnode = AVLNode.rightnode
         return AVLNode.key

     else:
       #2 hijos, elimina el menor de los mayores
       newNode = smaller(AVLNode.rightnode)
       AVLNode.value = newNode.value
       oldKey = AVLNode.key
       AVLNode.key = newNode.key

       if newNode.parent.leftnode == newNode:
         newNode.parent.leftnode = None
       elif newNode.parent.rightnode == newNode:
         newNode.parent.rightnode = None
       return oldKey

def smaller(node):
   if node.leftnode != None:
     current = smaller(node.leftnode)
     if current != None:
       return current
   else: return node

'''
access(B,key)
Descripción: Permite acceder a un elemento del árbol binario con una clave determinada.
Entrada: El árbol binario (BinaryTree) y la key del elemento al cual se quiere acceder.
Salida: Devuelve el valor de un elemento con una key del árbol
'''

def access(AVLTree, key):
   node = accessR(AVLTree.root, key)
   if (node == None):
      return None
   else:
      return node.value

def accessR(node, key):
   if (node == None):
      return None

   if (node.key == key):
      return node

   rightN = accessR(node.rightnode, key)
   if (rightN != None):
      return rightN

   leftN = accessR(node.leftnode, key)
   if (leftN != None):
      return leftN

'''
update(L,element,key)
Descripción: Permite cambiar el valor de un elemento del árbol binario con una clave determinada.
Entrada: El árbol binario (BinaryTree) y la clave (key) sobre la cual se quiere asignar el valor de element.
Salida: Devuelve None si no existe elemento para dicha clave. Caso contrario devuelve la clave del nodo donde se hizo el update.
'''

def update(AVLTree, key, newValue):
   node = accessR(AVLTree.root, key)
   if node == None:
      return
   else:
      node.value = newValue
      return node.key

'''
rotateLeft(Tree,avlnode)
Descripción: Implementa la operación rotación a la izquierda
Entrada: Un Tree junto a un AVLnode sobre el cual se va a operar la rotación a la  izquierda
Salida: retorna la nueva raíz
'''
def rotateLeft(AVLTree, AVLNode):
   newNode = AVLNode.rightnode
   AVLNode.rightnode = newNode.leftnode
   newNode.leftnode = AVLNode

   newNode.parent = AVLNode.parent
   AVLNode.parent = newNode
   if AVLNode.rightnode != None:
      AVLNode.rightnode.parent = AVLNode

   AVLNode.bf = getBalanceFactor(AVLNode)
   newNode.bf = getBalanceFactor(newNode)

   return newNode
'''
rotateRight(Tree,avlnode)
Descripción: Implementa la operación rotación a la derecha
Entrada: Un Tree junto a un AVLnode sobre el cual se va a operar la rotación a la  derecha
Salida: retorna la nueva raíz

'''
def rotateRight(AVLTree, AVLNode):
   newNode = AVLNode.leftnode
   AVLNode.leftnode = newNode.rightnode
   newNode.rightnode = AVLNode

   newNode.parent = AVLNode.parent
   AVLNode.parent = newNode
   if AVLNode.leftnode != None:
      AVLNode.leftnode.parent = AVLNode

   AVLNode.bf = getBalanceFactor(AVLNode)
   newNode.bf = getBalanceFactor(newNode)

   return newNode

'''
calculateBalance(AVLTree)
Descripción: Calcula el factor de balanceo de un árbol binario de búsqueda.
Entrada: El árbol AVL  sobre el cual se quiere operar.
Salida: El árbol AVL con el valor de balanceFactor para cada subarbol
'''

def calculateBalance(AVLTree):
   return calculateBalanceR(AVLTree, AVLTree.root)

def calculateBalanceR(AVLTree, AVLNode):
   if AVLNode == None:
      return None

   leftheight = treeHeight(AVLNode.leftnode)
   rightheight = treeHeight(AVLNode.rightnode)

   AVLNode.bf = leftheight - rightheight

   calculateBalanceR(AVLTree, AVLNode.leftnode)
   calculateBalanceR(AVLTree, AVLNode.rightnode)

   return AVLTree

def treeHeight(currentNode):
   if currentNode == None:
      return 0
   else:
      Left = treeHeight(currentNode.leftnode)
      Right = treeHeight(currentNode.rightnode)

      if Left > Right:
        return Left + 1
      else:
        return Right + 1

'''
reBalance(AVLTree)
Descripción: balancea un árbol binario de búsqueda. Para esto se deberá primero calcular el balanceFactor del árbol y luego en función de esto aplicar la estrategia de rotación que corresponda.
Entrada: El árbol binario de tipo AVL  sobre el cual se quiere operar.
Salida: Un árbol binario de búsqueda balanceado. Es decir luego de esta operación se cumple que la altura (h) de su subárbol derecho e izquierdo difieren a lo sumo en una unidad.
'''

def checkRebalance(AVLTree, AVLNode):
   calculateBalance(AVLTree)

   if AVLNode == None:
      return None
   
   balanceFactor = AVLNode.bf
   if balanceFactor != [-1, 0, 1]:
      return True
   
   left = checkRebalance(AVLTree, AVLNode.leftnode)
   if left != None:
      return left
   right = checkRebalance(AVLTree, AVLNode.rightnode)
   if right != None:
      return right
   
   return None

def reBalance(AVLTree):
   if AVLTree.root != None:
      AVLTree.root = reBalanceR(AVLTree, AVLTree.root)

   if checkRebalance(AVLTree, AVLTree.root) == True:
      AVLTree.root = reBalanceR(AVLTree, AVLTree.root)

def reBalanceR(AVLTree, AVLNode):

   if AVLNode.leftnode != None:
      AVLNode.leftnode = reBalanceR(AVLTree, AVLNode.leftnode)
   if AVLNode.rightnode != None:
      AVLNode.rightnode = reBalanceR(AVLTree, AVLNode.rightnode)

   AVLNode.bf = getBalanceFactor(AVLNode)

   if AVLNode.bf > 1:
      if AVLNode.leftnode.bf > 0:
          AVLNode = rotateRight(AVLTree, AVLNode)
      else:
          AVLNode.leftnode = rotateLeft(AVLTree, AVLNode.leftnode)
          AVLNode = rotateRight(AVLTree, AVLNode)

   elif AVLNode.bf < -1:
      if AVLNode.rightnode.bf < 0:
        AVLNode = rotateLeft(AVLTree, AVLNode)
      else:
        AVLNode.rightnode = rotateRight(AVLTree, AVLNode.rightnode)
        AVLNode = rotateLeft(AVLTree, AVLNode)

   return AVLNode

def getBalanceFactor(node):
   leftHeight = 0
   rightHeight = 0

   if node.leftnode != None:
      leftHeight = treeHeight(node.leftnode)

   if node.rightnode != None:
      rightHeight = treeHeight(node.rightnode)

   return int(leftHeight) - int(rightHeight)

'''
Ejercicio 4:
Implementar la operación insert() en  el módulo avltree.py garantizando que el árbol  binario resultante sea un árbol AVL.  
'''

def insert(AVLTree, element, key):
   newNode = AVLNode()
   newNode.value = element
   newNode.key = key

   if AVLTree.root == None:
      newNode.bf = 0
      AVLTree.root = newNode
      return key
   else:
      key = insertR(newNode, AVLTree.root)

   calculateBalance(AVLTree)

   if key != None:
      reBalance(AVLTree)
   return key


'''
Implementar la operación delete() en  el módulo avltree.py garantizando que el árbol  binario resultante sea un árbol AVL.
'''

def delete(AVLTree, element):
   node = searchR(AVLTree.root, element)
   if node == None:
      return
   else:
      key = deleteR(AVLTree, node)

   calculateBalance(AVLTree)

   if key != None:
      reBalance(AVLTree)
   return key