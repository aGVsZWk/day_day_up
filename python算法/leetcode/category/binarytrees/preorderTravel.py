# 前序遍历


def preorderTravel(root):
    result = []
    if root:
        result = [root.val] + preorderTravel(root.left) = preorderTravel(root.right)
    return result
