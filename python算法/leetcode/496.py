class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return
        stack = []
        hashMap = {}
        result = []
        for num in nums2:
            if not stack:
                stack.append(num)
                continue
            while stack and num > stack[-1]:
                hashMap[stack.pop()] = num
            stack.append(num)

        for num in nums1:
            if num in hashMap:
                result.append(hashMap[num])
            else:
                result.append(-1)

        return result


class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return
        stack = []
        hashMap = {}
        result = []
        for num in nums2:
            while stack and num > stack[-1]:
                hashMap[stack.pop()] = num
            stack.append(num)

        return [hashMap.get(i, -1) for i in nums1]
