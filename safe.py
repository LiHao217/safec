#coding=utf-8
#在python中正则表达式通过re库实现#################################################################
import re
import os
import operator
# 读写2007 excel
import openpyxl
def rulecount(filepath) :
    #打开日志文件
    file = open(filepath,'r', encoding='UTF-8')
    print ("file name is: ", file.name)
    #strfile = str(file.read())

    #print(strfile.count(str1, 0,len(strfile)))#统计字符串的数量
    #############################统计命中的规则的名字以及数量####################
    strerror = "error: Rule"
    begin = 0
    errorRuleList = {}#命中规则的字典
    errorRuleTemp = ""
    for line in file.readlines():                          #依次读取每行
        line = line.strip()#去掉每行头尾空白
        strline = str(line)
        #print ("读取的数据为: %s" % (line))
        errorbegin = strline.find(strerror,begin,len(strline))#寻找error的起始位置
        if errorbegin >= 0:
            errorRule = strline[errorbegin+7:errorbegin+20]#errorRule的规则名字
            errorRule = errorRule.strip()  # 去掉头尾空白
            #print(errorRule)
            errorRuleTemp = errorRuleTemp + errorRule
            if errorRule not in errorRuleList:
                errorRuleList[errorRule] = 1#没有的规则名字，加入列表

    for errorRule in errorRuleList.keys():
        errorRuleList[errorRule] = errorRuleTemp.count(errorRule, 0, len(errorRuleTemp))
    print('error：')
    print(errorRuleList)
    file.close()
    #print(errorRuleTemp)
    #############################统计warning的规则的名字以及数量####################
    file = open(filepath,'r', encoding='UTF-8')
    strwarning = "warning:"
    begin = 0
    warningRuleList = {}#未命中规则的字典
    warningRuleTemp = ""
    for line in file.readlines():                          #依次读取每行
        line = line.strip()#去掉每行头尾空白
        strline = str(line)
        #print ("读取的数据为: %s" % (line))
        warningbegin = strline.find(strwarning,begin,len(strline))#寻找warning的起始位置
        if warningbegin >= 0:
            warningRule = strline[warningbegin+9:warningbegin+22]#warningRule的规则名字
            #print(warningRule)
            warningRule = warningRule.strip()  # 去掉头尾空白
            warningRuleTemp = warningRuleTemp + warningRule
            if warningRule not in warningRuleList:
                warningRuleList[warningRule] = 1#没有的规则名字，加入列表

    for warningRule in warningRuleList.keys():
        warningRuleList[warningRule] = warningRuleTemp.count(warningRule, 0, len(warningRuleTemp))
    print('warning：')
    print(warningRuleList)
    #print(warningRuleTemp)
    #############################统计未命中的规则的名字以及数量####################
    file = open(filepath,'r', encoding='UTF-8')
    strnote = "note:"
    begin = 0
    noteRuleList = {}#未命中规则的字典
    noteRuleTemp = ""
    for line in file.readlines():                          #依次读取每行
        line = line.strip()#去掉每行头尾空白
        strline = str(line)
        #print ("读取的数据为: %s" % (line))
        notebegin = strline.find(strnote,begin,len(strline))#寻找note的起始位置
        if notebegin >= 0:
            noteRule = strline[notebegin+5:notebegin+24]#noteRule的规则名字
            noteRule = noteRule.strip()  # 去掉头尾空白
            #print(noteRule)
            noteRuleTemp = noteRuleTemp + noteRule
            if noteRule not in noteRuleList:
                noteRuleList[noteRule] = 1#没有的规则名字，加入列表

    for noteRule in noteRuleList.keys():
        noteRuleList[noteRule] = noteRuleTemp.count(noteRule, 0, len(noteRuleTemp))
    print('allnote：')
    print(noteRuleList)
    #############################统计willcheck的规则的名字以及数量####################
    file = open(filepath,'r', encoding='UTF-8')
    strnote = "note:"
    begin = 0
    noteRuleList = {}#未命中规则的字典
    noteRuleTemp = ""
    for line in file.readlines():                          #依次读取每行
        line = line.strip()#去掉每行头尾空白
        strline = str(line)
        #print ("读取的数据为: %s" % (line))
        notebegin = strline.find(strnote,begin,len(strline))#寻找note的起始位置
        if notebegin >= 0:
            noteRule = strline[notebegin+6:notebegin+24]#noteRule的规则名字
            noteRule = noteRule.strip()#去掉头尾空白
            noteRule = noteRule.replace("willCheck", "Rule", 1)#willCheck转rule
            #print(noteRule)
            noteRuleTemp = noteRuleTemp + noteRule
            if noteRule not in noteRuleList :
                if 'Rule' in str(noteRule):
                    #print(noteRule)
                    noteRuleList[noteRule] = 1#没有的规则名字，加入列表

    for noteRule in noteRuleList.keys():
        #print(noteRule)
        noteRuleList[noteRule] = noteRuleTemp.count(noteRule, 0, len(noteRuleTemp))#统计每条规则的数量

    print('willcheack：')
    print(noteRuleList)

##################统计#########
    Rulenum = len(errorRuleList) + len(warningRuleList) + len(noteRuleList) #所有规则的数量
    print("Rule number is:",Rulenum)
    Rulecount = [[0 for i in  range(4)] for i in range(Rulenum)] #统计所有规则的二维数组
    i=0
    for key in errorRuleList.keys():#统计error的规则
        if key not in Rulecount:
            Rulecount[i][0] = key
            Rulecount[i][1] = errorRuleList[key]
            i = i + 1
        else :
            print("error：Rule has exit")
    for key in warningRuleList.keys():#统计warning的规则
        if key not in Rulecount:
            Rulecount[i][0] = key
            Rulecount[i][2] = warningRuleList[key]
            i = i + 1
        else :
            Rulecount[Rulecount.index(key)][2] = warningRuleList[key]
            print("error：Rule has exit")
    Rulecount_index = -1#已存在规则的位置
    Rulecount_exist = 0#规则是否存在
    for key in noteRuleList.keys():#统计note的规则
        #if key not in errorRuleList:
        for j in range(0, len(Rulecount)):
            if key in Rulecount[j]:#判断这条规则是否已经存在
                print(key,"is exist")
                Rulecount_exist = 1#规则存在
                Rulecount_index = j#已存在规则的位置
                print("key's index is",j)
        if Rulecount_exist == 1:
            Rulecount[Rulecount_index][3] = noteRuleList[key]
            print("Rule has exit：", key)
        else :
            Rulecount[i][0] = key
            print(key)
            Rulecount[i][3] = noteRuleList[key]
            i = i + 1
        Rulecount_exist = 0#检查规则是否存在的开关置0
            #print(key)
            #Rulecount[Rulecount.index(key)][2] = noteRuleList[key]
    Rulecount = sorted(Rulecount, key=lambda x:x[1] ,reverse=True)#排序

    print(Rulecount)
    print("rule number is" , len(Rulecount))
    path = 'Rulecount20.xlsx'
    write07Excel(path, Rulecount)
###############rulecount结束#################################################


###################################统计结果写入excel表格#####################
def write07Excel(path,list):
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = '统计结果'

    value = [["规则名称", "error", "warning", "note"]]#表头名字
    value = value + list#合并数据，list为表中数据
    for i in range(0, len(value)):
        for j in range(0, len(value[i])):
            sheet.cell(row=i+1, column=j+1, value=str(value[i][j]))#写入数据
    wb.save(path)
    #print(value[1])
    print("写入数据成功！")
###########################################################################
#输入日志路径
rulecount('Z:/spec2006/spec06int/gcc/gcc2.log')
