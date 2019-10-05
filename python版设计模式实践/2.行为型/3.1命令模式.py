import abc


class VmReceiver(object):
    """命令接受者, 真正执行命令的地方"""
    def start(self):
        print("Visual machine start")

    def stop(self):
        print("Visual machine stop")


class Command(object):
    """命令抽象类"""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def execute(self):
        """命令对象对外只提供execute方法"""
        pass


class StartVmCommand(Command):
    """开启虚拟机命令"""
    def __init__(self, receiver):
        """使用一个命令接受者初始化"""
        self.receiver = receiver

    def execute(self):
        """真正执行命令的时候命令接受者开启虚拟机"""
        self.receiver.start()


class StopVmCommand(Command):
    def __init__(self, receiver):
        """使用一个命令接受者初始化"""
        self.receiver = receiver

    def execute(self):
        """真正执行命令的时候命令接受者开启虚拟机"""
        self.receiver.stop()


class ClientInvoker(object):
    """命令调用者"""
    def __init__(self, command):
        self.command = command

    def do(self):
        self.command.execute()


if __name__ == '__main__':
    receiver = VmReceiver()
    start_command = StartVmCommand(receiver)
    # 命令调用者, 同时也是客户端, 通过命令实例也执行真正的操作
    client = ClientInvoker(start_command)
    client.do()

    # 告诉命令接受者执行不同的操作
    stop_command = StopVmCommand(receiver)
    client.command = stop_command
    client.do()
