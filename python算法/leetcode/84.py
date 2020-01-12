class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        sorted_heights = sorted(set(heights))
        area = 0
        for step in sorted_heights:
            l = []
            for h in heights:
                if h >= step:
                    l.append(h)
                else:
                    area = max(step * len(l), area)
                    l = []
            area = max(step * len(l), area)
        return area
