class BinaryTree(object):
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def preorder(self):
        # 前序遍历
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()


import unittest

class BinaryTreeTest(unittest.TestCase):
    def setUp(self):
        self.tree = BinaryTree('a')

    def test_binary_tree(self,):
        self.tree.insertLeft('b')
        self.tree.insertRight('c')
        self.tree.getRightChild().setRootVal('hello')
        self.tree.getLeftChild().setRootVal('d')

if __name__ == '__main__':
    unittest.main()
