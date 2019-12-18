class Solution:
    def isValid(self, s: str) -> bool:
        known = {")":"(", "}":"{", "]":"["}
        stack = []
        for i in s:
            if i in known.values():
                stack.append(i)
            else:
                if stack:
                    t = stack.pop()
                    if t != known[i]:
                        return False
                else:
                    return False
        return False if stack else True
