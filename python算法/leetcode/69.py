# 暴破
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        elif x <= 3:
            return 1
        else:
            for i in range(2, x):
                if i ** 2 > x:
                    return i - 1

# 二分查找
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        low = 1
        high = x
        i = (low + high) // 2
        while True:
            if i ** 2 <= x and (i + 1) ** 2 > x:
                return i
            elif i ** 2 > x:
                t = i
                i = (low + i) // 2
                high = t
            elif i ** 2 < x:
                t = i
                i = (high + i) // 2
                low = t

# 二分
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        low = 1
        high = x
        while True:
            i = (low + high) // 2
            if i ** 2 > x:
                high = i
            elif (i+1) ** 2 <= x:
                low = i
            elif i ** 2 <= x and (i+1) ** 2 > x:
                return i
