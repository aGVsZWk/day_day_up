class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        knownNums = {}
        start = -1
        maxLength = 0
        for i in range(len(s)):
            if s[i] in knownNums and knownNums[s[i]] > start:
                start = knownNums[s[i]]
            else:
                length = i - start
                if length > maxLength:
                    maxLength = length
            knownNums[s[i]] = i
        return maxLength
