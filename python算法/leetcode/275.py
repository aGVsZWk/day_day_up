# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        self.result = []
        self.binaryPath(root, "")
        return self.result

    def binaryPath(self, root, path):
        if not root.left and not root.right:
            path += str(root.val)
            self.result.append(path)
        if root.left:
            path1 = path + str(root.val) + str("->")
            self.binaryPath(root.left, path1)
        if root.right:
            path2 = path + str(root.val) + str("->")
            self.binaryPath(root.right, path2)
