import os
import re
def searchfile(script_path , project_name , file_name ,keyword):
	flag_all = 0
	for root,dirs,files in os.walk(script_path + '/' + project_name + '/'):
	        for file in files:
	           if re.findall(file_name , file) != []:
	           	filepath = root +'/'+ os.path.join(file)
	           	if 'xlsx' in filepath or'.svn' in filepath or '.exe' in filepath or '.EXE' in filepath or '.asp' in filepath or '.dll' in filepath or '.zip' in filepath or 'sjl' in filepath or '.jar' in filepath:
	           		continue
	           	try:
	           		f=open(filepath , encoding = 'utf-8')
	           		content = f.read()
	           		flag = 0
	           		for eachline in content.split('\n'):
	           			if re.findall(keyword , eachline) != []:
	           				print(eachline)
	           				flag = 1
	           				flag_all = 1
	           		f.close()
	           		if flag  == 1:
	           			printpath=(root +'/'+os.path.join(file)).split('svn_search/')[1]
	           			print(printpath+"\n")
	           	except:
	           		try:
		           		f=open(filepath)
		           		content = f.read()
		           		flag = 0
		           		for eachline in content.split('\n'):
		           			if re.findall(keyword , eachline) != []:
		           				print(eachline)
		           				flag = 1
		           				flag_all = 1
		           		f.close()
		           		if flag  == 1:
		           			printpath=(root +'/'+os.path.join(file)).split('svn_search/')[1]
		           			print(printpath+"\n")
		           	except:
	           			print("WRONG:"+(root +'/'+os.path.join(file)).split('svn_search/')[1]+'\n')
	if flag_all == 0:
		print("end" , project_name+'/No Result\n')

def search_svn(url , file_name , keyword):
	script_path = os.popen('chdir').read().replace('\n',"")
	project_name = url.split('/')[-2]
	cmd = 'svn export ' + url
	if os.system(cmd) == 0:
		searchfile(script_path , project_name, file_name , keyword)
	#cmd = 'rm -rf '+ project_name
	#os.system(cmd)


f = open('list.txt')
urllist = f.read().split('\n')
file_name = '(.*)'
keyword = 'FailoverPublishRate'
for url in urllist:
	print(url)
	search_svn(url , file_name , keyword)