class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        t = x
        ret = 0
        while t:
            ret = ret * 10 + t % 10
            t = t // 10
        if x == ret:
            return True
        else:
            return False
