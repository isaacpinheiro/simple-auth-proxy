#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, request

app = Flask(__name__)

def get_params_string(params):

    res = ''
    keys = list(params.keys())

    for k in keys:

        if res == '':
            res += '?' + k + '=' + str(params[k])
        else:
            res += '&' + k + '=' + str(params[k])

    return res

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return 'Simple Auth Proxy: ' + path + get_params_string(request.args)

if __name__ == '__main__':
    app.run()

