# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        from collections import defaultdict
        self.cache = defaultdict(int)
        self.travalNode(root)
        times = max(self.cache.values())
        answer = []
        for key, val in self.cache.items():
            if val == times:
                answer.append(key)
        return answer

    def travalNode(self, root):
        if not root:
            return
        self.cache[root.val] += 1
        self.travalNode(root.left)
        self.travalNode(root.right)
