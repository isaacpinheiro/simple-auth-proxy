#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
import requests as req
import json

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

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'PATCH', 'OPTIONS'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'PATCH', 'OPTIONS'])
def index(path):

    url = 'http://localhost:1026/' + path + get_params_string(request.args)
    res = req.request(request.method, url, json=request.json, headers=request.headers)

    if res.text != None and res.text != '':
        return jsonify(json.loads(res.text))
    else:
        return jsonify({})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

