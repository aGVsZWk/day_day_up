class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        low, high = 1, n
        while low <= high:
            mid = (low + high) / 2
            coinsLow = (1 + mid) * mid / 2
            coinsHigh = (1 + mid + 1) * (mid + 1) / 2
            if coinsLow < n and coinsHigh > n or coinsLow == n:
                return mid
            elif coinsHigh <= n:
                low = mid + 1
            elif coinsLow > n:
                high = mid - 1
