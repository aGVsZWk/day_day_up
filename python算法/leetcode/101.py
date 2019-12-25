# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.isSymmetricRenc(root.left, root.right)

    def isSymmetricRenc(self, left, right):
        if root is None and right is None:
            return True
        if left is None or right is None or left.val != right.val:
            return False
        return self.isSymmetricRenc(left.left, right.right) and self.isSymmetricRenc(left.right. right.left)
