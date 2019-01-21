# 一. 类型和运算
# 1 --简单的列出对象obj所包含的方法和名称, 返回一个字符串列表
# print(dir(obj))
# 查询obj.func的具体介绍和方法
# help(obj.func)



# 2--测试类型的三种方法
# L = list()
# if type(L) == type([]):
#     print("L is list")
#
# if type(L) == list:
#     print("L is list")
#
# if isinstance(L, list):
#     print("L is list")



# 3--python数据类型: 哈希类型, 不哈希类型
# 哈希类型, 即在原地不能改变的变量类型, 不可变类型. 函数hash()查看其hash值, 也可以作为字典的key
# "数字类型: int, float, decimal.Decimal, fractions.Fraction, complex"
# import decimal
# a = decimal.Decimal(12.5)  # Decimal常用于金融,货币
# print(a, type(a))
# import fractions
# a = fractions.Fraction(12.5)  # 分数
# print(a, type(a))
# print(complex(1,2.1))
# print(complex("1"))
# print(complex("1+2.1j"))
# "字符串类型: str, bytes"
# "元组: tuple"
# "冻结类型: frozenset"
# "布尔类型: True, False"
# "None"
# 不可hash类型: 原地可变类型, list, dict和set. 它们不可作为字典的key




# 4--数字常量
# 整数: 1234, -1234, 0, 9999999
# 浮点数: 1.23, 1., 3.14e-10(表示3.14乘以10的-10次方), 4E210(表示4乘以10的210次方), 4e+210(表示4乘以10的210次方),
# 八进制, 十六进制, 二进制  0o177, 0x9ff, 0X9FF, 0b101010
# 复数常量, 也可以用complex(real, image)来创建 3+4j, 3.0+4.0j, 3J, 4j
# 将十进制数转化为十六进制, 八进制, 二进制 hex(100), oct(100), bin(100)
# 将字符串转化为整数,base为进制数 int(string, base)
# print(int('100',16))
# 正无穷, 负无穷, 非数, 非数a!=a为True, 0乘以无穷等于nan, 正无穷+负无穷等于nan, Numpy里用列表表示分数分母填0转换过去是inf  float('inf'), float('-inf'), float('nan')
# if 0 > float('-inf'): print(True)
# if 0 < float('inf'): print(True)
# print(0 * float('nan'))
# a = float('nan')
# print(a!=a)
# print(0*float('inf'))
# print(float('inf')+float('-inf'))





# 5--数字的表达式操作符
# yield x                       # 生成器函数发送协议
# lamda args: expression        # 生成匿名函数
# x if y else z                 # 三元表达式
# x and y, x or y, not x        # 逻辑与, 逻辑或, 逻辑非
# x in y, x not in y            # 成员对象测试
# x is y, ix is not y           # 对象实体测试
# x<y, x<=y, x>y, x>=y, x==y, x!=y      # 大小比较, 集合子集或超集值相等性操作符
# a = {1,2,3}
# b = {1,2,3,4}
# print(a <= b)     # 集合子集
# print(1<2<3)      # python中允许连续比较
# x|y, x&y, x^y     # 位或, 位与, 位异或
# a = 0b00000000
# b = 0b11111111
# print(a|b)
# print(a&b)
# print(a^b)
# x<<y, x>>y        # 位操作:x左移/右移y位
# x = 0b00000001
# y = 0b10000000
# print(x<<7==y)
# +, -, *, /, //, %, **     # 加减乘除取整取余幂运算
# -x, +x, ~x        # 一元减法, 识别, 按位求补
# x = 0b10000000
# print(-x)
# print(+x)
# print(~x)
# 取反函数
# foo = lambda x: ~x+1
# print(foo(5))
# x[i], x[i:j:k]    # 索引, 切片
# int(3.14), float(3)   # 强制类型转换

# 6--整数可以利用bit_length函数测试所占的位数
# a = 1
# print(a.bit_length())
# a = 1024
# print(a.bit_length())

# 7--repr和str显示格式的区别
"""
repr格式: 默认的交互模式的回显, 产生的结果看起来它们就像是代码
str格式: 打印语句, 转换成一种对用户更加友好的格式
"""
# a = "hello"
# print(a)
# print(repr(a))




# 8--数字相关的模块
# math模块
# Decimal模块: 小数模块
# from decimal import Decimal,getcontext
# getcontext().prec = 3   # 设置精度, 最大为3
# value = Decimal(1) / Decimal(3)
# print(value)
# Fraction模块: 分数模块
# from fractions import Fraction
# value = Fraction(4,6)
# value2 = Fraction(0.25)
# print(value,value2)






