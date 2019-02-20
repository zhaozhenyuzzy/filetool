# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 10:00:10 2019

@author: thor
把一个文件分步读入，每次读取8096 4K字节，计算MD5值
read one file while get 8096 bytes each time, to calculate the MD5 value.
"""

# coding=gbk
import datetime
import hashlib
import os

def GetFileMd5(filename):
    if not os.path.isfile(filename):
        raise Exception("The path is not a file. Please check.")
    hashValue = hashlib.md5()
    f = open(filename,'rb')
    while True:
        block = f.read(8096)
        if not block:
            break
        hashValue.update(block)
    f.close()
    return hashValue.hexdigest()

filepath = input('请输入文件路径：')

# 输出文件的md5值以及记录运行时间
starttime = datetime.datetime.now()

try:
    value = GetFileMd5(filepath)
except Exception as e:
    print(e)
    exit()
print("文件的MD5值是：")
print(value)
endtime = datetime.datetime.now()
print('运行时间：%ds'%((endtime-starttime).seconds))
