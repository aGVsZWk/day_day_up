# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxLength = 0
        self.getLength(root)
        return self.maxLength

    def getLength(self, node):
        if not node:
            return 0
        left = self.getLength(node.left)    # 左边最长路径
        right = self.getLength(node.right)  # 右边最长路径
        self.maxLength = max(self.maxLength, left + right)  # 直径
        return max(left, right) + 1     # 以当前节点为定点的最长路径
