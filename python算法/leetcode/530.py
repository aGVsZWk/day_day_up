# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.values = []
        self.inOrderTravel(root)
        self.answer = float('inf')
        for i in range(len(self.values)-1):
            self.answer = min(self.answer, abs(self.values[i] - self.values[i+1]))
        return self.answer

    def inOrderTravel(self, root):
        if not root:
            return
        if root.left:
            self.inOrderTravel(root.left)
        self.values.append(root.val)
        if root.right:
            self.inOrderTravel(root.right)
