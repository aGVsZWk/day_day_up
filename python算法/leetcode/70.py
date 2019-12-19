class Solution:
    def climbStairs(self, n: int) -> int:
        knownResults = [0] * (n + 1)
        for i in range(1, n+1):
            if i <= 2:
                knownResults[i] = i
            else:
                knownResults[i] = knownResults[i - 1] + knownResults[i - 2]
        return knownResults[n]
