import os
import re
import operator
import openpyxl
import codecs
#读取目录下所有的文件名
def file_name(file_dir):   
    for root, dirs, files in os.walk(file_dir):
        print(files)
    return files

#写文件
def write_txt(txt, path):
    f = codecs.open(path, 'a', 'utf8')
    f.write(str(txt))
    f.close()

logfile = file_name("E:/实习日志/2018-7-3/bzip2/newlog")
for file in logfile:
    print(file)
    filetemp = open("E:/实习日志/2018-7-3/bzip2/newlog/"+file, 'r', encoding='UTF-8')
    print(filetemp)
    for line in filetemp.readlines():
        write_txt(line, "E:/实习日志/2018-7-3/bzip2/newlog/allnewlog.txt")
        #write_txt('\n', "E:/实习日志/2018-6-25/log/allc.txt")
#test = open('alias.log', 'r', encoding='UTF-8')
#print(test)

