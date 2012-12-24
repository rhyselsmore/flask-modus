# -*- coding: utf-8 -*-

from werkzeug import url_decode


class Middleware(object):
    """ WSGI Method Overriding Middleware """

    allowed_methods = frozenset([
        'GET',
        'HEAD',
        'POST',
        'DELETE',
        'PUT',
        'PATCH',
        'OPTIONS'
    ])
    bodyless_methods = frozenset(['GET', 'HEAD', 'OPTIONS', 'DELETE'])

    def __init__(self, app=None, input_name=''):
        self.app = app
        self.input_name = input_name

    def __call__(self, environ, response):
        """ Extract the new method from the Query String """

        def set_method(method):
            if method in self.allowed_methods:
                method = method.encode('ascii', 'replace')
                environ['REQUEST_METHOD'] = method
            if method in self.bodyless_methods:
                environ['CONTENT_LENGTH'] = '0'

        # Handle our Header Method
        method = environ.get('HTTP_X_HTTP_METHOD_OVERRIDE', '').upper()
        if method in self.allowed_methods:
            set_method(method)
            return self.app(environ, response)

        # Handle our Query String Method setter
        if '_method' in environ.get('QUERY_STRING', ''):
            args = url_decode(environ['QUERY_STRING'])
            method = args.get('_method', '').upper()
            if method in self.allowed_methods:
                set_method(method)

        return self.app(environ, response)


class Modus(object):
    """ Enables Flask Method Overriding """

    def __init__(self, app=None):
        self.app = app

        if self.app:
            self.init_app(self.app)

    def init_app(self, app):
        """ Configures the Flask Overriding Middleware """

        app.wsgi_app = Middleware(app.wsgi_app)
