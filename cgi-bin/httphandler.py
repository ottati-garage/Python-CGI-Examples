#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi
import os
import pickle


class Request():
    """HTTPのリクエストをハンドリングクラス
    """
    def __init__(self, environ=os.environ):
        self.form = cgi.FieldStorage()
        self.environ = environ
        self.method = environ.get('REQUEST_METHOD', None)


class Response():
    """HTTPのレスポンスをハンドリングするクラス
    """
    def __init__(self):
        self.header = "Content-type: text/html\n"
        self.body = ""

    def set_body(self, body):
        self.body = body
        return self

    def make_output(self):
        return self.header + self.body

    def __str__(self):
        return self.make_output()


class BaseView():
    """ビューの基底クラス
    Usage:
    req = Request()
    print(SomeView().render(req))
    """
    http_method_names = ['get', 'post']

    def __init__(self, **kwargs):
        self.response = Response()
        for k, v in kwargs.items():
            setattr(self, k, v)

    def render(self, request):
        """標準出力用の文字列を返すメソッド
        """
        self.dispatch(request)
        return self.response.set_body(self.get_template() % self.get_content(request))

    def dispatch(self, request):
        if request.method.lower() not in self.http_method_names:
            handler = self.http_method_not_allowed
        else:
            handler = getattr(self, format(request.method.lower()),
                              self.http_method_not_allowed)
        handler(request)

    def http_method_not_allowed():
        raise NotImplementedError

    def get(self, request):
        pass

    def post(self, request):
        pass

    def get_content(self, request):
        return "Content is not defined."

    def get_template(self):
        html_body = """
        <html>
        <head>
        <meta charset="shift-jis">
        </head>
        <body>%s</body>
        </html>"""
        return html_body


class PickleMixin():
    """Pickleを使ってオブジェクトを永続化するためのMixin
    """
    filepath = None

    def render(self, request):
        self.obj = self.get_obj()
        return super().render(request)

    def get_obj(self):
        try:
            f = open(self.get_filepath(), "rb")
            obj = pickle.load(f)
        except IOError:
            obj = {}
        else:
            f.close()
        return obj

    def save_obj(self):
        with open(self.get_filepath(), 'wb') as f:
            pickle.dump(self.obj, f)

    def get_filepath(self):
        return self.filepath

if __name__ == "__main__":
    print("Content-type: text/html\n")
    print("This is not to be shown...")
