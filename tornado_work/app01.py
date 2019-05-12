import datetime
import hashlib

import tornado.web
import tornado.ioloop

import uimethods as mt
import uimodules as ml

container = {
    'sadsagds': {'xx': 'xxx', 'xx1': 'xxx1'}
}


class Bar:

    def __init__(self, handler):
        self.handler = handler
        self.ramdom_str = None

        # 先在请求信息中获取sessionid，如没有表示是新用户或者没有登录的
        client_random_str = self.handler.get_cookie('session_id')
        if not client_random_str or client_random_str in container:
            '''新用户和非法用户'''
            self.ramdom_str = self.create_ramdom_str()
            container[self.ramdom_str] = {}
        else:
            '''老用户'''
            self.ramdom_str = client_random_str
        ctime = datetime.datetime.now()
        delta = datetime.timedelta(1800)
        self.handler.set_cookie('session_id', self.ramdom_str, expires=ctime + delta)

    def create_ramdom_str(self):
        v = str(datetime.datetime.now())
        m = hashlib.md5()
        m.update(bytes(v, encoding='utf-8'))
        return m.hexdigest()

    def __setitem__(self, key, value):
        container[self.ramdom_str][key] = value

    def __getitem__(self, item):
        return container[self.ramdom_str][item]

    def __delitem__(self, key):
        del container[self.ramdom_str][key]

    def clear(self):
        del container[self.ramdom_str]


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
