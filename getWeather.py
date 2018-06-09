#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time     : 2018/6/9下午3:06
# @Author   : Saseny Zhou
# @Site     : 
# @File     : getWeather.py
# @Software : PyCharm

import requests
import json
import re
import pprint


class Weather():
    header = {"User-agent":
                  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
              }
    url_city = "http://toy1.weather.com.cn/search?cityname={}"
    weather_url = "http://d1.weather.com.cn/dingzhi/{}.html"
    real_weather = "http://d1.weather.com.cn/sk_2d/{}.html"
    referer = "http://www.weather.com.cn/weather1d/{}.shtml"
    history = "history.json"
    cityInfo = "cityInfo.json"

    def write_json(self, obj, path):
        try:
            date = json.dumps(obj, indent=4, ensure_ascii=False)
            f = open(path, 'w', encoding='utf-8')
            f.write(date)
            f.close()
        except IOError as e:
            return False

    def read_json(self, path):
        try:
            f_obj = open(path, 'r', encoding='utf-8')
            date = json.loads(f_obj.read())
            f_obj.close()
            return date
        except IOError as e:
            return False

    def getData(self, url):
        try:
            response = requests.get(url, headers=self.header)
            if response.status_code == 200:
                return True, response
            else:
                return False, response.status_code
        except:
            return False, 400

    def getCode(self, city):
        dictInfo = {}
        status = self.getData(self.url_city.format(city))
        if status[0] is True:
            text = status[1].text
            for i in text.split("\""):
                if re.findall("\d+", i):
                    tmp = i.split("~")
                    dictInfo[tmp[2]] = tmp
        totalInfo = self.read_json(self.cityInfo)
        if totalInfo is False:
            totalInfo = {}
        totalInfo[city] = dictInfo
        self.write_json(totalInfo, self.cityInfo)
        return dictInfo

    def explain(self, text, info=1):
        dictInfo = {}
        tmp = re.findall("\{(\".*?\")\}", text)
        if tmp:
            if int(info) == 1:
                tmp = [x for x in tmp[0].split("\"") if re.findall('\w+', x)][1:]
                dictInfo["count"] = len(tmp)
                for i in range(0, len(tmp), 2):
                    dictInfo[tmp[i]] = tmp[i + 1]
            else:
                tmp = [x for x in tmp[0].split("\"") if re.findall('\w+', x)]
                dictInfo["count"] = len(tmp)
                if len(tmp) % 2 != 0:
                    dictInfo["count"] = len(tmp) + 1
                    tmp.remove("limitnumber")
                    dictInfo["limitnumber"] = ""
                for i in range(0, len(tmp), 2):
                    dictInfo[tmp[i]] = tmp[i + 1]
        return dictInfo

    def getWeather(self, city):
        cityInfo = self.read_json(self.cityInfo)
        if cityInfo is False:
            cityCode = self.getCode(city)
        elif cityInfo.get(city, False) is False:
            cityCode = self.getCode(city)
        else:
            cityCode = cityInfo[city]
        if len(cityCode) != 0:
            try:
                code = cityCode[city][0]
            except:
                return False, "城市名称不正确,请确认..."
            self.header["Referer"] = self.referer.format(code)
            weather = self.getData(self.weather_url.format(code))
            real_weather = self.getData(self.real_weather.format(code))
            if weather[0] is True and real_weather[0] is True:
                weather = str(weather[1].text.encode(weather[1].encoding), "utf-8")
                real_weather = str(real_weather[1].text.encode(real_weather[1].encoding), "utf-8")
                history = self.read_json(self.history)
                weather = self.explain(weather, info=1)
                
                real_weather = self.explain(real_weather, info=2)
                if history is not False:
                    if history.get(city, False) is False:
                        history[city] = [{"天气情况": weather, "实时天气": real_weather}]
                    else:
                        history[city].append({"天气情况": weather, "实时天气": real_weather})
                else:
                    history = {}
                    history[city] = [{"天气情况": weather, "实时天气": real_weather}]
                self.write_json(history, self.history)
                return True, {"天气情况": weather, "实时天气": real_weather}
        else:
            return False, "城市名称不正确,请确认..."


if __name__ == "__main__":
    t = Weather()
    cityName = input("请输入要查询的城市名称 如:(苏州 | 南京 | 上海) 仅支持单个城市查询!\n->>")
    info = t.getWeather(cityName)
    pprint.pprint(info)
