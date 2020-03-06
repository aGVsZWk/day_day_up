# 后序遍历


def postorderTravel(root):
    result = []
    if root:
        result = postorderTravel(root.left) + postorderTravel(root.right) + [root.val]
    return result
