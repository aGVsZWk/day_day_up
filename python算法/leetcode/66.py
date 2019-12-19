# 优化前
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ret = []
        sign = 0
        for i in range(len(digits)-1, -1, -1):
            if i == len(digits)-1:
                t = digits[i] + 1
            else:
                t = digits[i] + sign
            if t == 10:
                t = 0
                sign = 1
            else:
                sign = 0
            ret.insert(0, t)
        if sign != 0:
            ret.insert(0, sign)
        return ret

# 优化后
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        acc = 1
        for i in range(len(digits)-1, -1, -1):
            t = digits[i] + acc
            if t == 10:
                acc = 1
                digits[i] = 0
            else:
                digits[i] = t
                acc = 0
                return digits
        if acc:
            digits.insert(0, 1)
            return digits
