#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time     : 2018/6/8下午4:57
# @Author   : Saseny Zhou
# @Site     : 
# @File     : getUrls.py
# @Software : PyCharm


import requests
import time
import re
from file_read_write.json_file import *


def getUrls(url, times=3):
    try:
        response = requests.get(url)
        if response.status_code == 200 and "name" in response.text:
            return str_to_dict(response.text)
    except:
        print("Get Url: [{}] Fail.".format(url))
        if times > 0:
            time.sleep(3)
            print("Try again ...")
            getUrls(url=url, times=times - 1)


def str_to_dict(text):
    listInfo = text.split("},")
    dictInfo = dict()
    for i in range(len(listInfo)):
        tmp = listInfo[i].split("\"")
        dictInfo[tmp[3]] = {"spell": tmp[7], "url": tmp[11]}
    write_json_file(dictInfo, "config/cityUrl.json")
    return len(dictInfo), dictInfo
