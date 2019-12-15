def preorder(tree):
    # 前序遍历
    if tree:
        print(tree.key)
        preorder(tree.leftChild)
        preorder(tree.rightChild)

def postorder(tree):
    # 后序遍历
    if tree:
        postorder(tree.leftChild)
        postorder(tree.rightChild)
        print(tree.key)

def inorder(tree):
    # 中序遍历
    if tree:
       inorder(tree.leftChild)
       print(tree.key)
       inorder(tree.rightChild)
