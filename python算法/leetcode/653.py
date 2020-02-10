# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root or (not root.left and not root.right):
            return False

        self.values = []
        self.inOrder(root)
        for i, v in enumerate(self.values):
            if self.values[i] != k - v and (k - v) in self.values:
                return True
        return False

    def inOrder(self, node):
        if node:
            self.inOrder(node.left)
            self.values.append(node.val)
            self.inOrder(node.right)
