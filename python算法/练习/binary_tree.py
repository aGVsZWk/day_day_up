class BinaryTree(object):
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, data):
        node = BinaryTree(data)
        node.leftChild = self.leftChild
        self.leftChild = node

    def insertRight(self, data):
        node = BinaryTree(data)
        node.rightChild = self.rightChild
        self.rightChild = node

    def getRootVal(self, root):
        return root.data

    def setRootVal(self, root, data):
        root.data = data

    def preOrder(self):
        # 前序遍历
        print(self.data)
        if self.leftChild:
            self.preOrder(self.leftChild)
        if self.rightChild:
            self.preOrder(self.rightChild)

    def postOrder(self):
        # 后序遍历
        if self.leftChild:
            self.postOrder(self.leftChild)
        if self.rightChild:
            self.postOrder(self.rightChild)
        print(self.data)

    def inOrder(self):
        # 中序遍历
        if self.leftChild:
            self.inOrder(self.leftChild)
        print(self.data)
        if self.rightChild:
            self.inOrder(self.rightChild)
