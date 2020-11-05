#encoding:utf-8

def getFileData():
    fout = open('D:\python-workspace\ssq\dlt.txt', encoding='UTF-8')
    lines = fout.readlines()
    print(lines)

getFileData()