from typing import Dict

#count1 前区中奖个数
#count2 后区中奖个数
#no     期号
#根据前后区中奖个数，查询中奖金额，并返回中奖金额I（一二等奖返回固定金额500万和10万）
def showdlt(count1,count2,no):
    money = 0
    if count1 == 5 :
        if count2 == 2 :
            print(no+'恭喜你！喜中一等奖！奖金浮动')
            money += 5000000
        elif count2 == 1:
            print(no+'恭喜你！喜中二等奖！奖金浮动')
            money += 100000
        else:
            print(no+'喜中三等奖！奖金10000元')
            money += 10000
    elif count1 == 4 :
        if count2 == 2 :
            print(no+'喜中四等奖！奖金3000元')
            money += 3000
        elif count2 == 1:
            print(no+'喜中五等奖！奖金300元')
            money += 300
        else:
            print(no+'喜中七等奖！奖金100元')
            money += 100
    elif count1 == 3 :
        if count2 == 2 :
            print(no+'喜中六等奖！奖金200元')
            money += 200
        elif count2 == 1:
            print(no+'喜中八等奖！奖金15元')
            money += 15
        else:
            print(no+'喜中九等奖！奖金5元')
            money += 5
    elif count1 == 2:
        if count2 == 2:
            print(no+'喜中八等奖！奖金15元')
            money += 5
        elif count2 == 1:
            print(no+'喜中九等奖！奖金5元')
            money += 5
    elif count2 == 2:
        print(no+'喜中九等奖！奖金5元')
        money += 5

    return money

def showSsq(count1,count2,no):
    money = 0
    if count1 == 6 :
        if count2 == 1 :
            print(no+'恭喜你！喜中一等奖！奖金浮动')
            money += 5000000
        else:
            print(no+'恭喜你！喜中二等奖！奖金浮动')
            money += 100000
    elif count1 == 5:
        if count2 == 1:
            print(no+'喜中三等奖！奖金3000元')
            money += 3000
        else:
            print(no+'喜中四等奖！奖金200元')
            money += 200
    elif count1 == 4 :
        if count2 == 1 :
            print(no+'喜中四等奖！奖金200元')
            money += 200
        else:
            print(no+'喜中五等奖！奖金10元')
            money += 10
    elif count1 == 3 and count2 == 1:
        print(no+'喜中五等奖！奖金10元')
        money += 10
    elif count2 == 1:
        print(no+'喜中六等奖！奖金5元')
        money += 5

    return money
#根据大乐透开奖文件记录，取得开奖期号为id，开奖记录为value的数据字典
def makeDict(fileName):
    out = open(fileName, encoding='UTF-8')
    lines = out.readlines()
    read_dict = {}

    for line in lines:
        list = line.split(',')
        id = list[0]
        # print(id)
        read_dict[id] = list[1]+'+'+list[2]
    out.close()
    return read_dict

#inStr 开奖结果，格式为：1 2 3 4 5+6 7
#frontList 前区5位数字
#afterList 后区2位数字
#根据前后区数字，比对开奖结果，并返回前后区中奖个数：前期中奖个数|后区中奖个数
def comparData(instr,frontList:list,afterList:list):
    list = instr.split('+')
    list1 = list[0].split(' ')
    list2 = list[1].split(' ')
    count1 = 0
    count2 = 0
    for i in range(0,len(list1)):
        for j in range(0,len(frontList)):
            if int(frontList[j])<int(list1[i]):
                pass
            elif int(frontList[j])>int(list1[i]):
                continue
            else:
                count1 = count1 + 1
    for i in range(0, len(list2)):
        for j  in range (0,len(afterList)):
            if int(afterList[j])<int(list2[i]):
                pass
            elif int(afterList[j])>int(list2[i]):
                continue
            else:
                count2 = count2 + 1
    # print('前区中奖个数：' + str(count1))
    # print('后区中奖个数：' + str(count2))
    return str(count1)+'|' + str(count2)

def comparData(list1:list,list2:list):
    count = 0
    for i in range(0,len(list1)):
        for j in range(0,len(list2)):
            if int(list2[j])<int(list1[i]):
                pass
            elif int(list2[j])>int(list1[i]):
                continue
            elif int(list2[j])==int(list1[i]):
                count = count + 1
    return count

def isExistInfo(inStr,dlt_dict:Dict):
    if(inStr in dlt_dict.keys()):
        return True
    else:
        return False

def runDlt():
    no = '20077'
    dlt_front = [1,2,3,4,5]
    dlt_after = [6,7]
    #
    read_dict = makeDict('dlt.txt')
    print(read_dict[no])

    str = comparData(read_dict[no],dlt_front,dlt_after)
    list = str.split('|')
    showdlt(list[0],list[1],no)
    fout = open('dlt.txt',encoding='UTF-8')
    line = fout.readline()
    while line:
        list = line.split(',')
        list1 = list[1].split(' ')
        list2 = list[2].split(' ')
        count1 = 0
        count2 = 0
        for i in range(0,len(list1)):
            for j in range(0,len(dlt_front)):
                if int(dlt_front[j])<int(list1[i]):
                    pass
                elif int(dlt_front[j])>int(list1[i]):
                    continue
                else:
                    count1 = count1 + 1
        for i in range(0, len(list2)):
            for j  in range (0,len(dlt_after)):
                if int(dlt_after[j])<int(list2[i]):
                    pass
                elif int(dlt_after[j])>int(list2[i]):
                    continue
                else:
                    count2 = count2 + 1
        print(line)
        print('前区中奖个数：'+str(count1))
        print('后区中奖个数：'+str(count2))
        showdlt(count1,count2,list[0])
        line = fout.readline()

    fout.close()

