class Solution:
    def countAndSay(self, n: int) -> str:
        known = [None] * (n + 1)
        for i in range(1, n+1):
            if i == 1:
                known[i] = "1"
                continue
            else:
                last_str = known[i-1]
                print(known)
                times = 1
                char = last_str[0]
                known[i] = ""
                for j in range(1, len(last_str)):
                    if last_str[j] == char:
                        times += 1
                    else:
                        known[i] += str(times) + str(char)
                        char = last_str[j]
                        times = 1
                known[i] += str(times) + str(char)
        return known[n]

if __name__ == '__main__':
    s = Solution()
    s.countAndSay(5)
