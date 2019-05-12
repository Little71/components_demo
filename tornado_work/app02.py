import datetime
import hashlib

import tornado.web
import tornado.ioloop

import uimethods as mt
import uimodules as ml


class Cache:
    '''
    表示将session保存在内存，所以还可以配置其他保存方式
    这就不需要更改session组件
    '''

    def __init__(self):
        self.container = {}

    def __contains__(self, item):
        return item in self.container

    def initial(self, random_str):
        self.container[random_str] = {}

    def get(self, random_str, key):
        return self.container[random_str][key]

    def set(self, random_str, key, value):
        self.container[random_str][key] = value

    def delete(self, random_str, key):
        del self.container[random_str][key]

    def open(self):
        pass

    def close(self):
        pass

    def clear(self, random_str):
        del self.container[random_str]


P = Cache


class Bar:

    def __init__(self, handler):
        self.handler = handler
        self.random_str = None
        self.db = P()
        self.db.open()

        # 先在请求信息中获取sessionid，如没有表示是新用户或者没有登录的
        client_random_str = self.handler.get_cookie('session_id')
        if not client_random_str or client_random_str in self.db:
            '''新用户和非法用户'''
            self.random_str = self.create_ramdom_str()
            self.db.initial(self.random_str)
        else:
            '''老用户'''
            self.random_str = client_random_str

        ctime = datetime.datetime.now()
        delta = datetime.timedelta(1800)
        self.handler.set_cookie('session_id', self.random_str, expires=ctime + delta)
        self.db.close()

    def create_ramdom_str(self):
        v = str(datetime.datetime.now())
        m = hashlib.md5()
        m.update(bytes(v, encoding='utf-8'))
        return m.hexdigest()

    def __setitem__(self, key, value):
        self.db.open()
        self.db.set(self.random_str, key, value)
        self.db.close()

    def __getitem__(self, key):
        self.db.open()
        v = self.db.get(self.random_str, key)
        self.db.close()
        return v

    def __delitem__(self, key):
        self.db.open()
        self.db.delete(self.random_str, key)
        self.db.close()

    def clear(self):
        self.db.open()
        self.db.clear(self.random_str)
        self.db.close()


class Foo:

    def initialize(self):
        self.session = Bar(self)


class HomeHandler(Foo, tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        user = self.session['uuuuu']
        if not user:
            self.redirect('xxxx')
        else:
            self.write('xxx')


class MainHandler(Foo, tornado.web.RequestHandler):

    def get(self):
        '''
        1、生成随机字符串
        2、写到应用浏览器上 cookie
        3、后台存储session信息
        :return:
        '''
        # self.session['is_login'] = True
        # self.session['user'] = 'tom'
        # # xxx = self.session['xx']
        # # del self.session['xx']
        # self.write('hello world')
        self.session['uuuuu'] = 'root'
        self.redirect('/home')


application = tornado.web.Application([
    ('/index', MainHandler),
    ('/home', HomeHandler),
])

if __name__ == '__main__':
    application.listen(9999)
    tornado.ioloop.IOLoop.instance().start()
