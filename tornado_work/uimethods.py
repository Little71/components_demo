from tornado import escape

def tag(self):
    return "<h1>aaa</h1>"
    # return escape.xhtml_escape("<h1>aaa</h1>")
    return escape.xhtml_unescape("<h1>aaa</h1>")
    return 'uimethods'