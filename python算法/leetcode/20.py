# class Solution:
#     def isValid(self, s: str) -> bool:
#         known = {")":"(", "}":"{", "]":"["}
#         stack = []
#         for i in s:
#             if i in known.values():
#                 stack.append(i)
#             else:
#                 if stack:
#                     t = stack.pop()
#                     if t != known[i]:
#                         return False
#                 else:
#                     return False
#         return False if stack else True




class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {"(":")", "[":"]", "{": "}"}
        stack = []
        for item in s:
            if item in d:
                key = item
                stack.append(key)
            else:
                value = item
                key = stack.pop() if stack else None
                if not key:
                    return False
                if value != d[key]:
                    return False
        return True if not stack else False



if __name__ == '__main__':
    s = Solution()
    t = s.isValid("()[]{}")
    print(t)
