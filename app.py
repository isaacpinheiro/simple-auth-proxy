#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
import requests as req
import json
import re

from config import config

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

def verify_access_token(headers):

    authorized = False

    if headers.get('Authorization') == None:
        return authorized
    elif re.match('^Bearer .*$', headers.get('Authorization')) == None:
        return authorized

    token = headers.get('Authorization').split(' ')[1]
    idm_url = config['idm_host'] + ':' + str(config['idm_port']) + '/user?access_token=' + token
    res = req.get(idm_url, verify=config['idm_ssl_verification'])
    obj = json.loads(res.text)

    if obj.get('app_id') ==  config['idm_app_id']:
        authorized = True

    return authorized

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'PATCH', 'OPTIONS'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'PATCH', 'OPTIONS'])
def index(path):

    if verify_access_token(request.headers) == False:
        return {'msg': 'Unauthorized'}

    url = config['app_host'] + ':' + str(config['app_port']) + '/' + path + get_params_string(request.args)

    res = req.request(
        request.method,
        url,
        verify=config['app_ssl_verification'],
        json=request.json,
        headers=request.headers
    )

    if res.text != None and res.text != '':
        return jsonify(json.loads(res.text))
    else:
        return jsonify({})

if __name__ == '__main__':
    app.run(host=config['proxy_host'], port=config['proxy_port'])

