class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        logsHelp = [(int(i.split(':')[0]), i.split(':')[1], int(i.split(':')[2])) for i in logs]
        result = [0] * n
        stack = []
        for log in logsHelp:
            if log[1] == "start":
                stack.append(log)
            else:
                t = stack.pop()
                time = log[2] - t[2] + 1
                n = t[0]
                result[n] += time
                if stack:
                    result[stack[-1][0]] -= time
        return result
