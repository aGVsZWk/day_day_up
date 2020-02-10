# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        self.answer = []
        if not root:
            return []
        level, nextLevel = [root], []
        while level:
            tmp = []
            for node in level:
                tmp.append(node)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            self.answer.append(sum([t.val for t in tmp]) / float(len(tmp)))
            level = nextLevel
            nextLevel = []
        return self.answer
