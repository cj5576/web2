#encoding:utf-8
import schedule,getssq,searchdlt,getdlt,datetime

def getLotteryInfo():
    getssq.getData(searchdlt.makeDict( 'ssq.txt' ))
    getdlt.getData(searchdlt.makeDict( 'dlt.txt' ))

def getNowTimes():
    print(datetime.datetime.now())

def taskList():
    schedule.clear()
    schedule.every(1).hours.do(getLotteryInfo)
    while(True):
        schedule.run_pending()
taskList()
# getNowTimes()