# 9--集合set
"""
set是一个无序不重复元素集, 基本功能包括关系测试和消除重复元素
set支持union(联合),intersection(交),difference(差)和symmetric difference(对称差集)等数学运算
set支持x in set, len(set), for x in set
set不记录元素位置或者插入点, 因此不支持indexing,slicing,或其它类序列的操作
"""
# s = set([3,5,9,10,"h"]) # 传入的是可迭代对象就ok
# print(s)
# t = set("hello")
# print(t)

# a = t | s   # 并集, 等价于t.union(s)
# print(a)
# print(t.union(s))

# b = t & s   # 交集, 等价于t.intersection(s)
# print(b)
# print(t.intersection(s))

# c = t - s   # 求差集, t不在s中的项, 等价于t.difference(s)
# print(c)
# print(t.difference(s))

# d = t ^ s   # 对称差集(项在t或s中, 但不会同时出现在二者中), 等价于t.symmetric_difference(s)
# print(d)
# print(t.symmetric_difference(s))

# t.add('x'), t.remove('x')   # 增加/删除一个item

# s.update([10,37,42])        # 利用[......]更新集合
# print(s)

# x in s, x not in s        # 集合是否存在某个值

# print(s.issubset(t))   # s<=t, 测试是否s中的每一个元素都在t中
# print(s.issuperset(t)) # s>=t, 测试是否t中的每一个元素都在s中
# s.copy()      # 拷贝

# x = 3
# s.discard(x)  # 删除s中的x
# print(s)

# s.clear()       # 清空s

# {x**2 for x in [1,2,3,5]}
# {x for x in 'spam'}




# 10--集合fronzenset, 不可变对象
"""
set是可变对象, 即不存在hash值, 不能作为字典的值. 同样的还有list等(tuple是可以作为字典的key的)
frozenset是不可变对象, 即存在hash值, 可作为字典的键值
frozenset对象没有add, remove等方法, 但有union/intersection/difference/等方法
"""
# a = set([1,2,3])
# b = set()
# b.add(a)  # 报错, set是不可哈希类型
# b.add(frozenset(a)) # ok, 将set变为frozenset, 可哈希
# print(b)




# 11--布尔类型bool
# type(True)
# isinstance(False,int)
# True == 1; True is 1; 输出(True, False)





# 12--动态类型简介
"""
变量名通过引用, 指向对象
python中的"类型"属于对象, 而不是变量, 每个对象都包含有头部信息,比如:"类型标示符","引用计数器等"
"""
# 共享引用及在原处修改: 对于可变对象, 要注意尽量不要共享引用
# 共享引用和相等测试:
# L = [1]
# M = [1]
# print(L is M)   # 返回False
# L = M = [1,2,3]
# print(L is M)   # 返回True, 共享引用

# 增强赋值和共享引用:普通+号会生成新的对象, 而增强赋值+=会在原处修改
# L = M = [1,2]
# L = L + [3,4] # +号进行运算, 运算完成后生成个新对象, L在引用这个对象
# print(L,M)    # L = [1,2,3,4], M = [1,2]

# L += [3,4]      # += 不生成新对象, 直接对原对象操作, 也不会重新进行引用
# print(L,M)      # L =[1,2,3,4], M = [1,2,3,4]



# 13--常见字符串常量和表达式
# S = ''  # 空字符串
# S = "spam's"    # 双引号和单引号相同
# S = "s\np\ta\x00m"  # 转移字符, \x00表示空格
# S = r'\temp'    # Raw字符串, 不会进行转移, 抑制转义
# S = b'Spam'     # python3中的字节字符串
# S = u'spam'     # python2中的Unicode字符串
# s1+s2, s1*3, s[i], s[i:j], len(s) # 字符串操作
# s = 'a %s parrot' %'kind'   # 字符串格式化表达
# s = 'a {1} {0} parrot'.format('kind','red')   #字符串格式化方法
# print(s)
# for x in s:print(x)   # 字符串迭代, 成员关系
# [x*2 for x in s]    # 字符串列表解析
# s = ",".join(['a','b','c'])   # 字符串输出, 结果: a,b,c
# print(s)



# 14--内置str处理函数
str1 = "string object"
str1.upper(), str1.lower(), str1.swapcase(), str1.capitalize(), str1.title()    # 全部大写, 全部小写, 大小写转换, 首字母大写, 每个单词的首字母大写   str是不可变类型, 生成新对象, 需要变量引用它

