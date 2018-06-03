#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Create time : 2018/6/3下午12:56
# Create by Saseny.Zhou
# File name: plist_read.py

import plistlib


def plist_file_write(obj, path):
    try:
        with open(path, 'wb') as f:
            plistlib.dump(obj, f, sort_keys=False)
    except:
        return False


def plist_file_read(path):
    try:
        with open(path, 'rb') as f:
            pl = plistlib.load(f)
        return pl
    except:
        return False


def plist_file_dumps(obj, path):
    try:
        data = plistlib.dumps(obj, sort_keys=False)
        f = open(path, 'wb')
        f.write(data)
    except:
        return False


def plist_file_loads(path):
    try:
        f = open(path, 'rb')
        data = plistlib.loads(f.read())
        return data
    except:
        return False
