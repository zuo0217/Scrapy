#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Create time : 2018/6/3下午5:27
# Create by Saseny.Zhou
# File name: config.py

configInfo = {
    "url": "https://search.51job.com/list/070300%252C070500%252C070400%252C070800%252C071800,000000,0000,00,9,99,"
           "python,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99"
           "&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=5&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=",
    "mysql":
        {
            "ip": "127.0.0.1",
            "port": "3306",
            "username": "root",
            "password": "88670211",
            "database": "Position"
        },
    "indirect": "https://search.51job.com/list/070300%252C070500%252C070400%252C070800%252C071800,000000,0000,00,9,99,python,2,1.html",
    "city-code": "https://js.51jobcdn.com/in/js/2016/layer/area_array_c.js",
    "special name":
        {
            "030819": "高埗镇",
            "030827": "道滘镇"
        },
    "final url": "https://search.51job.com/list/{},000000,0000,00,9,99,{},2,{}.html",
    "data": "https://js.51jobcdn.com/in/js/2016/search/search_data_c.js",
    "type": "https://js.51jobcdn.com/in/js/2016/layer/indtype_array_c.js",
    "position": "https://js.51jobcdn.com/in/js/2016/layer/funtype_array_c.js",
    "url insert info":
        {
            "message": "https://search.51job.com/list/{城市},000000,0000,00,{日期},{薪水},{搜索内容},2,{页面}.html?"
                       "cotype={公司性质}&workyear={工作年限}&degreefrom={学历}&companysize={公司规模}",
            "company format":
                {
                    "所有": "99",
                    "外资(欧美)": "01",
                    "外资(非欧美)": "02",
                    "合资": "03",
                    "国企": "04",
                    "民营企业": "05",
                    "外企代表处": "06",
                    "政府机关": "07",
                    "事业单位": "08",
                    "非营利组织": "09",
                    "上市公司": "10",
                    "创业公司": "11"
                },
            "degree from":
                {
                    "所有": "99",
                    "初中及以下": "01",
                    "高中/中技/中专": "02",
                    "大专": "03",
                    "本科": "04",
                    "硕士": "05",
                    "博士": "06"
                },
            "company size":
                {
                    "所有": "99",
                    "<50": "01",
                    "50-150": "02",
                    "150-500": "03",
                    "500-1000": "04",
                    "1000-5000": "05",
                    "5000-10000": "06",
                    ">10000": "07"
                },
            "work year":
                {
                    "所有": "99",
                    "无经验": "01",
                    "1-3年": "02",
                    "3-5年": "03",
                    "5-10年": "04",
                    "10年以上": "05"
                },
            "salary":
                {
                    "all": "99",
                    "< 2000": "01",
                    "2000-3000": "02",
                    "3000-4500": "03",
                    "4500-6000": "04",
                    "6000-8000": "05",
                    "8000-10000": "06",
                    "10000-15000": "07",
                    "15000-20000": "08",
                    "20000-30000": "09",
                    "30000-40000": "10",
                    "40000-50000": "11",
                    ">50000": "12"
                },
            "date":
                {
                    "all": "9",
                    "day": "0",
                    "three day": "1",
                    "week": "2",
                    "mouth": "3",
                    "other": "4"
                }
        },
    "duplicate key": {
        "updateTime": False,
        "position": True,
        "company": True,
        "address": True,
        "salary": True,
        "positionUrl": True,
        "companyUrl": True,
        "information": False,
        "requirement": False,
        "positionInfo": False,
        "workAddress": False,
        "companyInfo": False,
        "others": False
    }
}
