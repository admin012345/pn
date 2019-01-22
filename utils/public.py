#!/usr/bin/python
# -*- coding:utf-8 -*-
#author:wang

"""Excel文件目录"""
import os


def base_dir(package='data', filename=None):
    '''获取文件路径'''
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), package, filename)


# print(base_dir(filename='requestData.json'))