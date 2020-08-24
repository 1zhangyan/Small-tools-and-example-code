#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
import csv

csv_file = open('followdata2.csv','w' , newline = '')
writer = csv.writer(csv_file)
searchuserlist = ['32820037','41273726','82385070']

#writer.writerow()

#url ='https://api.bilibili.com/x/relation/followings?vmid=32820037&pn=1&ps=50&order=desc'
#url = 'https://api.bilibili.com/x/relation/followings?vmid=62397974&pn=2&ps=20&order=desc'
count = 0;

for eachuserid in searchuserlist:
	templist = []
	templist.append(eachuserid+"的关注列表")
	writer.writerow(templist)
	templist = []
	templist = ['用户名','用户id','头像','用户主页']
	writer.writerow(templist)
	for i in range(6):
		if i == 0:
			continue
		url = 'https://api.bilibili.com/x/relation/followings?vmid=' + eachuserid + '&pn='+str(i)+'&ps=50&order=desc'
		response = requests.get(url)
		response.encoding ='utf-8'
		html = response.text
		newhtml = j = json.loads(html)
		list = []
		list = newhtml['data']['list']
		if list == []:
			break
		print(i)
		for usermeta in list:
			templist = []
			templist.append(str(usermeta['uname']))
			templist.append(str(usermeta['mid']))
			templist.append(usermeta['face'])
			templist.append('https://space.bilibili.com/'+str(usermeta['mid']))
			writer.writerow(templist)
			templist = []
csv_file.close()