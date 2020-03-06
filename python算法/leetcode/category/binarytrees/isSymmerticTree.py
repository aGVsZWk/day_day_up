# 判断二叉树是否对称


def isSymmerticTree(root):
    if rot:
        return isSameVal(root.left, root.right)
    else:
        return True

def isSameVal(p, q):
    if not p and not q:
        return True
    elif p and q and p.val == q.val:
        return isSameVal(p.left, q.right) and isSameVal(p.right, q.left)
    else:
        return False
