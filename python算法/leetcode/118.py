class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        elif numRows == 1:
            target = [[1]]
        elif numRows == 2:
            target = [[1], [1, 1]]
        else:
            target = [[1], [1, 1]]
            for i in range(3, numRows+1):
                vals = [1] * i
                for j in range(1, i-1):
                    vals[j] = target[i-2][j-1] + target[i-2][j]
                target.append(vals)
        return target




class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(numRows):
            result.append([])
            for j in range(i+1):
                if j in (0, i):
                    result[i].append(1)
                else:
                    result[i].append(result[i-1][j-1] + result[i-1][j])
        return result
