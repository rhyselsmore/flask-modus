"""
Flask-Modus
------------

This is a simple Flask extension that configures your Flask
application to handle method overrides when POSTing.

"""

from setuptools import setup

setup(
    name='Flask-Modus',
    version='0.0.1',
    url='https://github.com/rhyselsmore/flask-modus',
    license='BSD',
    author='Rhys Elsmore',
    author_email='me@rhys.io',
    description='Flask Method Overriding Middleware.',
    long_description=__doc__,
    py_modules=['flask_modus'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=['Flask'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
