from tornado.web import UIModule
from tornado import escape

class custom(UIModule):

    def embedded_css(self):
        return '嵌入css'

    def css_files(self):
        #引入静态文件目录，需要配置static_path
        return 'commone.css'

    def embedded_javascript(self):
        return '嵌入js'

    def javascript_files(self):
        return 'xxx.js'

    def render(self, *args, **kwargs):
        # 视图函数的render内部调用render_string
        return "<h1>aaa</h1>"
        # return escape.xhtml_escape("<h1>aaa</h1>")
        return escape.xhtml_unescape('<h1>aaa</h1>')

    def render_string(self, path, **kwargs):
        pass