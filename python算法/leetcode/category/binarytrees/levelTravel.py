# 层次遍历


def levelTravel(root):
    if not root:
        return []
    result, level = [], [root]
    while level:
        temp = []
        nextLevel = []
        for node in level:
            temp.append(node.val)
            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)
        level = nextLevel
    return result
