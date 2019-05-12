import tornado.web
import tornado.ioloop
from tornado.gen import Runner

import uimethods as mt
import uimodules as ml

from controllers.account import LoginHandler
from controllers.home import HomeHandler

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('hello world')  # 返回文本
        self.render('index.html')  # 渲染模板
        self.redirect('http://')  # 重定向


# 配置
settings = {
    'template_path': 'templates',
    'cookie_secret': 'dsjahu8wu8jf5eg16e1rhg1r5b2q6d4e8w6789t7d1b631fg',
    'static_path': 'static',
    'static_url_prefix': '/static/',
    'ui_methods': mt,
    'ui_modules': ml,

}
application = tornado.web.Application([
    ('/index', MainHandler),
    ('/login', LoginHandler),
    ('/home', HomeHandler),
], **settings)

if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
