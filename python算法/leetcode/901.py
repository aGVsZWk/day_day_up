class StockSpanner(object):

    def __init__(self):
        self.prices = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        self.prices.append(price)

        j = len(self.prices) - 1
        while j >= 0 and self.prices[j] <= price:
            j -= 1
        return len(self.prices) - j - 1



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
