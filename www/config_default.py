#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/12/7 上午10:21
# @Author  : chenyuqiao
# @File    : config_default.py


configs = {
    'debug': True,
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'admin',
        'password': '123456',
        'db': 'awesome'
    },
    'session': {
        'secret': 'Awesome'
    }
}