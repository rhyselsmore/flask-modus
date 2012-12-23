# -*- coding: utf-8 -*-

from werkzeug import url_decode


class Middleware(object):
    """ WSGI Method Rewriting Middleware """

    def __init__(self, app=None, input_name=''):
        self.app = app
        self.input_name = input_name

    def __call__(self, environ, response):
        """ Extract the new method from the Query String """

        if 'METHOD_OVERRIDE' in environ.get('QUERY_STRING', ''):
            args = url_decode(environ['QUERY_STRING'])
            method = args.get('__METHOD_OVERRIDE__')
            if method:
                method = method.encode('ascii', 'replace')
                environ['REQUEST_METHOD'] = method
        return self.app(environ, response)


class MethodRewrite(object):
    """ Enables Flask Method Rewriting """

    def __init__(self, app=None):
        self.app = app

        if self.app:
            self.init_app(self.app)

    def init_app(self, app):
        """ Configures the Flask Rewriting Middleware """

        app.wsgi_app = Middleware(app.wsgi_app)
