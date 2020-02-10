# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s:
            return False
        if self.isSameTree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


    def isSameTree(self, s, t):
        if not t and not s:
            return True
        elif (not t) or (not s) or (s.val != t.val):
            return False
        else:
            return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
