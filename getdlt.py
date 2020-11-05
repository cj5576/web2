import requests
from bs4 import BeautifulSoup
import searchdlt
from typing import Dict

def isExistInfo(inStr,dlt_dict:Dict):
    if(inStr in dlt_dict.keys()):
        return True
    else:
        return False

def getData(dlt_dict:Dict):
    url = 'http://zst.sina.aicai.com/dlt/'
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML,like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    response = requests.get(url,headers=head,timeout=10)
    response.encoding = 'UTF-8'
    htm = response.text
    soup = BeautifulSoup(htm,'html.parser')
    numbers = soup.find( 'tbody' ).find_all( attrs={'class': 'c_fbf5e3 bd_rt_a'} )
    print(numbers[0].text)
    fonts = soup.find( 'tbody' ).find_all( attrs={'class': 'chartBall01'} )
    afters = soup.find( 'tbody' ).find_all( attrs={'class': 'chartBall02'} )
    fout = open( 'dlt.txt', 'a+', encoding='UTF-8' )
    result = ''
    for i in range( 0, len(numbers) ):
        result = numbers[i].text + ',' + fonts[i * 5].text + ' ' + fonts[i * 5 + 1].text + ' ' + fonts[i * 5 + 2].text + ' ' + fonts[
            i * 5 + 3].text + ' ' + fonts[i * 5 + 4].text + ',' + afters[i * 2].text + ' ' + afters[i * 2 + 1].text
        print( result )
        if (isExistInfo( numbers[i].text, dlt_dict )):
            print( result, end=" isExist" )
            print()
        else:
            fout.write( result + '\n' )
    fout.close()
    # page = len(soup.find('select').find_all('option'))
    # # print('总页数：' + str(len(soup.find('select').find_all('option'))))
    #
    # url_part = 'https://www.lottery.gov.cn/kj/kjlb.html?dlt'
    # fout = open('dlt.txt','a+',encoding='UTF-8')
    # for i in range(1,page+1):
    #     url = url_part + '_' + str(i) + '.jspx?_ltype=dlt'
    #     res = requests.get(url, headers=head, timeout=10)
    #     soups = BeautifulSoup(res.text, 'html.parser')
    #     table_rows = soups.table.find_all('tr')
    #     for row_num in range(2, len(table_rows)):
    #         row_tds = table_rows[row_num].find_all('td')
    #         result = row_tds[0].text+','+ row_tds[1].text+' ' + row_tds[2].text+' ' + row_tds[3].text+' ' + row_tds[4].text+' ' + row_tds[5].text+',' + row_tds[6].text+' ' + row_tds[7].text
    #         # print(result)
    #         if(isExistInfo(row_tds[0].text,dlt_dict)):
    #             print(result, end=" isExist")
    #             print()
    #         else:
    #             fout.write(result + '\n')
    # fout.close()

dlt_dict = searchdlt.makeDict('dlt.txt')
getData(dlt_dict)