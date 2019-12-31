# 移掉 k 位数字(leetcode 402)
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        for i in range(len(num)):
            # 小于栈顶 --> 弹栈后入栈; 否则直接入栈
            while stack != [] and num[i] < stack[-1] and k > 0:
                stack.pop()
                k -= 1
            if num[i] != "0" or stack != []:    # 注意 "0"，双引号不要丢
                stack.append(num[i])
        # k 还有剩余的情况
        while k > 0 and stack != []:
            stack.pop()
            k -= 1
        ans = ''.join(stack)
        return ans if ans else "0"    # 最后可能会栈空，返回 0
