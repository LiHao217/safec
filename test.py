with open('Z:/spec2006/spec06int/gobmk/CandD_new.log', encoding='UTF-8') as f:
    for line in f:
        strnote = "note:"
        begin = 0
        noteRuleList = {}  # 未命中规则的字典
        noteRuleTemp = ""

        line = line.strip()  # 去掉每行头尾空白
        strline = str(line)
        print ("读取的数据为: %s" % (line))