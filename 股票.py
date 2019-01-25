# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 20:19:19 2019

@author: zf
"""

#导入gain_data模块
import gain_data

#喂入目标网址的地址
pa=gain_data.spider('http://quote.eastmoney.com/stocklist.html')
#设置html文本保存位置【是为了防止由于程序失误而反复爬虫】
text=pa.get_html(path='F:\\股票名称及代码.txt')
#设置目标数据匹配列表
match=['<li><a target="_blank" href="','">','</a></li> ']
#根据匹配列表规则解析出数据
data_list=gain_data.get_data(text,match)
#把解析出的数据再组装，存入数据库【这里用了excel表格】
gain_data.savedata('F:\\股票名称及代码.xls',data_list)