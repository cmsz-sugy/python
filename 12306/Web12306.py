#coding=utf-8
import requests
import argparse
import datetime
import re
from prettytable import PrettyTable
now = datetime.datetime.now()

# 禁用安全请求警告
requests.packages.urllib3.disable_warnings()
tomorrow = now+datetime.timedelta(days=2)
tomorrow = tomorrow.strftime('%Y-%m-%d')
print tomorrow

argument = argparse.ArgumentParser()
argument.add_argument('--fromcity','-f',default='beijing|')
argument.add_argument('--tocity','-t',default='xiamen')
argument.add_argument('--date','-d',default=tomorrow)
# argument.add_argument('-d',action='store_true')
args =argument.parse_args()

from_station =  args.fromcity
to_station = args.tocity
Date = args.date

stationlist_url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js'
r = requests.get(stationlist_url, verify=False)
stationlist = r.content

ToStation = ''
FromStation =''

placea = stationlist.find(from_station)
placeb = stationlist.find(to_station)

for i in range(-4,-1):
	FromStation += stationlist[placea+i]
for i in range(-4,-1):
	ToStation += stationlist[placeb+i]

query_url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date='+Date+'&leftTicketDTO.from_station='+FromStation+'&leftTicketDTO.to_station='+ToStation+'&purpose_codes=ADULT'
r = requests.get(query_url,verify=False)


with open('json.txt','w') as fp:
	 fp.write(str(r.json()))


if 'result' in r.json()["data"]:
	rj = r.json()["data"]["result"]
	result_map= r.json()["data"]['map']
	pt = PrettyTable()



	header = '车次 车站 到站时间 时长 一等座 二等座 软卧 硬卧 硬座 无座'.split()
	pt._set_field_names(header)

	for x in rj:
		vertical = x.find('|')
		length = len(x)
		train = x[vertical + 1:length]
		while vertical!=-1:
			vertical = train.find('|')
			if vertical== 0:
				train = train[vertical + 1:length]
				continue
			if vertical == -1:break
			print train[0:vertical]
			length = len(x)
			train = train[vertical+1:length]
   		print "====================================="
else :
	print '这两个站点没有直达列车'