#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return 'Simple Auth Proxy: ' + path

if __name__ == '__main__':
    app.run()

