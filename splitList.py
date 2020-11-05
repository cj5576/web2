from typing import Dict
import itertools
import searchdlt

capStr = 'ABCDEFGHIJKLMNOPQRSTUVWXWZ!@#$%^&*='
lowerStr = 'abcdefghijklmnopqrstuvwxwz'

#count 复式投注个数
#type  类型：0-大乐透前区；1-大乐透后区；2-双色球红球；3-双色球蓝球
def combinationStr(count,type):
    str1 = ''
    j = 0
    if type == 0:
        j = 5
    elif type == 1:
        j = 2
    elif type == 2:
        j = 6
    else:
        j = 1

    for i in itertools.combinations(capStr[0:count], j):
        str1 = str1 + ','.join(i) + '|'
    return str1

def cartesianProduct(str1,str2,splitStr):
    list1 = str1[0:len(str1)-1].split(splitStr)
    ss = ''
    # for i in list1:
    #     print(i)
    list2 = str2[0:len(str2)-1].split(splitStr)
    # for i in list2:
    #     print(i)
    list = itertools.product(list1,list2)
    for i in list:
        ss = ss + '+'.join(i) + '|'
    return ss

def replaceString(oldStr,newStr,replaceStr):
    return replaceStr.replace(oldStr,newStr)

def isExistInfo(inStr,dlt_dict:Dict):
    if(inStr in dlt_dict.keys()):
        return True
    else:
        return False

def returnList(frontStr = '2,4,11,20,23,25,28',afterStr = '1,11,12'):
    frontList = frontStr.split(',')
    afterList = afterStr.split(',')

    returnStr = '一共'

    replaceStr = cartesianProduct(combinationStr(len(frontList),0),combinationStr(len(afterList),1).lower(),'|')
    # print(replaceStr)
    for i in range(0,len(frontList)):
        replaceStr = replaceString(capStr[i],frontList[i],replaceStr)

    for j in range(0,len(afterList)):
        replaceStr = replaceString(lowerStr[j],afterList[j],replaceStr)

    list = replaceStr[0:len(replaceStr)-1].split('|')
    returnStr = returnStr + str(len(list)*2) + '元<br>'
    for i in list:
        returnStr = returnStr + i + '<br>'

    return returnStr


def runDlt(frontStr = '2,4,11,20,23,25,28',afterStr = '1,11,12',no = '20081'):
    frontList = frontStr.split(',')
    afterList = afterStr.split(',')

    moneys = 0

    replaceStr = cartesianProduct(combinationStr(len(frontList),0),combinationStr(len(afterList),1).lower(),'|')
    # print(replaceStr)
    for i in range(0,len(frontList)):
        replaceStr = replaceString(capStr[i],frontList[i],replaceStr)

    for j in range(0,len(afterList)):
        replaceStr = replaceString(lowerStr[j],afterList[j],replaceStr)

    # print(replaceStr)
    read_dict = searchdlt.makeDict('dlt.txt')
    if(isExistInfo(no,read_dict)):
        retStr = ''
        inStr = read_dict[no]
        inStrList = inStr.split('+')
        frontList = inStrList[0].split(' ')
        afterList = inStrList[1].split(' ')
        # print(read_dict[no])
        list = replaceStr[0:len(replaceStr)-1].split('|')
        for i in list:
            # print(i)
            lists = i.split('+')
            list1 = lists[0].split(',')
            list2 = lists[1].split(',')
            # ll = searchdlt.comparData(inStr, list1, list2).split('|')
            # print(ll)
            moneys += searchdlt.showdlt(searchdlt.comparData(frontList,list1), searchdlt.comparData(afterList,list2), no)

        retStr = '前区：' + frontStr + '后区：' + afterStr + '的中奖总金额为：' + str(moneys) + '元'
    else:
        retStr = '开奖记录不存在！'
    return retStr

def returnList2(frontStr = '2,4,11,18,20,23,25,28',afterStr = '1,16'):
    frontList = frontStr.split(',')
    afterList = afterStr.split(',')

    returnStr = '一共'

    replaceStr = cartesianProduct(combinationStr(len(frontList), 2), combinationStr(len(afterList), 3).lower(), '|')
    # print(replaceStr)
    for i in range(0, len(frontList)):
        replaceStr = replaceString(capStr[i], frontList[i], replaceStr)

    for j in range(0, len(afterList)):
        replaceStr = replaceString(lowerStr[j], afterList[j], replaceStr)

    list = replaceStr[0:len( replaceStr ) - 1].split( '|' )

    returnStr = returnStr + str(len(list)*2) + '元<br>'
    for i in list:
        returnStr = returnStr + i + '<br>'

    return returnStr

def runSsq(frontStr = '2,4,11,18,20,23,25,28',afterStr = '1,16',no = '2020081'):
    frontList = frontStr.split(',')
    afterList = afterStr.split(',')

    moneys: int = 0

    replaceStr = cartesianProduct(combinationStr(len(frontList), 2), combinationStr(len(afterList), 3).lower(), '|')
    # print(replaceStr)
    for i in range(0, len(frontList)):
        replaceStr = replaceString(capStr[i], frontList[i], replaceStr)

    for j in range(0, len(afterList)):
        replaceStr = replaceString(lowerStr[j], afterList[j], replaceStr)

    # print(replaceStr)
    read_dict = searchdlt.makeDict('ssq.txt')
    if (isExistInfo(no, read_dict)):
        inStr = read_dict[no]
        # print("双色球"+no+"开奖号码："+inStr)
        inStrList = inStr.split('+')
        frontOpenList = inStrList[0].split(' ')
        afterOpenList = [inStrList[1]]
        # for k in frontOpenList:
        #     print("前区开奖号码："+k)
        # for l in afterOpenList:
        #     print("后区开奖号码："+l)
        # print(read_dict[no],end=' 开奖记录')
        # print()
        list = replaceStr[0:len(replaceStr) - 1].split('|')
        for i in list:
            # print("购买彩票记录："+i)
            lists = i.split('+')
            list1 = lists[0].split(',')
            list2 = lists[1].split(',')
            # ll = searchdlt.comparData(inStr, list1, list2).split('|')
            # print(ll)
            l1 = searchdlt.comparData(frontOpenList, list1)
            l2 = searchdlt.comparData(afterOpenList, list2)
            # print(l1)
            # print(l2)
            moneys += searchdlt.showSsq(l1, l2, no)

        return '红球：' + frontStr + '蓝球：' + afterStr + '的中奖总金额为：' + str( moneys ) + '元'

    else:
        return '开奖记录不存在！'

# runSsq()
# runDlt()