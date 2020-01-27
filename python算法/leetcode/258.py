# 直接对 9 取余，就是结果
# X = 100*a + 10*b + c = 99*a + 9*b + (a+b+c)；所以对9取余即可。
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        return (num - 1) % 9 + 1 if num else num
