class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        child, cake = 0, 0
        while child < len(g) and cake < len(s):
            if g[child] <= s[cake]:
                child += 1
            cake += 1
        return child
