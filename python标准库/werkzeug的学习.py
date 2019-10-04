# 信息隔离: 有两个线程, 线程A里的变量和线程B里的变量不能共享, 这就是线程隔离.
# 如何实现线程隔离: threading.local

from threading import local, Thread, currentThread

# 定义一个local实例
local_data = local()
# 在主线中给, 存入name这个变量
local_data.name = 'local_data'


class MyThread(Thread):
    def run(self):
        print("赋值前-子线程: ", currentThread, local_data.__dict__)
        local_data.name = self.getName()
        print("赋值后-子线程: ", currentThread, local_data.__dict__)


if __name__ == '__main__':
    print("开始前-主线程: ", local_data.__dict__)
    t1 = MyThread()
    t1.start()
    t1.join()

    t2 = MyThread()
    t2.start()
    t2.join()

    print("开始前-主线程: ", local_data.__dict__)


# local实际上就是一个字典型对象, 全局唯一, 只有一个. 它会根据当前的线程从不同的存储空间中读取或存入.
