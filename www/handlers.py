#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/12/7 上午10:24
# @Author  : chenyuqiao
# @File    : handlers.py
from www.coroweb import get
from www.models import User


@get('/')
async def index(request):
    users = await User.findAll()
    return {
        '__template__': 'test.html',
        'users': users
    }