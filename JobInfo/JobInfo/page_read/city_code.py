#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Create time : 2018/6/3下午12:39
# Create by Saseny.Zhou
# File name: city_code.py

import re
from page_read.json_read import *


def city_code(text):
    listInfo = []
    configInfo = read_json_file("config/config.json")["special name"]
    for i in str(text).split("\"")[1:-1]:
        if re.findall("\w+", str(i)):
            listInfo.append(i)
    if len(listInfo) % 2 == 0:
        dictInfo = {}
        for l in range(0, int(len(listInfo) / 2), 2):
            if configInfo.get(listInfo[l],False) is not False:
                dictInfo[configInfo[listInfo[l]]] = listInfo[l]
            else:
                dictInfo[listInfo[l + 1]] = listInfo[l]
        write_json_file(dictInfo, "config/city_code.json")
