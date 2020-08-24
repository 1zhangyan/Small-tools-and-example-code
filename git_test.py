import re
filelist = open("list.txt","r")
ProjectPath_list=filelist.read().split('\n')
for eachpath in ProjectPath_list:
	print(eachpath.split('/')[-1].split('.git')[0])