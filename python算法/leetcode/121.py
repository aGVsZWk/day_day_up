class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        min_price = prices[0]
        profit = 0
        for i in range(len(prices)):
            profit = max(profit, prices[i] - min_price)
            min_price = min(min_price, prices[i])

        return profit


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        min_price = float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        return profit
