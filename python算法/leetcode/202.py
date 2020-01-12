class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        self.helper = []
        return self.cal(n)

    def cal(self, n):
        if n == 1:
            return True
        ans = 0
        for i in str(n):
            ans += int(i) ** 2
        if ans not in self.helper:
            self.helper.append(ans)
            return self.cal(ans)
        else:
            return False
        
