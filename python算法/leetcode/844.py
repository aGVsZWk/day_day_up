class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        return self.backspace(S) == self.backspace(T)

    def backspace(self, s):
        stack = []
        for i in s:
            if stack and i == "#":
                stack.pop()
            elif not stack and i == "#":
                continue
            else:
                stack.append(i)
        return stack

    def backspace(self, s):
        stack = []
        for i in s:
            if i != "#":
                stack.append(i)
            elif stack:
                stack.pop()
            else:
                continue
        return stack
