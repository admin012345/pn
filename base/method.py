#!/usr/bin/python
# -*- coding:utf-8 -*-

#author:wang
"""封装post请求方法"""
import requests
from page.lagou import *
from utils.excelData import *
from utils.operationExcel import operationExcel
from utils.operationJson import operationJson

# operation = operationExcel()
# def checkHeaders(row, f1=None, f2=None):
#     '''检查请求头：若请求头不一样，做判断'''
#     url = operation.get_URL(row=row)
#     list1 = url.split('/')
#     print(len(list1), list1, list1[4])
#     if list1[4] == "5396962.html":
#         return f1
#     elif list1[4] == "positionAjax.json?needAddtionalResult=false":
#         return f2


class methon:
    def __init__(self):
        self.excel = operationExcel()
        self.operationJson = operationJson()

    def post(self, row):
        try:
            r = requests.post(
                url=self.excel.get_URL(row=row),
                data=self.operationJson.getRequestData(row=row),
                headers=postHeaders())
            return r
        except Exception as e:
            raise RuntimeError("post请求接口出现未知错误")

    def post1(self, row, data):
        '''请求中包含动态参数'''
        try:
            r = requests.post(
                url=self.excel.get_URL(row=row),
                data=setso(data),
                # headers=checkHeaders(row=row,f1=getHeaders1(),f2=getHeaders2()))
                headers=postHeaders())
            return r
        except Exception as e:
            raise RuntimeError("post请求接口出现未知错误")

    def get(self, url, param=None):
        try:
            r = requests.get(url=url, params=param, headers=getHeaders())
            return r
        except Exception as e:
            raise RuntimeError("get请求接口出现未知错误")


class Assert:
    '''断言'''
    def __init__(self):
        self.excel = operationExcel()

    def isAssert(self, row, str2):
        '''判断：row是否在str2中'''
        flag = None
        if self.excel.get_expect(row=row) in str2:
            flag = True
        else:
            flag = False
        return flag

    def isTure(self, row, duanyan):
        '''判断：如果断言正确，写入pass；如果断言失败，写入failed'''
        if duanyan == True:
            self.excel.writeResult(row=row, content='Pass')
        elif duanyan == False:
            self.excel.writeResult(row=row, content='False')


# A = Assert()
# A.isTure(row=3, duanyan=True)
# r = requests.get(url="https://www.lagou.com/jobs/5073475.html", headers=getHeaders())
# print(r.text)
# # # print(r.status_code)
# # # print(type(r.text))
# print(r.url)
# # # print(r.encoding)
