import os
import re 
import requests
from urllib import request
def search_in_svn(url,filename , keyword):
	if '/../' in url:
		return 
	if url[-1] == '/':
		header = { 'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
		req = request.Request(url, headers=header)
		res = request.urlopen(req)
		htmlfile = res.read()
		sourcefile = htmlfile.decode('utf-8')
		docnames = re.findall('href="(.*)">',sourcefile)
		docnames=docnames[1:]
		if docnames==[]:
			return
		for docname in docnames:
				newurl = url+docname
				search_in_svn(newurl, filename, keyword)
	else:
		if re.findall(filename,url) == []:
			return	
		header = { 'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
		req = request.Request(url, headers=header)
		res = request.urlopen(req)
		htmlfile = res.read()
		try:
			sourcefile = htmlfile.decode('utf-8')
		except:
			print("ERROR: " + url)
		for eachline in sourcefile.split('\n'):
			findresult = re.findall(keyword,eachline)
			if findresult !=[]:
				print ('FIND IN '+url+'  :'+eachline)

f = open('weblist.txt')
file_name = 'xml'
keyword = 'VMA_5D'
urllist = f.read().split('\n')
for url in urllist:
	print(url)
	search_in_svn(url,file_name,keyword)