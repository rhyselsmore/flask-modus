#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from flask import Flask, request
from flask_method_rewrite import MethodRewrite


class MethodRewriteTestCase(unittest.TestCase):

    def setUp(self):
        """ Construct our Flask Test App """

        def index():
            return "get"

        def put():
            return "put"

        self.app = Flask(__name__)
        method_rewrite = MethodRewrite()
        method_rewrite.init_app(self.app)
        self.app.add_url_rule('/', 'index', index, methods=['GET'])
        self.app.add_url_rule('/', 'put', put, methods=['PUT'])
        self.client = self.app.test_client()

    def test_get(self):
        """ Test get """

        assert "get" in self.client.get('/').data

    def test_query_string(self):
        """ Test put """

        rv = self.client.put('/')
        assert "put" in rv.data
        rv = self.client.post('/?_method=put')
        assert "put" in rv.data

        with self.app.test_client() as c:
            c.post('/?_method=put')
            assert request.method == 'PUT'

    def test_x_header(self):
        with self.app.test_client() as c:
            c.post(
                '/',
                headers=[('X-HTTP-Method-Override', 'put')]
            )
            assert request.method == 'PUT'

if __name__ == '__main__':
    unittest.main()
