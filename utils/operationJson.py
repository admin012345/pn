#!/usr/bin/python
# -*- coding:utf-8 -*-
#author:wang
"""读取requestData.json文件中的请求参数"""
from utils.public import *
import json
from utils.operationExcel import operationExcel


class operationJson:
    def __init__(self):
        '''实例化对象，调用requestData方法'''
        self.excel = operationExcel()

    def getReadJson(self):
        '''读取json文件'''
        with open(base_dir(filename='requestData.json'), encoding='utf-8') as fp:
            data = json.load(fp)
            return data

    def getRequestData(self, row):
        '''1、文件中value值get_Json_Data
           2、将json、Excel更加请求数据的“login_001”连接起来getRequestData
           3、请求数据为“字典”，转化为“str”字符串json.dumps()
           4、ensure_ascii=False，编码为utf-8
        '''
        return json.dumps(self.getReadJson()[self.excel.get_requestData(row=row)])


# o = operationJson()
# # print(o.getReadJson())
# # print(o.get_Json_Data('login_001'))
# print(o.getRequestData(1), type(o.getRequestData(1)))
