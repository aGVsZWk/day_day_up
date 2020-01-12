class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        ans = 0
        for i in range(2, n):
            j = 2
            sign = True
            while j <= (i // 2):
                if i % j == 0:
                    sign = False
                    break
                j += 1
            if sign:
                ans += 1
        return ans



class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        cache = [1] * (n+1)
        cache[0] = 0
        cache[1] = 0
        for i in range(2, n // 2 + 1):
            for j in range(i, n // 2 + 1):
                if i * j >= n:
                    break
                else:
                    cache[i * j] = 0
        return sum(cache[:n])
