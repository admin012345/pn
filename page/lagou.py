#!/usr/bin/python
# -*- coding:utf-8 -*-

#author:wang
"""重写json文件的数据
动态参数处理：
    1、搜索的请求数据不同，如“自动化测试”、“开发工程师”，面向对象化解决
"""

from utils.operationJson import operationJson
from utils.operationExcel import operationExcel
import json
from utils.public import *


oj = operationJson()
excel = operationExcel()
def setso(kd=None):
    '''搜索关键字：给kd赋不同的值'''
    dic = json.loads(oj.getRequestData(row=2))
    dic['kd'] = kd
    return dic


def writepositionId(content):
    '''职位id写入文件'''
    with open(base_dir(filename="positionId"), 'w') as f:
        f.write(content)


def getpositionId():
    '''读取写入文件的positionId'''
    with open(base_dir(filename="positionId"), 'r') as f:
        return json.loads(f.read())


def setpositionId(row):
    '''关联数据==职位id：获取某一id'''
    dic = json.loads(oj.getRequestData(row=row))
    dic['positionId'] = getpositionId()
    return dic


def getpositionUrl():
    '''获取职位id的url：由于每个职位详情的url不同'''
    # positionUrl = excel.get_URL(2)
    list1 = []
    for item in getpositionId():
        positionUrl = "https://www.lagou.com/jobs/{0}.html".format(item)
        # print(positionUrl)
        list1.append(positionUrl)
    return list1



print(getpositionId())
# setpositionId(3)
# setso("看法工程")
# setpositionId(11111)