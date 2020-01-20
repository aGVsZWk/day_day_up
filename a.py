class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        buyPrice = prices[0]
        highPrice = prices[0]
        prices.append(float("-inf"))
        answer = 0
        for i in range(1, len(prices)):
            if prices[i] < buyPrice:
                buyPrice = prices[i]
            elif prices[i] > buyPrice + fee:
                highPrice = prices[i]
            elif prices[i] < highPrice and buyPrice < highPrice:
                answer += max(highPrice - buyPrice - fee, 0)
                buyPrice = prices[i]
                highPrice = prices[i]

        return answer

s = Solution()
a = s.maxProfit([1,3,2,8,4,9])
print(a)
