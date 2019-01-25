# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 22:13:20 2019

@author: zf
"""

#导入gain_data模块
import gain_data

#喂入目标网址的地址
pa=gain_data.spider('https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=1796886266,3045319124&fm=173&s=8CE27A22862635156198D10B0100E091&w=640&h=656&img.JPEG')
#设置文件保存位置
pa.get_content(path='F:\\二哈.jpg')