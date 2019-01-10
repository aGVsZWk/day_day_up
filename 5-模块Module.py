# 五. 模块Module

# 1--python模块搜索路径
"""
(1) 程序的主目录
(2) PYTHONPATH目录    # 是一个列表, 里面包含要搜索的库, 搜索顺序从前到后, 可以append路径, 也可insert路径, 但下次执行就会消失; 可写环境变量PYTHONPATH把它设置死
(3) 标准链接库目录
(4) 任何.pth文件的内容
"""


# 2--查看全部的模块搜索路径
import sys
# sys.path     # 一个列表, 包含所有系统导包的路径
# sys.argv     # 获得脚本的参数
# sys.builtin_module_names    # 查找内建模块
# print(sys.platform)    # 返回当前平台, 出现如: win32, linux, darwin等
# sys.modules     # 查找已经导入的模块
# sys.modules.keys()
# sys.stdout    # stdout和stderr都是类文件对象, 但是它们都是只写的. 它们都没有read方法, 只有write方法. 文件流
# sys.stdout.write("hello")     # 默认显示窗口, 往显示窗口里输出个hello
# sys.stderr.write("hello")     # 往显示窗口里输出个hello, 颜色和stdout不一样, 是输出错误, 红色的字
# sys.stdin


# 3--模块的使用代码
# import module1, module2   # 导入module1, 使用module1.printer()
# from module1 import printer     # 导入module1中的printer变量, 使用printer()
# from module1 import *     # 导入module1中的全部变量, 使用不必添加module前缀



# 4--重载模块的reload: 这是一个函数 ,而不是一条语句
# from imp import reload    # reload()函数在python2中是内置的, 在python3.0貌似是python3.4之前都是在imp模块中, 但是imp模块即将被废弃, 所以上面会有删除线
from importlib import reload      # 比较新的是在importlib中
# reload(module)

# 5--模块的包导入: 使用点号(.), 而不是路径(dir1\dir2)进行导入
# import dir1.dir2.mod  # 导入包(目录)dir1中的包dir2中的mod模块, 此时dir1必须在python可搜索路径中
# from dir1.dir2.mod import *


# 6--__init__.py包文件: 每个导入的包中都应该包含这么一个文件
"""
该文件可以为空
首次进行包导入时, 该文件会自动执行
高级功能: 在该文件中使用__all__列表来定义包(目录)以from*的形式导入时, 可导入的方法或属性
"""

# 7--包相对导入: 使用点号(.) 只能使用from语句
# from . import spam    # 导入当前目录下的spam模块(Python2: 当前目录下的模块, 直接导入即可)
# from .spam import name    #
# from .. import spam   # 导入当前目录的父目录下的spam模块




# 8--包相对导入和普通导入的区别
# from string import *    # 这里导入的string模块为sys.path路径上的, 而不是本目录下的string模块(如果存在也不是)
# from .string import *   # 这里导入的string模块为本目录下的(不存在则导入失败), 而不是sys.path路径上的


# 9--模块数据隐藏: 最小化from * 的破坏
# 使用_开头的变量或方法, 不能被其它文件所导入
# _X        # 变量名前加下划线可以防止from导入时该变量名被复制出去
# from import_test import *   # 只导入不以_开头的, 不在__all__中的也不被导入     # 一导入它, 包的__init__.py就会被执行
# print(X)
# print(XX)
# __all__ = [str1, str2, ...]   # 使用__all__列表指定from*时复制出去的变量名(变量名在列表中为字符串形式)

# 10--可以使用__name__进行模块的单元测试: 当模块为顶层执行文件时值为"__main__", 当模块被导入时为模块名
if __name__ == "__main__":
    pass


# 11--模块中的属性, 例如:
# __doc__     # 模块的说明文档
# __file      # 模块文件的文件名, 包括全路径
# __name__    # 主文件或者被导入文件
# __package__ # 模块所在的包




# 12--import语句from语句的as扩展
# import modulename as name
# from modulename import attrname as name



# 13--得到模块属性的集中欧冠方法, 假设为了得到name属性的值
# M.name
# M.__dict__["name"]
# sys.modules[M].name
# getattr(M, 'name')
