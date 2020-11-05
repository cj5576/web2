import requests
from bs4 import BeautifulSoup
from typing import Dict
import searchdlt

def isExistInfo(inStr,ssq_dict:Dict):
    if(inStr in ssq_dict.keys()):
        return True
    else:
        return False

def getData(ssq_dict:Dict):
	url = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list_1.html'
	head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML,like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
	response = requests.get(url,headers=head,timeout=10)
	response.encoding = 'UTF-8'
	htm = response.text

	soup = BeautifulSoup(htm,'html.parser')

	page = int(soup.find('p',attrs={"class": "pg"}).find_all('strong')[0].text)

	url_part = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list'
	fout = open('ssq.txt','a',encoding='UTF-8')

	for i in range(1,page+1):
		url = url_part + '_' + str(i) + '.html'
		res = requests.get(url,headers=head,timeout=10)
		res.encoding = 'UTF-8'
		context = res.text
		soups = BeautifulSoup(context,'html.parser')
		if soups.table is None:
			continue
		elif soups.table:
			table_rows = soups.table.find_all('tr')
			for row_num in range(2,len(table_rows)-1):
				row_tds = table_rows[row_num].find_all('td')
				ems = row_tds[2].find_all('em')
				result = row_tds[1].string + ','+ems[0].string+' '+ems[1].string+' '+ems[2].string+' '+ems[3].string+' '+ems[4].string+' '+ems[5].string+','+ems[6].string
				if (isExistInfo(row_tds[1].string,ssq_dict)):
					print(row_tds[1].string,end=" isExist")
					print()
				else:
					print( result + '\n' )
					fout.write(result +'\n')
	fout.close()

dlt_dict = searchdlt.makeDict('ssq.txt')
getData(dlt_dict)