# str1.ljust(width)   # 获取固定长度, 左对齐, 右边不够用空格补齐
# str1.rjust(width)   # 获取固定长度, 右对齐, 左边不够用空格补齐
# str1.center(width)  # 获取固定长度, 中间对齐, 两边不够用空格补齐
# str1.zfill(width)   # 获取固定长度, 右对齐, 左边不够用0补齐
# print(str1.ljust(30)+'end')
# print(str1.rjust(30))
# print(str1.center(30))
# print(str1.zfill(30))
# str1.find('t',start,end)   # 查找字符串, 可指定起始及结束位置搜索
# str1.rfind('t')   # 从右边开始查找字符串
# 上面所有的方法都可以用index代替, 不同的是使用index查找不到会抛异常, 而find返回-1
# str1.count('t')     # 查找字符串出现的次数
# str1.replace('old','new')   # 替换函数, 替换old为new
# str1.strip()          # 默认首尾删除空白符, 左边和右边都删
# s = "   a hello b   "
# print(s.strip()+'a')
# s = "helllllllllllllllo hello  qweqwqhelllllllll"
# s = "qwertyuiophhhheeeelllll"
# print(s.strip('hel'))     # 删除字符串中开头和结尾指定的字符串, 不删除中间; 最后一个可重复? 对, 重复任意次数
str1.lstrip()   # 去除左边的空格
str1.lstrip('d')    # 删除str1字符串左边的字符串
str1.rstrip()   # 去除右边的空格
str1.rsplit('d')    # 删除str1字符串右边的字符串
str1.startswith("start")    # 是否以start开头
str1.endswith("end")        # 是否以end结尾
str1.isalpha(), str1.isalnum(), str1.isdigit(), str1.islower(), str1.isupper()  # 判断字符串是否全为字母, 字母或数字(不包含下划线), 数字, 小写, 大写
# 数字分为Unicode数字, byte数字, 全角数字, 罗马数字, 汉字数字, 小数
str1.isdigit(), str1.isdecimal(), str1.isnumeric()  # 判断是否全是数字      # 其中, 全角数字全为True, 小数全为False




# 15--三重引号编写多行字符串块, 并且在代码折行出嵌入换行字符\n
# mantra = """
#         hello world
#         hello python
#         hello my friend
# """
# print(repr(mantra))



# 16--索引和切片:
# S[0], S[len(S)-1], S[-1]  # 索引
# S[1:3], S[1:], S[:-1], S[1:10:2]  # 分片, 第三个参数指定步长




# 17--字符串转换工具:
int('42'), str(42)  # 返回42, '42'
float('4.13'), str(4.13)    # 返回4.13, '4.13'
ord('s'), chr(115)      # 返回115, 's'    # ASCII编码
int('1001',2)   # 将字符串作为二进制数编码, 转换为数字, 返回9, 前面必须是字符串格式
bin(13), oct(13), hex(13)   # 将整数转换为二进制, 八进制, 十六进制字符串



# 18--另类字符串连接
# name = "wang" "hong"    # 单行, name = "wanghong"
name = "wang"\
       "hong"   # 多行, name = "wanghong", \的行, 后面不能加东西, 比如注释和空格

# print(name)

# 19--python中的字符串格式化实现   字符串格式化表达式
"""
基于C语言的'print'模型, 并且在大多数的现有的语言中使用
通用结构: %[(name)][flag][width].[precision]typecode
"""
# s = "this is %d %s" % (1,'dead')
# s = "%s----%s----%s" % (42, 3.14, [1,2,3])
# s = "%d...%6d...%-6d...%06d" % (1234, 1234, 1234, 1234)
# f = 1.23456789
# s = "%e | %f | %g" %(f,f,f)     # 浮点数字(科学计数法), 浮点数字(用小数点符号), 浮点数字(根据值自动确定用小数点还是科学计数法)
# s = "%c"%123 # 把ASCII码转换成字符, 然后输出
# s = "%(name1)d---%(name2)s" % {"name1":23, "name2":"value2"}    # 基于字典的格式化表达式
# def foo():
#     name = "zhangsan"
#     age = 18
#     print(vars())   # vars()函数返回一个字典, 包含了所有本函数调用时存在的变量(包括形参)
#     s = "%(name)s is %(age)d" % vars()
#     print(s)
# foo()



