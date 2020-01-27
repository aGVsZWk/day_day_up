# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1):
            return 1
        if not isBadVersion(n):
            return n
        low = 1
        high = n
        while low < high:
            mid = (low + high) // 2
            if not isBadVersion(mid) and isBadVersion(mid+1):
                break
            elif isBadVersion(mid):
                high = mid
            else:
                low = mid
        return mid + 1
