# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.maxDepth(root) >= 0

    def maxDepth(self, node):
        if node is None:
            return 0
        left_depth, right_depth = self.maxDepth(node.left), self.maxDepth(node.right)
        if left_depth == -1 or right_depth == -1 or abs(left_depth - right_depth) > 1:
            return -1
        return max(left_depth, right_depth) + 1




# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def getHeight(node):
            if node is None:
                return 0
            left_height, right_height = getHeight(node.left), getHeight(node.right)
            if left_height < 0 or right_height < 0 or abs(left_height - right_height) > 1:
                return -1
            return max(left_height, right_height) + 1
        return getHeight(root) >= 0
