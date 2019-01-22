#!/usr/bin/python
# -*- coding:utf-8 -*-
#author:wang
"""excel文件的读取、写入"""
import xlrd
from xlutils.copy import copy
from utils.public import *
from utils.excelData import *


class operationExcel:
    def getExcel(self):
        '''定位Excel表'''
        db = xlrd.open_workbook(base_dir("data", "Data.xls"))
        sheet = db.sheet_by_index(0)
        return sheet

    def get_row(self):
        '''获取Excel的行数'''
        return self.getExcel().nrows

    def get_cell(self, rowx, colx):
        '''获取Excel的单元格内容'''
        return self.getExcel().cell_value(rowx, colx)

    def get_caseID(self, row):
        '''获取caseID这一列'''
        return self.get_cell(row, getCaseID())

    def get_title(self, row):
        '''获取title这一列'''
        return self.get_cell(row, getTitle())

    def get_URL(self, row):
        '''获取URL这一列'''
        return self.get_cell(row, getURL())

    def get_requestData(self, row):
        '''requestData'''
        return self.get_cell(row, getRequestData())

    def get_expect(self, row):
        '''获取expect这一列'''
        return self.get_cell(row, getExpect())

    def get_result(self, row):
        '''获取result这一列'''
        return self.get_cell(row, getResult())

    def writeResult(self, row, content):
        '''
        把结果写入data表的result列中
        【注意】将文件提前复制一份，以防在写入时报错
        '''
        col = getResult()
        work = xlrd.open_workbook(base_dir("data", "Data.xls"))
        old_content = copy(work)
        ws = old_content.get_sheet(0)
        ws.write(row, col, content)
        old_content.save(base_dir("data", "Data.xls"))

    def get_success(self):
        '''获取成功的个数'''
        count_success = []
        count_false = None
        for i in range(1, self.get_row()):
            if self.get_result(i) == 'Pass':
                count_success.append(self.get_result(i))
        # print(len(count_success))
        return int(len(count_success))

    def get_false(self):
        '''获取失败的个数:失败个数=总数-成功个数'''
        # print((self.get_row()-1)-self.get_success())
        return (self.get_row()-1)-self.get_success()

    def get_pass_rate(self):
        '''通过率=成功个数/总个数*100'''
        rate = ''
        if self.get_false() == 0:
            rate = '100%'
        elif self.get_false() !=0:
            rate = str(int(self.get_success()/(self.get_row()-1)*100))+'%'
        print(rate)





# operation = operationExcel()
# #  print(operation.get_requestData(1))
# # print(operation.get_expect(1))
# # operation.writeResult(row=4, content='pass')
# operation.get_pass_rate()

