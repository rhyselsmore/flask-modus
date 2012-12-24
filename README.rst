Flask Method Override
=====================

.. image:: https://secure.travis-ci.org/rhyselsmore/flask-method-override.png?branch=master

*Under Construction*

Enable Flask Method overrides via Query String and Headers

Installation
------------

Installation is very straightforward::

    pip install flask-methodoverride

Usage
-----

Usage is even simpler::

    from flask import Flask
    from flask_method_override import MethodOverride

    app = Flask(__name__)
    method_override = MethodOverride(app)

*or*::

    from flask import Flask
    from flask_method_override import MethodOverride

    app = Flask(__name__)
    method_override = MethodOverride()
    method_override.init_app(app)
