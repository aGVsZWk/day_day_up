# 糖果问题
def findContentChildren(g, s):
    # g: 需求因子列表
    # s: 糖果大小列表
    child, candy = 0, 0
    while child < len(g) and candy < len(s):
        if g[child] < s[candy]:
            child += 1
        candy += 1
    return child

if __name__ == '__main__':
    print(findContentChildren([1, 3, 5, 10], [2, 2, 4, 11]))
