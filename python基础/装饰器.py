# 极其标准的写法

def decorator(f):
    def wrapper(*args, **kwargs):
        print(f.__name__)
        return f(*args, **kwargs)
    return wrapper

# 带参数的写法
def log(message):
    def decorator(f):
        def wrapper(*args, **kwargs):
            print('log: ' + message)
            print(f.__name__)
            return f(*args, **kwargs)
        return wrapper
    return decorator

@log("fuck you")
def foo1(a=10, b = 15):
    print(a+b)

@decorator
def foo2(a=10, b=15):
    print(a+b)

foo1()
foo2()
