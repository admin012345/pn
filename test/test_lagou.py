#!/usr/bin/python
# -*- coding:utf-8 -*-

#author:wang
"""测试用例"""
import unittest
from base.method import *
from utils.operationExcel import operationExcel
from page.lagou import *


class LaGou(unittest.TestCase):
    def setUp(self):
        self.obj = methon()
        self.a = Assert()
        self.excel = operationExcel()

    def statusCode(self, r):
        '''断言：协议状态码、业务状态码'''
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 0)

    def isContent(self, row, r):
        '''断言：内容---搜索页数15页'''
        self.assertTrue(self.a.isAssert(row=row, str2=r.text))


    def test_LaGou_001(self):
        '''拉勾网：测试翻页2'''
        r = self.obj.post(row=1)
        print(r.text)
        self.statusCode(r=r)
        # 搜索总页数15页，是否正确
        # self.assertTrue(self.a.isAssert(row=1, str2=r.text))
        # self.assertIn(self.excel.get_expect(1), r.text)
        self.isContent(row=1, r=r)

    def test_LaGou_002(self):
        '''拉勾网：测试搜索关键字'''
        r = self.obj.post1(row=1, data='开发工程师')
        # self.statusCode(r)
        # self.isContent(row=1, r=r)
        print(r.text)

    def test_LaGou_003(self):
        '''拉勾网：测试点击职位，跳转到职位详情，它们的“关联数据”为职位id'''
        r = self.obj.post1(row=2, data='开发工程师')
        print(r.text)
        print(r.url)
        list1 = []
        for i in range(0, 15):
            positionId = r.json()['content']['positionResult']['result'][i]['positionId']
            list1.append(positionId)
        # print(list1)
        writepositionId(json.dumps(list1))

    def test_LaGou_004(self):
        '''测试：职位的详细信息'''
        for i in range(15):
            r = self.obj.get(url=getpositionUrl()[i])
            print(r.url)
            print(r.text)
            print("========================")
            # 断言：期望值与实际是否相等
            dy = self.assertTrue(self.a.isAssert(row=3, str2=r.text))
            # 断言：文件写入pass或false
            self.a.isTure(row=3, duanyan=dy)


if __name__ == "__main__":
    unittest.main(verbosity=2)
