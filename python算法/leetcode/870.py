class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        result = []
        for numB in B:
            l = [numA for numA in A if numA > numB]
            if not l:
                t = min(A)
            else:
                t = min(l)
            A.remove(t)
            result.append(t)
        return result

# 上面办法超时！！！
