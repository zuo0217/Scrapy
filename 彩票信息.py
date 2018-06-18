#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time     : 2018/6/18下午6:11
# @Author   : Saseny Zhou
# @Site     : 
# @File     : 彩票信息.py
# @Software : PyCharm

import requests
import pprint
import time
import json


class lottery_ticket():
    url_ = "http://www.lottery.gov.cn/api/lottery_kj_detail_new.jspx?_ltype=4&_term={}"
    _url = "http://cp.zgzcw.com/lottery/hisnumber.action?lotteryId=001&issueLen=100"

    def request(self, **kwargs):
        try:
            response = requests.get(url=kwargs.get("url", ""), params=kwargs.get("data", ""),
                                    headers=kwargs.get("header", ""))
            return response.json()
        except:
            return {}

    def time(self, number):
        try:
            time_array = time.localtime(int(number))
            other_style = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
            return other_style
        except:
            return None

    def write(self, obj, path):
        try:
            date = json.dumps(obj, indent=4, ensure_ascii=False)
            f = open(path, 'w', encoding='utf-8')
            f.write(date)
            f.close()
        except IOError as e:
            return False

    def read(self, path):
        try:
            f_obj = open(path, 'r', encoding='utf-8')
            date = json.loads(f_obj.read())
            f_obj.close()
            return date
        except IOError as e:
            return False


if __name__ == "__main__":
    t = lottery_ticket()
    t.write(t.request(url=t._url), "/Users/saseny/Desktop/1234.json")
