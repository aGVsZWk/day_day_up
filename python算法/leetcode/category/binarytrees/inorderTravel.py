# 中序遍历


def inorderTravel(root):
    result = []
    if root:
        result = inorderTravel(root.left) + [root.val] + inorderTravel(root.right)
    return result
