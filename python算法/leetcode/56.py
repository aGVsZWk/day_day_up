class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        start, end = intervals[0][0], intervals[0][1]
        result = []
        for item in intervals:
            if item[0] <= end:
                end = max(end, item[1])
            else:
                result.append([start, end])
                start = item[0]
                end = item[1]
        result.append([start, end])
        return result
