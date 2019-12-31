# 进制转换：加取模等取整
# chr：数字转字符 (char)

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = ""
        while n:
            ans += chr((n-1) % 26 + ord("A"))
            n = (n-1) // 26
        return ans[::-1]
