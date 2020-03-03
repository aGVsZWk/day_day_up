class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        zero_row, zero_col = False, False

        # 将首行和首列置为0，并标记最初首行和首列是否出现0元素
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_row = True if i == 0 else zero_row
                    zero_col = True if j == 0 else zero_col
                    matrix[i][0] = matrix[0][j] = 0
        # 将对应行置为0
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        # 将对应列置为0
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        # 首行置0
        if zero_row:
            for j in range(n):
                matrix[0][j] = 0
        # 首列置0
        if zero_col:
            for i in range(m):
                matrix[i][0] = 0
