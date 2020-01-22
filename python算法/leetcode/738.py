class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        # 465 --- 459
        # 44123 --- 39999
        # 443 --- 399
        # 445 --- 445
        nums = [i for i in str(N)]
        i = 0
        sign = False
        while i < len(nums) - 1:
            t = i
            while i + 1 < len(nums) - 1 and nums[i] == nums[i+1]:
                i += 1
            if nums[i] > nums[i+1]:
                change = t
                sign = True
                break
            else:
                i += 1
        if not sign:
            return N
        nums[change] = str(int(nums[change]) - 1)
        for i in range(len(nums)):
            if i > change:
                nums[i] = "9"
        return int("".join(nums))


class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        # 465 --- 459
        # 44123 --- 4   40000 - 1
        # 443 --- 399
        # 445 --- 445
        nums = [i for i in str(N)]
        i = 0
        sign = False
        while i < len(nums) - 1:
            t = i
            while i + 1 < len(nums) - 1 and nums[i] == nums[i+1]:
                i += 1
            if nums[i] > nums[i+1]:
                change = t
                sign = True
                break
            else:
                i += 1
        if not sign:
            return N
        for i in range(len(nums)):
            if i > change:
                nums[i] = "0"
        return int("".join(nums)) - 1


# 因为是起始问题，可考虑倒序遍历，如果遇到满足条件位置，则可进行修改，然后让其满足条件继续遍历。
