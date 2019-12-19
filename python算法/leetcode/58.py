class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        i = len(s) - 1
        ret = 0
        while s[i] == " " and i >= 0:
            i -= 1
            continue
        while s[i] != " " and i >= 0:
            ret += 1
            i -= 1
        while s[i] == " " and i >= 0:
            break
        return ret
