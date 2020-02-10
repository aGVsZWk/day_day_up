class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # return A.index(max(A))
        left, right = 0, len(A) - 1
        while left <= right:
            mid = (left +right) / 2
            if A[mid - 1] < A[mid] and A[mid] < A[mid + 1]:
                left = mid + 1
            elif A[mid] > A[mid + 1] and A[mid - 1] > A[mid]:
                right = mid - 1
            else:
                return mid
