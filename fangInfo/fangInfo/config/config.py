#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time     : 2018/6/8下午6:10
# @Author   : Saseny Zhou
# @Site     : 
# @File     : config.py
# @Software : PyCharm

helpMessageInfo = """租房:
    c20-d21000-g22-i32

    c2{}-d2{}     价格: 0-1000
    g2{}          户型: 1 一居，2 二居，3 三居，4 四居，99 四居以上
    n3{}          方式: 1 整租，/hezu/ 合租，

新房:
    http://newhouse.nanjing.fang.com/house/s/b210000%2C15000-b92-c22/
    b210000%2C15000 价格 10000-15000
    c22             两居室
    b92             第二页

二手房:
    http://esf.nanjing.fang.com/house/c2100-d2120-g22-j250-k270-i32/
    c2100-d2120     价格 100-120万
    g22             两居室
    j250-k270       50-70平米
    i32             第二页
"""

defaultConfigInfo = {
    "city_urls": "http://js.soufunimg.com/homepage/new/family/css/citys20171228.js",
    "target_url":
        {
            "新房":
                {
                    "main": "http://newhouse.{}.fang.com/",
                    "page-normal": "http://newhouse.{}.fang.com/house/s/b9{}/",
                    "page-parameter": "http://newhouse.{}.fang.com/house/s/{}/"
                },
            "二手房":
                {
                    "main": "http://esf.{}.fang.com/",
                    "page-normal": "http://esf.{}.fang.com/house/i3{}",
                    "page-parameter": "http://esf.{}.fang.com/house/{}/"
                },
            "租房":
                {
                    "main": "http://zu.{}.fang.com/",
                    "page-normal": "http://zu.{}.fang.com/house/i3{}/",
                    "page-parameter": "http://zu.{}.fang.com/house/{}/"
                },
            "查房价": "http://fangjia.fang.com/{}/",
            "装修家居": "http://home.{}.fang.com/",
            "写字楼": "http://office.{}.fang.com/",
            "商铺":
                {
                    "main": "http://shop.{}.fang.com/",
                    "page-normal": "http://shop.{}.fang.com/shou/house/i3{}/"
                },
            "业主论坛": "",
            "房产百科": "http://news.{}.fang.com"
        },
    "help info": helpMessageInfo
}

from file_read_write.json_file import *
from pprint import pprint


def write_default_config():
    pprint(defaultConfigInfo)
    write_json_file(defaultConfigInfo, "config/config.json")
