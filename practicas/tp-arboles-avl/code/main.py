from avltree import *
from printtree import printBinaryTree
import random

A = AVLTree()


for _ in range(10):
    insert(A, 1, random.randint(0, 100))

calculateBalance(A)
printBinaryTree(A.root)

reBalance(A)

print("")

printBinaryTree(A.root)