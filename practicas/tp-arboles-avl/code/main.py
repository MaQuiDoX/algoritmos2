from avltree import *
from printtree import printBinaryTree
import random

A = AVLTree()

'''
for _ in range(11):
    insertAVL(A, 1, random.randint(0, 100))
'''

insertAVL(A, 10, 10)
insertAVL(A, 11, 11)
insertAVL(A, 12, 12)
insertAVL(A, 13, 13)
insertAVL(A, 14, 14)

printBinaryTree(A.root)

delete(A, 13)

printBinaryTree(A.root)