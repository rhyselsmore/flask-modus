Flask-Modus
=====================

.. image:: https://secure.travis-ci.org/rhyselsmore/flask-modus.png?branch=master

*Under Construction*

Enable Flask Method overrides via Query String and Headers

Installation
------------

Installation is very straightforward::

    pip install flask-modus

Usage
-----

Usage is even simpler::

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
