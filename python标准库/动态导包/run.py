import importlib

# 导入user.py模块
user = importlib.import_module('my_module.user')
# 调用user.py中的get_info()方法，打印信息
print(user.get_info())

my_module = importlib.import_module('my_module')
print(my_module.user.get_info())
