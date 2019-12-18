class Solution:
    def romanToInt(self, s: str) -> int:
        romanInt = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        ret = 0
        for i in range(len(s)-1):
            if romanInt[s[i]] < romanInt[s[i+1]]:
                ret -= romanInt[s[i]]
            else:
                ret += romanInt[s[i]]
        ret += romanInt[s[-1]]
        return ret
