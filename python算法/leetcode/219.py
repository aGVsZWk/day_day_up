# 开个 cache 缓存，保留最新
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hashMap = {}
        for i in range(len(nums)):
            if nums[i] not in hashMap or (i - hashMap[nums[i]]) > k:
                hashMap[nums[i]] = i
            else:
                return True
        return False


# 开个 cache+list 符合结构缓存
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        from collections import defaultdict
        cache = defaultdict(list)
        for i in range(len(nums)):
            if cache[nums[i]] and (i - cache[nums[i]][-1]) <= k:
                return True
            else:
                cache[nums[i]].append(i)
        return False
