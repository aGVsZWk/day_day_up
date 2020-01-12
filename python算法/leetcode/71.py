class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        temp = path.split("/")
        for s in temp:
            if s == ".." and stack:
                stack.pop()
            elif s == "." or s == "" or (s == ".." and not stack):
                continue
            else:
                stack.append(s)
        return "/" + "/".join(stack)
            
