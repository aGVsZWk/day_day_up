# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #    3
        #   /
        #  2

        #          5
        #         / \
        #        3   100
        #       /   /   \
        #      1   99   101
        #         /
        #        98
        if root is None:
            return 0
        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1

        # 二叉树考虑顺序: 1. 两边都没有  2. 两边都有   3. 只有一边有
        # 写法：
        # # 1.
        # if node.left is None and node.right is None:
        #     pass
        # if node.left is not None pr node.right is not None or node.left.val != node.right.val:
        #     pass
        # else:
        #     pass
        # # 2.
        # if node.left and node.right:
        #     pass
        # if node.left is None and node.right is None:
        #     pass
        # else:
        #     pass
