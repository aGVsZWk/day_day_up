class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 3:
            return True
        dp = [None] * (n+1)
        dp[0], dp[1], dp[2], dp[3] = None, True, True, True
        for i in range(4, n+1):
            dp[i] = not((dp[i-1] and dp[i-2] and dp[i-3]))
        return dp[i]


if __name__ == '__main__':
    s = Solution()
    s.canWinNim(6)
