class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        numStack = []
        strStack = []
        tail = ""
        num = 0
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "[":
                numStack.append(num)
                strStack.append(tail)
                tail = ""
                num = 0
            elif c == "]":
                tmp = strStack.pop()
                repeatTimes = numStack.pop()
                tmp += tail * repeatTimes
                tail = tmp
            else:
                tail += c
        return tail
