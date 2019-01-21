# 四. 函数例子

# 1--数学运算类
# abs(x)      # 求绝对值, 参数可以是整型, 也可以是复数
# complex([real[, imag]])   # 创建一个复数
# divmod(a,b)     # 计算a/b, 返回个元组, 元素1是商, 元素2是余数
# float([x]) # 将一个字符串或数转换为浮点数, 如果没参数将返回0.0
# int(x[, base])  # 将一个字符串或浮点数转换为int类型, base表示进制
# long([x[, base]]) # 将一个字符串或浮点数转换为long类型   # python2中使用
# pow(x, y)   返回x的y次幂
# range([start], stop[, step])
# round(x[, n])   # 四舍五入, n为保留的小数位数, 默认为0
# sum(iterable[, start])    对集合求和
# oct(x)  # 将一个数字转换为8进制字符串
# hex(x)  # 将一个数字转换为16进制字符串
# chr(i)  # 返回给定int类型对应的ASCII字符
# unichr(i)   # 返回给定int类型鹅unicode
# ord(c)  # 返回ASCII字符对应的整数
# bin(x)      # 将整数x转换为二进制字符串
# bool(x)     # 将x转换为Boolean类型



# 2--集合类操作
# basestring()    # str和unicode的超类, 不能直接调用, 可以用作isinstance判断    # python2中使用
# format(value, [, format_spec])    # 格式化输出字符
# enumerate(sequence[, start=0])  # 返回一个可枚举的镀锡, 注意它有第二个参数, 为枚举的起始值
# iter(obj[, sentinel])   # 返回一个对象的迭代器, 第二个参数表示分隔符
# max(iterable[, args...][key])   # 返回集合中的最大值
# min(iterable[, args...][key])   # 返回集合中的最小值
# dict([arg]) # 创建数据字典
# list(iterable)  # 将一个集合类型转换为另外一个集合类
# set()   # set对象实例化
# frozenset([iterable])     # 产生一个不可变的set
# tuple([iterable])    # 生成一个tuple类型
# str(object)       # 转换为string类型
# sorted(iterable[, cpm[, key[, reverse]]])   # 集合排序
L = [('b',2),('a',1),('c',3),('d',4)]
# sorted(L, key=lambda x: x[1],reverse=True)
sorted(L, key=lambda x: (x[0], x[1]))   # 使用key参数进行多条件排序, 即如果x[0]相同, 则比较x[1]




# 3--逻辑判断
# all(iterable)     # 集合中的元素都为真的时候, 特别的, 若为空串则返回True
# any(iterable)     # 集合中的元素有一个为真的时候, 特别的, 若为空串返回False
# cmp(x, y)   # 如果x<y, 返回负数; x==y, 返回0; x>y, 返回正数   # 只能在python2中使用




# 4--IO操作
# file(filename[, mode [, bufsize]])   # file类型的构造函数    只能在python2中使用
# raw_input([prompt])   # 设置输入, 输入都是作为字符串处理     只能在python2中使用
# open(name[, mode[, buffering]])   # 打开文件



# 5--其它
# callable(object)  # 检查对象object是否可调用
# classmethod(func) # 用来说明这个func是个类方法.  类方法: 用类名.func()直接调用, 而不需要用实例
# staticmethod(func)  # 用来说明这个func为静态方法.   静态方法: 不会改变类和实例状态的方法, 即不用self和cls
# dir(object) # 不带参数时, 返回当前范围内的变量, 方法和定义的类型列表; 带参数时, 返回参数的属性, 方法列表
# print(dir())
# print(dir(int))
# help(obj)   # 返回obj的帮助信息
# eval(expression)    # 计算表达式expression的值, 并返回
# print(eval('1+2'))
# exec('print(dir())')
# evalfile(filename)  # 用法类似exec(), 不同的是execfile的参数filename为文件名. 而exec的参数为字符串.    只能在python2中使用
# filter(function, iterable)    # 构造一个序列, 等价于[item for item in iterable if function(item)]
# list(filter(bool,range(-3,4)))  # 没有0
# hasattr(object, name)       # 判断对象是否包含名为name的特性
def test(): pass
test.a = 250
# print(hasattr(test, 'a'))
# getattr(object, name[, default])  # 获取一个类的属性
# print(getattr(test, 'a'))
# print(getattr(test,'b', 23123))
# delattr(object, name)   # 删除object对象名为name的属性
# delattr(test, 'a')
# print(getattr(test, 'a'))
# globals()     # 返回一个描述当前全局符号表的字典
# hash(object)    # 如果对象object为哈希表类型, 返回对象object的哈希值
# id(object)      # 返回对象的唯一标识, 一串数字
# isinstance(object, classinfo)     # 判断object是否是class的实例
# isinstance(1,int)
# isinstance(1.1,(int,float))   # isinstance的第二个参数接受一个元组类型
# issubclass(class, classinfo)    # 判断class是否是classinfo的子类
# locals()    # 返回当前的变量列表
# print(locals())
# map(function, iterable, ...)    # 遍历每个元素, 执行funcition操作
# list(map(abs, range(-3,4)))   # map里的func可接受多个形参, 此时需要传入多个列表
# def func(a,b,c):return a + b + c
# print([i for i in map(func, [1,2,3,4], [4,5,6,7], [10,11,12,13])])
# next(iterator[, default])   # 类似于iterator.next()
# property([fget[, fset[, fdel[, doc]]]])   # 属性访问的包装类, 设置后可以通过c.x=value等来访问setter和getter
# reduce(function, iterable[, initializer])   # 合并操作, 从第一个开始是前两个参数, 然后是前两个的结果与第三个合并进行处理, 以此类推.    只能在python2中使用, python3中需要导入functools
# def add(x, y): return x + y
# import functools
# functools.reduce(add, range(1,11))  # 返回55, 从1加到10
# s = functools.reduce(add, range(1,11), 20)  # 返回75

# reload(module)    # 重新加载模块
# repr(object)    # 将一个对象变换为可打印的格式
# slice(start, stop[, step])  # 产生分配对象
# type(object)    # 返回该object的类型
# vars(object)    # 返回该镀锡的变量名, 变量值的字段
# class Employee(): pass
# a = Employee() # Employee为一个空类, python中貌似又没有
# a.name = 'qi', a.age = 9
# vars(a) # {"name":"qi", "age":9}
# zip(iterable, ...)  # 返回对应数组
list(zip([1, 2, 3], [4, 5, 6]))     # 返回 [(1, 4), (2, 5), (3, 6)]
a = [1, 2, 3]
b = ["a", "b", "c"]
# z = zip(a,b)    # 压缩：[(1, "a"), (2, "b"), (3, "c")]
# print(*z)   # 解压缩：[(1, 2, 3), ("a", "b", "c")]
# * 既可对迭代器解包, 又可对非迭代器的可迭代对象解包, NB了
# print(*[1,2,3,4])
# print(*iter([1, 2, 3, 4]))
# unicode(string, encoding, errors)   # 将字符串string转化为unicode形式, string为encoded string   # 只有python2能用

