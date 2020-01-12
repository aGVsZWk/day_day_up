class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s and not t:
            return True
        i = 0

        while i < len(s):
            if s.find(s[i]) != t.find(t[i]):
                return False
            i += 1
        return True
