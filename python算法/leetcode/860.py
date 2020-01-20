class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        bill5 = 0
        bill10 = 0
        for bill in bills:
            if bill == 5:
                bill5 += 1
            elif bill == 10 and bill5 > 0:
                bill5 -= 1
                bill10 += 1
            elif bill == 20 and bill5 > 0 and bill10 > 0:
                bill10 -= 1
                bill5 -= 1
            elif bill == 20 and bill5 >=3:
                bill5 -= 3
            else:
                return False
        return True
