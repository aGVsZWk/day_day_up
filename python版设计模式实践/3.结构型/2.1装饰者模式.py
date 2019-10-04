from functools import wraps

HOST_DOCKER = 0


def docker_host_required(f):
    """装饰器要求host类型是 HOST_DOCKER"""
    @wraps(f)
    def wrapper(*args, **kwargs):
        if args[0].type != HOST_DOCKER:
            raise Exception('Not docker host')
        else:
            return f(*args, **kwargs)
    return wrapper


class Host(object):
    """host类"""
    def __init__(self, type):
        self.type = type

    # 装饰这一方法
    @docker_host_required
    def create_container(self):
        print("create container")


if __name__ == "__main__":
    host = Host(HOST_DOCKER)
    host.create_container()
    print('-' * 40)
    host = Host(1)
    host.create_container()
