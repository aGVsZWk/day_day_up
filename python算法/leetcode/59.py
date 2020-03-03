class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = [[0 for __ in range(n)] for _ in range(n)]
        left, top, right, bottom = 0, 0, n-1, n-1
        c = 1
        while c <= n * n:
            # 左到右
            for i in range(left, right+1):
                result[top][i] = c
                c += 1
            top += 1
            # 右到下
            for i in range(top, bottom+1):
                result[i][right] = c
                c += 1
            right -= 1
            # 右到左
            for i in range(right, left-1, -1):
                result[bottom][i] = c
                c += 1
            bottom -= 1
            # 下到上
            for i in range(bottom, top-1, -1):
                result[i][left] = c
                c += 1
            left += 1
        return result
