import operator


class Stack(object):
    def __init__(self):
        self._stack = []

    def push(self, value):
        self._stack.append(value)

    def pop():
        if self._stack:
            return self.pop()
        else:
            print("error: stack is empty")


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


def buildParseTree(fpexp):
    """解析表达式"""
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == "(":
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.leftChild()
        elif i not in ["+", "-", "*", "/", ")"]:   # i is num
            currentTree.key = int(i)
            parent = pStack.pop()
            currentTree = parent
        elif i in ["+", "-", "*", "/"]:
            currentTree.key = i
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.rightChild
        elif i == ")":
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree


def evaluate(parseTree):
    """表达式树求值"""
    opers = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
    leftC = parseTree.leftChild
    rightC = parseTree.rightChild
    if leftC and rightC:
        fn = opers[parseTree.key]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return parseTree.key


def postorderval(tree):
    """用后续遍历对表达式求值"""
    opers = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
    res1 = None
    res2 = None
    if tree:
        res1 = postorderval(tree.leftChild)
        res2 = postorderval(tree.rightChild)
        if res1 and res2:
            return opers[tree.key](res1, res2)
        else:
            return tree.key

           