# 20--python中的字符串格式化实现     字符串格式化调用方法
# 普通调用
"{0},{1} and {2}".format('spam','ham','eggs')   # 基于位置的调用
"{motto} and {pork}".format(motto="spam",pork="ham")    # 基于key的调用
"{motto} and {0}".format('ham',motto="spam")    # 混合调用
# 添加键  属性  偏移量(import sys)
# import sys
# s = "my {1[spam]} runs {0.platform}".format(sys,{"spam":"laptop"})    # 基于key的键和属性
# print(s)
# print(sys.platform) # 系统类型

# s = "first = {0[0]}, second = {0[1]}".format(['A','B','C'])
# print(s)
# 具体格式化
# s = "{0:e}, {1:.3e}, {2:g}".format(3.14159, 3.14159, 3.14159)   # 输出'3.141590e+00, 3.142e+00, 3.14159'
# print(s)

# "fieldname:format_spec".format(......)
# 说明
"""
    fieldname是指定参数的一个数字或关键字, 后面可跟可选的".name"或"[index]"成分引用
    fill        ::=  <any character>              #填充字符
    align       ::=  "<" | ">" | "=" | "^"        #对齐方式
    sign        ::=  "+" | "-" | " "              #符号说明
    width       ::=  integer                      #字符串宽度
    precision   ::=  integer                      #浮点数精度
    type        ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
"""
# 例子
# s = "={0:10}={1:10}".format("spam","123.456")   # 指定长度
# s = "={0:>10}=".format('test')                  # 右对齐
# s = "={0:<10}=".format('test')                  # 左对齐
# s = "={0:^10}=".format('test')                  # 居中对齐
# s = "{0:x},{1:o},{2:b}".format(255, 255, 255)   # 十六进制, 八进制, 二进制
# s = "My name is {0:{1}}.".format("Luke",8)      # 动态指定长度
# print(s)




# 21--常用列表常量和操作
# L = [[1,2], 'string', {}]   # 嵌套列表
# L = list('spam')        # 列表初始化
# L = list(range(0, 4))   # 列表初始化   # 只要是可迭代的, 都可以用list初始化吧
# L = list({"A":90,"B":80,"C":70}.items())
# print(L)
# L = list(map(ord,'spam'))   # 列表解析
# len(L)  # 求列表长度
# L.count(value)  # 求列表中某个值的个数
# L.append(obj)   # 向列表尾部添加数据
# L.insert(index, obj)  # 向列表的指定index位置添加数据,index及其之后的数据右移
# L.extend(interable)   # 通过添加interable中的元素来扩展列表
# L = [1,2,3].extend("hello")
# L.index(value, [start, [stop]])   # 返回列表中value值的第一个索引
# L.pop(index)    # 删除并返回index处的元素, 默认为删除并返回最后一个元素
# L.remove(value)   # 删除列表中的value值, 只删除第一次出现的value的值
# L.reverse()     # 翻转列表
# L.sort(cmp=None,key=None,reverse=False)   # 排序列表
# a = [1, 2, 3],
# b = a[10:]    # 注意, 这里不会引发IndexError异常, 只会返回一个空的列表[]
a = []
a += [1]    # 在原有列表的基础上进行操作, 即列表的id没有改变
# a = []
# a = a + [1]     # 构建了一个新的列表, a引用新的列表, 列表id发生了改变




# 22--用切片来删除序列的某一段
a = [1,2,3,4,5,6,7]
a[1:4] = []
a = [0,1,2,3,4,5,6,7]
del a [::2]     # 去除偶数项(偶数索引的)


# 23--常用字典常量和操作
# D = {}
# D = {"spam":2, "tol":{"ham":1}} # 嵌套字典
# D = dict.fromkeys(['s','d'],[8,9])  # {"s":8, "d":"9"}
# D = dict.fromkeys(['s','d'],8)  # {"s":8, "d":"8"}
# D = dict(name="tom", age="12")
# D.keys(), D.values(), D.items()   # 字典键, 值, 以及键值对
# D.get(key, default) # get函数通过键去获取键值, 如果获取不到返回default
# D = {"a":90, "b":80, "c":70}
# D_other = {"a":90, "b":80, "c":60}
# D.update(D_other)   # 合并字典, 如果存在相同的键值, D_other会覆盖掉数据
# D.pop("key",ret)    # 删除字典中键值为key的项, 并返回其键值, 如果不存在此键, 返回ret
# D.popitem()     # pop字典中随机的一项
# ret = D.setdefault("d",60)  # 如果键d存在, 返回60; 如果键d不存在, 设置键d的值为60, 并返回60
# del D # 删除字典
# del D['key']    # 删除字典的某一项
# if key in D: if key not in D:     # 测试字典键是否存在
# 字典注意事项: 1. 对新索引会添加一项 2. 字典键不一定非得是字符串, 也可以为任何的不可变对象
# 不可变对象: 调用对象自身的任意方法, 也不会改变该对象自身的内容,这些方法会创建新的对象并返回
# D[(1,2,3)] = 2  # tuple作为字典的key




