import tornado.web
import tornado.ioloop


class LoginHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('login.html',msg="")

    def post(self, *args, **kwargs):
        # v = self.request.files['xxxx']#获取上传文件 xxx即标签的name
        # self._headers #请求头对象
        username = self.get_argument('user')
        password = self.get_argument('pwd')

        # self.get_body_argument()
        # self.get_body_arguments()
        #
        # self.get_query_argument()
        # self.get_query_arguments()
        #
        # self.get_argument()
        # self.get_arguments()

        if username == 'root' and password == '123':
            # self.set_cookie('xxx','ooo')
            self.set_secure_cookie('xxx','ooo')
            self.redirect('/home')
        else:
            self.render('login.html',msg='用户名或密码错误')
