# 二. 语法和语句

# 1--赋值语句的形式
# spam = 'spam'               # 基本形式
# spam, ham = 'spam', 'ham'   # 元组赋值形式
# [spam, ham] = ['s', 'h']    # 列表赋值形式
# a, b, c, d = 'abcd'    # 序列赋值形式
# a, *b, c = "abcd"   # 序列解包形式(Python3.x中才有), b是一个列表:['b', 'c']
# spam = ham = 'no'   # 多目标赋值运算, 涉及到共享引用
# spam += 42      # 增强赋值, 涉及到共享引用





# 2--序列赋值, 序列解包
# [a, b, c] = (1, 2, 3)
# a, b, c, d = "spam"
# a, b, c = range(3)
# a, *b = [1, 2, 3, 4]
# *a, b = [1, 2, 3, 4]
# a, *b, c = [1, 2, 3, 4]
# 带有*时, 会优先匹配*之外的变量, 如:
# a, *b, c = [1, 2]   # a = 1, c = 2




# 3--print函数原型
# print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
# 流的重定向
# print('hello world')
# import sys
# temp = sys.stdout    # 原有流的保存
# sys.stdout = open('log.log', 'a')   # 流的重定向, 以后再print就不输出显示了, 而是输出到log.log文件中
# print('hello world')    # 写入到文件log.log
# sys.stdout.close()  # 关闭
# sys.stdout = temp       # 原有流的复原
# print("hello world")




# 4--python中and或or总是返回对象(左边的对象或右边的对象)且具有短路求值的特性
# 1 or 2 or 3     # 返回1
# 1 and 2 and 3   # 返回3



# 5--if/else三元表达符(if语句在行内)
# X = False
# Y = True
# A = 1 if X else 2
# A = 1 if X else (2 if Y else 3)
# 也可以使用and-or语句(一条语句实现多个if-else)
# a = 6
# result = (a > 20 and "big than 20" or a > 10 and "big than 10" or a > 5 and "big than 5")   # 有意思
# print(result)





# 6--python的while语句或者for语句可以带else语句, 当然也可以带continue/break/pass 语句
# a = 0
# while a < 100:
#     print("a<100", a)
#     a += 1
# else:
#     print("a>=100",a)
# else语句会在循环结束后执行，除非在循环中执行了break，同样的还有for语句
# for i in range(5):
#     print(i)
    # if i == 3:
    #     break
# else:
#     print("for结束")






# 7--for循环的元组赋值
# for (a,b) in [(1, 2),(3, 4)]: # 最简单的赋值
# for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]:    # 自动解包赋值
# for ((a, b), c) in [((1, 2,), 3), ('XY', 6)]:     # 自动解包 a = X, b = Y, c = 6
# for (a, *b) in [(1, 2, 3), (4, 5, 6)]:      # 自动解包赋值, b为列表





# 8--列表解析语法
# M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# res = [sum(row) for row in M]
# res = [c * 2 for c in 'spam']
# res = [a * b for a in [1, 2] for b in [4, 5]] # 多解析过程,返回[4, 5, 8, 10]
# res = [a for a in [1, 2, 3] if a < 2]   # 带判断条件的解析过程
# res = [a if a > 0 else 0 for a in [-1, 0, 1]]   # 带判断条件的高级解析过程
# 两个列表同时解析: 使用zip函数
# for teama, teamb in zip(["Packers", "49ers"],["Ravens", "Patriots"]):
#     print(teama + " vs. " + teamb)
# 带所有的列表解析: 使用enumerate函数
# for index, team in enumerate(["Packers", "49ers", "Ravens", "Patriots"]):
#     print(index, team)






# 9--生成器表达式
M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
G = (sum(row) for row in M) # 使用小括号可以创建所需结果的生成器generator object     # 生成器可迭代
# print(type(G))
# for i in G:
#     print(i)
# next(G), next(G), next(G)
G = {sum(row) for row in M}     # 解析语法还可以生成集合和字典
G = {i:sum(M[i]) for i in range(3)}





# 10--文档字符串: 出现在Module的开端以及其中函数或类的开端, 使用三重引号字符串

"""
module document
"""

def func():
    """
    function document
    """
    print()
class Employee(object):
    """
    class docuemnt
    """
    print()
# print(func.__doc__)     # 输出函数文档字符串
# print(Employee.__doc__) # 输出类文档的字符串




# 11--命名惯例
"""
以单一下划线开头的变量名(_X)不会被from module import * 等语句导入
前后有两个下划线的变量名(__X__)是系统定义的变量名, 对解释器有特殊意义
以两个下划线开头但不以下划线结尾的变量名(__X)是类的本地(私有)变量
"""



# 12--列表解析 in 成员关系测试 map sorted zip enumerate内置函数等都使用了迭代协议
# 'first line\n' in open("test.txt")    # in测试, 返回True 或 False
# 可直接对文件进行遍历, 得到每一行的内容
# l = list(map(str.upper, open('test.txt')))  #map(func, iterable_obj)   # 对可迭代对象按func函数规则进行映射,返回个可迭代的map对象
# sorted(iter([2, 5, 8, 3, 1]))   # iter(iterable_obj, sentinel)  # sorted()返回排好序的对象    # 如果对iter有不理解的, 去看我的博文python中的迭代




# 13--del语句: 手动删除某个变量
# del X




# 14--获取列表的字表的方法:
x = [1, 2, 3, 4, 5, 6]
# x[:3]     # 前3个[1, 2, 3]
# x[1:5]    # 中间4个[2, 3, 4, 5]
# x[-3:]    # 最后三个[4, 5, 6]
# x[::2]    # 奇数项[1, 3, 5]
# x[1::2]   # 偶数项[2, 4, 6]



# 15--手动迭代:iter和next
L = [1, 2, 3]
I = iter(L)     # I为L的迭代器
print(next(I))      # 返回1
print(I.__next__()) # 返回2
print(next(I))      # 返回3   next(Iterator)和Iterator.__next__()等效



# 16--python中的可迭代对象
"""
1. range迭代器
2. map, zip 和filter迭代器
3. 字典视图迭代器: D.keys(), D.items()等
4. 文件类型
5. 生成器 
"""