# 24--字典解析
# D = {k:8 for k in ['s','d']}
# D = {k:v for (k,v) in zip(['name',"age"], ["tom",12])}




# 25--字典的特殊方法__missing__: 当查找不到该key时, 会执行该方法
# class dict(dict):
#     def __missing__(self, key):
#         return "hahaha"

# d = dict()
# print(d["foo"])



# 26--元组和列表的唯一区别在于元组是不可变对象, 列表是可变对象
# a = [1,2,3]     # a[1] = 0, OK
# a = (1,2,3)     # a[1] = 0, Error
# a = ([1,2],)    # a[0][1] = 0, OK  # 没有逗号, 元组只有一个元素, 不能索引
# a = [(1,2)]     # a[0][1] = 0, Error



# 27--元组的特殊用法: 逗号和圆括号
# D = (12)    # 此时D为一个整数, 即D = 12
# D = (12,)   # 此时D为一个元组, 即D = (12,)  len(D)仍然为1




# 28--文件的基本操作
# fw = open(r'C:\Luke\spam.html',"w")
# fw.write("hello\nworld\nhahahaha")
# fw.close()
# fr = open(r'C:\Luke\spam.html',"r")
# print(fr.read())
# fr.close()


# output = open(r'C:\Luke\spam.html',"w")   # 打开输出文件, 用于写,
# output.write("hello\nqweqwe")
# input = open('C:\Luke\spam.html','r')     # 打开输入文件, 用于读
# 写文件不存在的话默认新建, 读文件不存在的话会报错. 打开的方式可以为 "r", "w", "a", "rb", "wb", "ab"等
# fp = open('C:\Luke\spam.html','r')
# fp.read(size)     # size为读取的长度, 以byte为单位, 一个字符占用一个byte, r和rb都是这样
# fr.readline(size)   # 读取第一行前size个字符
# fr.readlines(size)      # 把文件的每一行作为list的一个元素, 返回这个list. 它的内部是通过循环调用readline()来实现的, 如果提供size参数, size是表示读取内容的总长
# fr.readable()   # 是否可读
# fw.write(str)   # 把str写到文件中, write()并不会在str后面加上一个换行符
# fw.writelines(seq)    # 把sql的内容全部写到文件中(多行一次性写入)
# fw.writable()   # 是否可写, 注意:没有e
# fr.close()      # 关闭文件
# fw.flush()      # 把缓冲区的内容写入硬盘
# fw.fileno()     # 返回一个长整型的"文件标签", 一个数字
# s = fr.isatty() # 文件是否是一个终端设备文件(unix系统中的)
# fr.tell()   # 返回文件操作标记的当前位置, 以文件的开头为原点
# 文件操作标记, 光标位置, 之能用于读, 不能用于写, 也不能追加
# fr.next()   # 返回下一行, 并将文件操作标记位移到下一行. 把file用于 for .. in file这样的语句时, 就是调用next()函数来实现遍历的
# fr.seek(offset, whence)   # 将文件打开操作标记移到offset位置, whence为0表示从头开始计算, 1表示以当前位置为原点计算, 2表示以文件末尾为原点进行计算
# fr.seek(0,0)
# fr.seekable()       # 是否可以seek
# fr.truncate(size)   # 将文件裁成规定的大小, 默认是裁到当前文件操作标记的位置

# for line in open('data'):     # 使用for语句, 比较适用于打开比较大的文件
#     print(line)

# with open('data') as file:
#     print(file.readline())      # 使用with语句, 可以保证文件关闭

# with open('data') as f:
#     lines = f.readlines()       # 一次性读入文件所有行, 并关闭文件

# open('f.txt', encoding="latin-1")   # python3.x Unicode文本文件
# open('f.bin','rb')      # python3.x 二进制bytes文件





# 29--其它
# python中的真假值含义: 1. 数字如果非零, 则为真; 0为假.   2. 其它对象如果非空, 则为真
# 通常意义下的类型分类: 1.数字, 序列, 映射    2. 可变类型和不可变类型
# id()和hash()