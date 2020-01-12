class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        j = len(s)
        ans = 0
        for i in range(0, j):
            ans = ans * 26 + (ord(s[i]) - ord("A")) + 1
        return ans
