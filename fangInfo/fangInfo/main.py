#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time     : 2018/6/8下午4:58
# @Author   : Saseny Zhou
# @Site     : 
# @File     : main.py
# @Software : PyCharm


from page_read.getUrls import *
from config.config import *
from scrapy import cmdline

configInfo = read_json_file("config/config.json")
cityInfo = read_json_file("config/cityUrl.json")

if cityInfo is False:
    cityInfo = getUrls(configInfo["city_urls"])[1]

write_default_config()
