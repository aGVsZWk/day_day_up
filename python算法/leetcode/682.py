class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        ans = 0
        stack = []
        for i in ops:
            if i.isdigit() or i.startswith("-"):
                ans += int(i)
                stack.append(int(i))
            elif i == "C":
                ans -= stack[-1]
                stack.pop()
            elif i == "D":
                t = stack[-1] * 2
                ans += t
                stack.append(t)
            elif i == "+":
                t = stack[-1] + stack[-2]
                ans += t
                stack.append(t)
        return ans

class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        for i in ops:
            if i.isdigit() or i.startswith("-"):
                stack.append(int(i))
            elif i == "C":
                stack.pop()
            elif i == "D":
                t = stack[-1] * 2
                stack.append(t)
            elif i == "+":
                t = stack[-1] + stack[-2]
                stack.append(t)
        return sum(stack)
