import tornado.web
import tornado.ioloop


class HomeHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # xxx = self.get_cookie('xxx')
        xxx = self.get_secure_cookie('xxx')
        if not xxx:
            self.redirect('/login')
            return
        self.write('welcome')
