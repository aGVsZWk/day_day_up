# 八. 异常相关
# 1--捕获异常
import sys

try:
    pass
except:       # 捕获所有异常, 等同于except Exception
    pass
# except name:    # 捕获指定的异常
# except name, value:   # 捕获指定的异常和额外的数据(实例)
# except (name1, name2):
# except (name1, name2), value:
# except name4 as X:
else:           # 如果没有发生异常
    pass
finally:        # 总会执行的部分
    pass

# 引发异常: raise子句(raise IndexError)
# raise <instance>  # raise instance of a class, raise IndexError()
# raise <class> # make and raise instance of a class, raise IndexError
# raise   # raise the most recent exception




# 2--Python3.x中的异常链: raise exception from otherException
# except Exception as X:    # 错误详细信息给X
#     raise IndexError('Bad') from X    # todo

# 3--assert子句: assert<test>, <data>
# x = 2
# assert x < 0, 'x must be negative'  # 抛出错误, AssertionError: x must be negative

# 4--with/as环境管理器: 作为常见的try/finally用法模式的替代方案
# with expression [as variable],expression [as variable]:
# 例:
# with open('log.log') as myfile:
#     for line in myfile: print(line)
# 等同于
# myfile = open('log.log')
# try:
#     for line in myfile: print(line)
# finally:
#     myfile.close()




# 5--用户自定义异常: class Bad(Exception)......
"""
Exception超类/ except基类即可捕获到其所有的子类
Exception超类有默认的打印消息和状态, 当然也可以定制打印显示:
"""
class MyBad(Exception):
    def __str__(self):
        return "定制的打印消息"
# try:
#     raise MyBad
# except MyBad as x:
#     print(x)

# 6--用户定制异常数据
class FormatError(Exception):
    def __init__(self, line, file):
        self.line = line
        self.file = file
try:
    raise FormatError(42, 'test.py')
except FormatError as X:
    pass
    # print('Error at', X.file, X.line)



# 7--用户定制异常行为(方法): 以记录日志为例
class FormatError(Exception):
    logfile = 'log.log'
    def __init__(self, line, file):
        self.line = line
        self.file = file

    def logger(self):
        open(self.logfile, 'a', encoding='utf-8').write('\nError at {0} {1}'.format(self.file, self.line))
try:
    raise FormatError(42,'test.py')
except FormatError as X:
    X.logger()



# 8--关于sys.exc_info: 允许一个异常处理器获取对最近引发异常的访问
# try:
#     pass
#     abc
# except:
    # 此时sys.exc_info()返回一个元组(type, value, tarceback)
    # type: # 处理的异常的异常类型
    # value: 引发的异常的实例
    # traceback: 堆栈信息
    # print(sys.exc_info())





# 9--异常层次:
# BaseException
# +-- SystemExit
# +-- KeyboardInterrupt
# +-- GeneratorExit
#     +-- Exception
#     +-- StopIteration
#     +-- ArithmeticError
#     +-- AssertionError
#     +-- AttributeError
#     +-- BufferError
#     +-- EOFError
#     +-- ImportError
#     +-- LookupError
#     +-- MemoryError
#     +-- NameError
#     +-- OSError
#     +-- ReferenceError
#     +-- RuntimeError
#     +-- SyntaxError
#     +-- SystemError
#     +-- TypeError
#     +-- ValueError
#     +-- Warning
