def log(*args, **kwargs):
    """
    自定义 log
    """
    print(*args, **kwargs)


def singleton(cls):
    """
    单例装饰器
    """
    _instance = {}

    def inner():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]
 
    return inner
