# 整数反转
def reverse(x):
    ret = 0
    while x:
        ret = ret * 10 + x % 10
        x = x // 10
    return ret


if __name__ == '__main__':
    print(reverse(12321))
