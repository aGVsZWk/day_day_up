# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []
        level = [root]
        t = 0
        while level:
            j = 0
            temp = []
            nextLevel = []
            while j < len(level):
                temp.append(level[j].val)
                if level[j].right:
                    nextLevel.append(level[j].right)
                if level[j].left:
                    nextLevel.append(level[j].left)
                j += 1
            if t % 2 == 1:
                result.append(temp)
            else:
                result.append(reversed(temp))
            t += 1
            level = nextLevel
        return result
