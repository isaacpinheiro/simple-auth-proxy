#!/usr/bin/python
# -*- coding: utf-8 -*-

config = {}

# Proxy Configuration
config['proxy_host'] = '0.0.0.0'
config['proxy_port'] = 5000

# App Configuration
config['app_host'] = 'http://localhost'
config['app_port'] = 1026
config['app_ssl_verification'] = True # Always use True in production!

# Identity Manager Configuration
config['idm_host'] = 'http://localhost'
config['idm_port'] = 3001
config['idm_ssl_verification'] = True # Always use True in production!
config['idm_app_id'] = ''

