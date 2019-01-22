#!/usr/bin/python
# -*- coding:utf-8 -*-
#author:wang
"""获取excel的列的数据"""


class excelVariable:
    caseID = 0
    title = 1
    URL = 2
    requestData = 3
    expect = 4
    result = 5


def getCaseID():
    return excelVariable.caseID


def getTitle():
    return excelVariable.title


def getURL():
    return excelVariable.URL


def getRequestData():
    return excelVariable.requestData


def getExpect():
    return excelVariable.expect


def getResult():
    return excelVariable.result


def postHeaders():
    '''获取post请求头信息'''
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': '_ga=GA1.2.1143653235.1545960525; user_trace_token=20181228092842-e92a301b-0a3f-11e9-ad84-5254005c3644; LGUID=20181228092842-e92a339c-0a3f-11e9-ad84-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; WEBTJ-ID=20190109133008-1683116df1b450-00407d48dfd108-323b5b03-1049088-1683116df1d388; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1546419454,1546419529,1546568474,1547011810; _gid=GA1.2.1147851451.1547011810; JSESSIONID=ABAAABAAAIAACBI54D085DD997BE225709A5167C57657C5; _qddaz=QD.kpzoil.dua8fk.jqpz25i0; X_MIDDLE_TOKEN=49484def62577082a7f35a45da276f4c; _gat=1; PRE_HOST=; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221683643a8d76-0c8011d5fbda9c-323b5b03-1049088-1683643a8d81d7%22%2C%22%24device_id%22%3A%221683643a8d76-0c8011d5fbda9c-323b5b03-1049088-1683643a8d81d7%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; LGSID=20190110133823-f2303beb-1499-11e9-940a-525400f775ce; PRE_UTM=m_cf_cpt_baidu_pc; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpt_baidu_pc; TG-TRACK-CODE=index_search; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1547099023; LGRID=20190110134340-af38054f-149a-11e9-b2eb-5254005c3644; SEARCH_ID=8b786dc9ab214ec7a8c82dab49bb331c',
        'Referer': 'https://www.lagou.com/jobs/list_%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95?labelWords=&fromSearch=true&suginput=',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    return headers

def getHeaders():
    '''获取get请求头信息'''
    headers = {
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'Cookie': '_ga=GA1.2.1143653235.1545960525; user_trace_token=20181228092842-e92a301b-0a3f-11e9-ad84-5254005c3644; LGUID=20181228092842-e92a339c-0a3f-11e9-ad84-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; WEBTJ-ID=20190109133008-1683116df1b450-00407d48dfd108-323b5b03-1049088-1683116df1d388; _gat=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1546419454,1546419529,1546568474,1547011810; _gid=GA1.2.1147851451.1547011810; LGSID=20190109133010-a1e98f63-13cf-11e9-8b98-525400f775ce; PRE_UTM=m_cf_cpt_baidu_pc; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpt_baidu_pc; JSESSIONID=ABAAABAAAIAACBI54D085DD997BE225709A5167C57657C5; SEARCH_ID=9ead45ec759c4b828ad818eca1a059d6; TG-TRACK-CODE=search_code; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1547011968; LGRID=20190109133248-001588a4-13d0-11e9-b2c8-5254005c3644',
        'Referer': 'https://www.lagou.com/jobs/list_%E5%BC%80%E5%8F%91%E5%B7%A5%E7%A8%8B%E5%B8%88?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput='}
    return headers

# print(getCaseID())
