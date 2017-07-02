#coding:utf-8
import os
import re
os.chdir("R:\\")        #设置读取路径
li = os.listdir("R:\\") #遍历目录下文件

##################################################################

# for name in li:
	# if re.findall("[*.*]",name): #只要文件不要文件夹
		# fp = open(name,'r')      #读内容
		# print "========================================="
		# print "----",name,"-----------------------------"
		# print fp.read()
		# fp.close()
	# else:
		# print "========================================="
		# print "\""+name+"\"  is a dir."

##################################################################		

fw = 'fw.txt'
fp = open(fw,'w')  #清空文件内容并写入新内容，文件不存在则自动创建
fp.write('write something.\n')

fp = open(fw,'a')  #追加内容
fp.write('add users:\n')
fp.write("%10s\t %3s\t %6s\n"%("name", "age", 'sex'))
fp.write("%10s\t %3d\t %6s\n"%("lwk", 56, 'male'))
fp.write("%10s\t %3d\t %6s\n"%("中文", 45, 'male'))
fp.write("%10s\t %3d\t %6s\n"%("ght", 43, 'male'))
fp.write("%10s\t %3d\t %6s\n"%("lli", 73, 'male'))
fp.write("%10s\t %3d\t %6s\n"%("lwk", 56, 'female'))
fp.close()

##################################################################	

fr = open("fw.txt",'r')
print fr.readline()  #中文正常显示
print fr.readline()
print fr.readline().strip().strip('\n').split('\t') #去空格换行符，再截断
print "-----"
print fr.readlines() #中文会变字符码
fr.close()

	