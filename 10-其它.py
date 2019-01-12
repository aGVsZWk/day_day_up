# 十. 其它
# 1--python实现其任意深度的赋值 例如a[0] = 'value1'; a[1][2] = 'value2'; a[3][4][5] = 'value3'
class MyDict(dict):
    def __setitem__(self, key, value):      # 该函数不走任何改动, 这里只是为了输出
        print('setitem:', key, value, self)
        super().__setitem__(key, value)

    def __getitem__(self, item):    # 主要技巧在该函数
        print('getitem:', item, self)   # 输出信息
        # 基本思路: a[1][2]赋值时, 需要先取出a[1], 然后给a[1]的[2]赋值
        if item not in self:    # 如果a[1]不存在, 则需要新建一个dict, 并使得a[1] = dict
            temp = MyDict()     # 新建的dict: temp
            super().__setitem__(item, temp) # 赋值a[1] = temp
            return temp
        return super().__getitem__(item)     # 如果a[1]存在 则直接返回a[1]


#
# test = MyDict()
# test[0] = 'test'
# print(test[0])
# test[1][2] = "test1"
# print(test[1][2])
# test[1][3] = 'test2'
# print(test[1][3])
# print(test)


# 2--python中的多维数组
lists = [0] * 3     # 扩展list, 结果为[0, 0, 0]
lists = [[]] * 3    # 多为数组, 结果为 [[], [], []]
lists[0].append(3)  # 期望看到的结果[[3], [], []]，实际结果[[3], [3], [3]]，原因：list*n操作，是浅拷贝，如何避免？往下看
lists = [[] for i in range(3)]
lists[0].append(3)      # 结果为[[3], [], []]
lists[1].append(6)      # 结果为[[3], [6], []]
lists[2].append(9)      # 结果为[[3], [6], [9]]
lists = [[[] for j in range(4)] for i in range(3)]  # 3行4列, 且每一个元素为[]



