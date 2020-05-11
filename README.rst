~*~*~*~*~*~*~*~*~* Warning ~*~*~*~*~*~*~*~*~* 

Due to it's lack of security controls, and the lack of CSRF in Flask, I am recommending that you don't use this library -- and instead write your own solution start to finish to understand the nuance of allowing request methods to be specified in GET parameters.

Flask-Modus
=====================

.. image:: https://secure.travis-ci.org/rhyselsmore/flask-modus.png?branch=master

Enable Flask Method overrides via Query String and Headers.

Allows for a much more enjoyable experience when building HTML which requires a custom method, or when using a client that doesn't support certain methods.

The following methods are supported:

    - Get
    - Post
    - Put
    - Patch
    - Delete
    - Options
    - Head

Installation
------------

Installation is very straightforward::

    pip install flask-modus

Configuration
-------------

Configuration is pretty damn easy::

    from flask import Flask
    from flask_modus import Modus

    app = Flask(__name__)
    modus = Modus(app)

*or*::

    from flask import Flask
    from flask_modus import Modus

    app = Flask(__name__)
    modus = Modus()
    modus.init_app(app)

Usage
-----

Either append your favoured methods to the end of your query string::

    $ curl http://localhost:5000/?_method=put

or supply a X-HTTP-Method-Override header::

    $ curl -H "X-HTTP-Method-Override: PUT" http://localhost:5000/

*Note:* If you supply both a header and a query string parameter, the method specified in the header will be that which is used.
