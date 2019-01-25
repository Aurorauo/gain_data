# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 10:30:46 2019
@author: zf
"""

import requests
import time
import random
import re
from xlutils.copy import copy
import xlwt
import xlrd
import os

'''获取网页数据'''
class spider:
    
    """初始化，设预值"""
    def __init__(self,url,timeout=5,sleeptime=0,**kwargs):
        self.url=url
        self.timeout=timeout
        try:
            self.headers=kwargs["headers"]
        except:
            self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
        try:
            self.sleeptime=random.randint(int(kwargs["sleeptime"][0]),int(kwargs["sleeptime"][0]))
        except:
            self.sleeptime=sleeptime
        
    """获取网页html文本，可以选择将文本保存为txt文件，返回值有两种模式可供选择"""
    def get_html(self,html='1',write='w',**kwargs):
        try:
            time.sleep(self.sleeptime)
            req=requests.get(self.url,headers=self.headers,timeout=self.timeout)
            try:
                req.encoding=kwargs["encoding"]
            except:
                req.encoding=req.apparent_encoding
            text=req.text
            try:
                if kwargs["path"]:
                    with open(kwargs["path"],write) as f:
                        f.write(text)
                        f.close()
            except:
                pass
            if str(html)=='1':
                return text
            else:
                return text.replace('\n','').replace('\t','').replace('\r','').replace(' ','')
        except:
            return ''
            
    """返回网页内容{例如图片，视频等数据}，可选择保存为txt文件"""
    def get_content(self,write='wb',**kwargs):
        try:
            time.sleep(self.sleeptime)
            req=requests.get(self.url,headers=self.headers,timeout=self.timeout)
            req.encoding=req.apparent_encoding
            try:
                if kwargs["path"]:
                    with open(kwargs["path"]+kwargs["name"],write) as f:
                        f.write(req.content)
                        f.close()
            except:
                pass
            return req.content
        except:
            return ''

'''通过正则表达式来解析出想到得到的数据，返回值为得到的数据列表'''
def get_data(text,match,mode='0'):   #text为待解析字符串，match列表中存放待解析字符串前后模范字符串
    try:
        pattern=''
        if mode!='0':
            n=1
            for i in match:
                if n%2:
                    pattern=pattern+str(i)+'(.*?)'
                else:
                    pattern=pattern+str(i)+'.*?'
                n=n+1
            pattern=pattern[:-3]
        else:
            for i in match:
                pattern=pattern+str(i)+'(.*?)'
            pattern=pattern[:-5]
        print(pattern)
        data=re.compile(pattern).findall(text.replace('\n','').replace('\t','').replace('\r',''))
        if mode!='0':
            return [data,int(len(match)/2.0)]
        else:
            return [data,len(match)]
    except:
        return []
    
'''保存数据函数，将数据保存到excel表格中'''
def savedata(path,data_list,):   #path 为数据保存路径；data_list为保存数据输入列表
    try:
        if not(os.path.exists(path)):
            w=xlwt.Workbook()
            sheet =w.add_sheet("爬取到的数据")
            num=0
            tuple_length=int(data_list[-1])-1
            for i in data_list[0]:
                for j in range(tuple_length):
                    sheet.write(num,j,str(i[j]))
                num=num+1
            w.save(path)
        else:
            old = xlrd.open_workbook(path,formatting_info=True)
            new = copy(old)
            news = new.get_sheet(0)
            sheet_data=old.sheet_by_index(0)
            num=sheet_data.nrows
            tuple_length=int(data_list[-1])-1
            for i in data_list[0]:
                for j in range(tuple_length):
                    news.write(num,j,str(i[j]))
                num=num+1
            new.save(path)
    except:
        pass
