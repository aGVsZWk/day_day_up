class Solution:
    def addBinary(self, a: str, b: str) -> str:
        la = len(a)
        lb = len(b)
        sign = 0
        ret = ""
        for i in range(max(len(a), len(b))):
            t = (int(a[la - i - 1]) if i < len(a) else 0) + (int(b[lb - i - 1]) if i < len(b) else 0) + sign
            if t >= 2:
                t -= 2
                sign = 1
            else:
                sign = 0
            ret += str(t)
        if sign:
            ret += "1"
        return ret[::-1]
