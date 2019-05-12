import socket
import select
import datetime


class Future:
    def __init__(self, timeout):
        self.result = None
        self.timeout = timeout
        self.start = datetime.datetime.now()


class HttpRequest(object):
    """
    用户封装用户请求信息
    """

    def __init__(self, content):
        """

        :param content:用户发送的请求数据：请求头和请求体
        """
        self.content = content

        self.header_bytes = bytes()
        self.body_bytes = bytes()

        self.header_dict = {}

        self.method = ""
        self.url = ""
        self.protocol = ""

        self.initialize()
        self.initialize_headers()

    def initialize(self):

        temp = self.content.split(b'\r\n\r\n', 1)
        if len(temp) == 1:
            self.header_bytes += temp
        else:
            h, b = temp
            self.header_bytes += h
            self.body_bytes += b

    @property
    def header_str(self):
        return str(self.header_bytes, encoding='utf-8')

    def initialize_headers(self):
        headers = self.header_str.split('\r\n')
        first_line = headers[0].split(' ')
        if len(first_line) == 3:
            self.method, self.url, self.protocol = headers[0].split(' ')
            for line in headers:
                kv = line.split(':')
                if len(kv) == 2:
                    k, v = kv
                    self.header_dict[k] = v


f = None


def index(reuqest):
    global f
    f = Future()
    return f


def stop(request):
    global f
    f.result = b'xxxxxxxxxxx'
    return f


def main(reuqest):
    return 'main'


routers = [
    ('/index', index),
    ('/main', main)
]


# 同步框架
# def run():
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     sock.bind(("127.0.0.1", 9999,))
#     sock.setblocking(False)
#     sock.listen(128)
#
#     inputs = []
#     inputs.append(sock)
#
#     while True:
#         rlist, wlist, elist = select.select(inputs, [], [], 0.05)
#         for r in rlist:
#             if r == sock:
#                 '''新请求到来'''
#                 conn, addr = sock.accept()
#                 conn.setblocking(False)
#                 inputs.append(conn)
#             else:
#                 '''客户端请求'''
#                 data = bytes()
#                 while True:
#                     try:
#                         chunk = r.recv(1024)
#                         data += chunk
#                     except Exception as e:
#                         chunk = None
#                     if not chunk:
#                         break
#
#                 # 1、data处理，获取请求头和请求体
#                 # 2、获取url 匹配路由  获取执行函数
#                 # 3、执行函数 获取返回值
#                 # 4、send返回值回去
#                 request = HttpRequest(data)
#                 import re
#                 flag = False
#                 func = None
#                 for router in routers:
#                     if re.match(router[0], request.url):
#                         flag = True
#                         func = router[1]
#                         break
#                 if flag:
#                     result = func(request)
#                 else:
#                     result = '404'
#
#                 r.sendall(bytes(result, encoding='utf-8'))
#                 inputs.remove(r)
#                 r.close()

def asyncrun():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("127.0.0.1", 9999,))
    sock.setblocking(False)
    sock.listen(128)

    inputs = []
    async_dict = {}

    inputs.append(sock)

    while True:
        rlist, wlist, elist = select.select(inputs, [], [], 0.05)
        for r in rlist:
            if r == sock:
                '''新请求到来'''
                conn, addr = sock.accept()
                conn.setblocking(False)
                inputs.append(conn)
            else:
                '''客户端请求'''
                data = bytes()
                while True:
                    try:
                        chunk = r.recv(1024)
                        data += chunk
                    except Exception as e:
                        chunk = None
                    if not chunk:
                        break

                # 1、data处理，获取请求头和请求体
                # 2、获取url 匹配路由  获取执行函数
                # 3、执行函数 获取返回值
                # 4、send返回值回去
                request = HttpRequest(data)
                import re
                flag = False
                func = None
                result = '404'
                for router in routers:
                    if re.match(router[0], request.url):
                        flag = True
                        func = router[1]
                        break
                if flag:
                    result = func(request)
                    if isinstance(result, Future):
                        async_dict[r] = result
                    else:
                        r.sendall(bytes(result, encoding='utf-8'))
                else:
                    r.sendall(bytes(result, encoding='utf-8'))

                inputs.remove(r)
                r.close()

        temp = []
        for conn in async_dict.keys():
            future = async_dict[conn]

            start = future.start
            timeout = future.timeout
            ctime = datetime.datetime.now()
            if (start + timeout) <= ctime:
                future.result = b"timeout"
            if future.result:
                conn.sendall(future.result)
                conn.close()
                inputs.remove(conn)
                temp.append(conn)
            else:
                pass

        for conn in temp:
            del async_dict[conn]


if __name__ == '__main__':
    asyncrun()
