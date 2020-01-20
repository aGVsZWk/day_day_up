class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        answer = 0
        buyPrice = float('inf')
        for price in prices:
            if price < buyPrice:
                buyPrice = price
                continue
            if price > buyPrice + fee:
                answer += price - buyPrice - fee
                buyPrice = price - fee
        return answer
