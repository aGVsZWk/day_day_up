class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        times = len(strs)
        strs.sort(key=len)
        for i in range(len(strs[0])):
            temp = ""
            for j in range(len(strs)):
                temp += strs[j][i]
            if temp != times * strs[0][i]:
                return strs[0][:i]
        return strs[0]


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        answer = ""
        for i in zip(*strs):
            if len(set(i)) != 1:
                break
            answer += i[0]
        return answer
