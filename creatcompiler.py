#coding=utf-8
#在python中正则表达式通过re库实现#################################################################
import re
import os
import operator
import openpyxl
import codecs
# 读写2007 excel
import openpyxl
#打开日志文件
def write_txt(txt, path):
    f = codecs.open(path , 'a', 'utf8')
    f.write(str(txt))
    f.close()
file = open('C:/Users/lihao/Desktop/1.sh','r', encoding='UTF-8')
for line in file.readlines():  # 依次读取每行
    line = line.strip()  # 去掉每行头尾空白
    strline = str(line)
    strlog = strline.replace(".c", ".log", 1)
    write_txt('/home/lh/gcc-4.9.3-loongson/build/gcc/cc1    -fsafe_c -fsafe_d '+ line + ' &>> '+ strlog, "C:/Users/lihao/Desktop/bzip2.sh")
    write_txt('\n', "C:/Users/lihao/Desktop/bzip2.sh")