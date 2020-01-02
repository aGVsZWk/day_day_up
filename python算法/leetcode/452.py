class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) < 2:
            return len(points)
        points = sorted(points, key=lambda x: x[0])
        shot_start = points[0][0]
        shot_end = points[0][1]
        times = 1
        for start, end in points:
            if start > shot_end:
                times += 1
                shot_end = end
            if start > shot_start:
                shot_start = start
            if end < shot_end:
                shot_end = end
        return times
