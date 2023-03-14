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
     return
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

def insertTree(B, element, key):
   newNode = BinaryTreeNode()
   newNode.key = key
   newNode.value = element
   if (B.root == None):
     B.root = newNode
     return key
   return insertR(newNode, B.root)

def insertR(newNode, currentNode):
   if newNode.key > currentNode.key:
     if currentNode.rightnode == None:
       newNode.parent = currentNode
       currentNode.rightnode = newNode
       return newNode.key
     else:
       right = insertR(newNode, currentNode.rightnode)
       if right != None:
         return right

   else:
     if currentNode.leftnode == None:
       newNode.parent = currentNode
       currentNode.leftnode = newNode
       return newNode.key
     else:
       left = insertR(newNode, currentNode.leftnode)
       if left != None:
         return left

'''      
delete(B,element)
Descripción: Elimina un elemento del TAD árbol binario.
Poscondición: Se debe desvincular el Node a eliminar.
Entrada: el árbol binario B sobre el cual se quiere realizar la eliminación (BinaryTree) y el valor del elemento (element) a eliminar.
Salida: Devuelve clave (key) del elemento a eliminar. Devuelve None si el elemento a eliminar no se encuentra.
'''

def deleteTree(B, element):
  node = searchNode(B, element)
  if node == None:
    return
  else:
    return deleteR(B, node)

def searchNode(B, element):
   return searchR(B.root, element)

def deleteR(B, node):
   if node.rightnode == None:
     if node.leftnode == None:
       #eliminar hoja
       if node.parent.leftnode != None and node.parent.leftnode == node:
         node.parent.leftnode = None
         return node.key
       elif node.parent.rightnode != None and node.parent.rightnode == node:
         node.parent.rightnode = None
         return node.key
     #hoja del lado izquierdo
     if node.parent.leftnode != None and node.parent.leftnode == node:
       node.parent.leftnode = node.leftnode
       return node.key
     elif node.parent.rightnode != None and node.parent.rightnode == node:
       node.parent.rightnode = node.leftnode
       return node.key
   else:
     #hoja del lado derecho
     if node.leftnode == None:
       if node.parent.leftnode == node:
         node.parent.leftnode = node.rightnode
         return node.key
       elif node.parent.rightnode == node:
         node.parent.rightnode = node.rightnode
         return node.key

     else:
       #2 hojas, elimina el menor de los mayores
       newNode = smaller(node.rightnode)
       node.value = newNode.value
       oldKey = node.key
       node.key = newNode.key
    
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

def accessTree(B, key):
   node = searchKey(B.root, key)
   if (node == None):
     return None
   else:
     return node.value

def searchKey(node, key):
   if (node == None):
     return None

   if (node.key == key):
     return node

   rightN = searchKey(node.rightnode, key)
   if (rightN != None):
     return rightN

   leftN = searchKey(node.leftnode, key)
   if (leftN != None):
     return leftN

'''
update(L,element,key)
Descripción: Permite cambiar el valor de un elemento del árbol binario con una clave determinada.
Entrada: El árbol binario (BinaryTree) y la clave (key) sobre la cual se quiere asignar el valor de element.
Salida: Devuelve None si no existe elemento para dicha clave. Caso contrario devuelve la clave del nodo donde se hizo el update.
'''

def updateTree(L, element, key):
   node = searchKey(L.root, key)
   if (node == None):
     return
   else:
     node.value = element
     return node.key

'''
calculateBalance(AVLTree) 
Descripción: Calcula el factor de balanceo de un árbol binario de búsqueda. 
Entrada: El árbol AVL  sobre el cual se quiere operar.
Salida: El árbol AVL con el valor de balanceFactor para cada subarbol
'''

def calculateBalance(AVLTree):
   return calculateBalanceR(AVLTree, AVLNode.root)

def calculateBalanceR(AVLTree, AVLNode):
   if AVLNode == None:
      return
   
   AVLNode.bf = treeHeight(AVLNode.leftnode) - treeHeight(AVLNode.rightnode)

   calculateBalanceR(AVLTree, AVLNode.leftnode)
   calculateBalanceR(AVLTree, AVLNode.rightnode)

def treeHeight(B):
    if B == None:
        return 0
    return 1 + max(treeHeight(B.leftnode), treeHeight(B.rightnode))

