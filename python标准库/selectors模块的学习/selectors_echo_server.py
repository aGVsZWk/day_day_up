# 运行模式
# selectors 里面的API是事件驱动的， 类似与 select 里面的 poll() 方法.
# 有几种实现方式，并且这个模块可以自动根据当前的操作系统的配置设置一个别名为 DefaultSelector 来引用最有效率的一个方式.

# 选择器都喜爱那个提供了一个用来指定socket上监听事件的方法，然后让调用以平台无关的方式等待事件。注册感兴趣的事件会创建一个
# SelecotrKey来保存 socket 感兴趣的事件信息和可选的应用程序信息。
# 选择其的所有者通过调用select()方法来了解事件进度。该方法的返回值是一系列的key对象和标识发生事件种类的位掩码。
# 使用选择其的程序需要不断的调用select()方法去及时的处理事件。

# 服务器响应
import selectors
import socket

mysel = selectors.DefaultSelector()
keep_running = True


def read(connection, mask):
    """读取事件的回调"""
    global keep_running

    client_address = connection.getpeername()
    print('read({})'.format(client_address))
    data = connection.recv(1024)
    if data:
        # 可读的客户端 socket 有数据
        print(' received {!r}'.format(data))
        connection.sendall(data)

    else:
        # 将空的结果解释为关闭链接
        print('  closing')
        mysel.unregister(connection)
        connection.close()
        # 告诉主进程停止
        keep_running = False


def accept(sock, mask):
    """有新链接的回调"""
    new_connection, addr = sock.accept()
    print('accept({})'.format(addr))
    new_connection.setblocking(False)
    mysel.register(new_connection, selectors.EVENT_READ, read)


if __name__ == '__main__':
    server_address = ('localhost', 10000)
    print('starting up on {} port {}'.format(*server_address))
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setblocking(False)
    server.bind(server_address)
    server.listen(5)

    mysel.register(server, selectors.EVENT_READ, accept)

    while keep_running:
        print('waiting for I/O')
        for key, mask in mysel.select(timeout=1):
            callback = key.data
            callback(key.fileobj, mask)

    print('shutting down')
    mysel.close()
