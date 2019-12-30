class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [1] + [0] * rowIndex
        for i in range(rowIndex):
            for j in range(rowIndex, 0, -1):
                result[j] = result[j] + result[j-1]
        return result
