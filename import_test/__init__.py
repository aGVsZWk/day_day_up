"""导包测试
"""
# 以_开头的不能被其它导出
__X = 0
_X = 1
X = 2
XX = 3
__all__ = ['X',]   # 指定可被其它模块所导入的内容, 必须是字符串形式.
print("是主文件还是被其它文件导入", __name__)     # 被其它文件导入时, 打印此包的名字 import_test
print("模块所在的包", __package__)
print("模块的绝对路径", __file__)
print("模块的说明文档", __doc__)