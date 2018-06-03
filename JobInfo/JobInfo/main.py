#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Create time : 2018/6/3下午12:26
# Create by Saseny.Zhou
# File name: main.py


import requests
import pprint
from page_read.city_code import *

configInfo = read_json_file("config/config.json")


def writeJsonWithCityCode():
    response = requests.get(configInfo["city-code"])
    city_code(response.text)


def getCity(city):
    cityInfo = read_json_file("config/city_code.json")
    if cityInfo is False:
        writeJsonWithCityCode()
        cityInfo = read_json_file("config/city_code.json")
    city_list = []
    for i in city:
        if cityInfo.get(i, False) is not False:
            city_list.append(cityInfo[i])
    return "%252C".join(city_list)


def getUrl(city, info, page):
    base = configInfo["final url"]
    return base.format(getCity(city), info, page)


def writeStartUrl(url, default, table, pageNumber=100):
    dictInfo = {"start": url,
                "default": default,
                "pageNumber": pageNumber,
                "table": table}
    write_json_file(dictInfo, "config/startUrl.json")


if __name__ == "__main__":
    city = ["苏州", "无锡", "常州", "泰州", "扬州"]
    table = "脚本工程师"

    url = getUrl(city, table, 1)
    default = getUrl(city, table, "{}")
    writeStartUrl(url, default, table, pageNumber=200)

    from scrapy import cmdline

    cmdline.execute('Scrapy crawl Job'.split())
