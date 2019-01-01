---
layout: post
title: "Python系统文件操作"
date: 2013-01-17 13:10
comments: true
categories: Python
---

# 前言

其实做了这么多的文件数据分析。大家还是会奇怪这些工作用excel也可以做啊。
甚至很快捷的可以解决。的确，我们可以很快速的使用excel这样的工具解决，但是比较bug的是如果文件很多时候怎么办？

其实很简单，用VBA这样的工具也是可以实现的。
但是如果你没有VBA的话，那么就只能选择开源的内容去实现了。比如说Python。
如果是Python的话，下面一步需要解决的就是如何在系统中寻找文件并且打开然后进行计算。

这就是这篇日志的内容。

<!--more-->

# 程序

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import os

def check(searchStr,count,fileList,dirlist):
	for dirName,dirs,files in os.walk("."):
		for f in files:
			if os.path.splitext(f)[1]==".txt":
				count=count+1
				aFile=open(os.path.join(dirName,f),'r')
				fileStr=aFile.read()
				if searchStr in fileStr:
					fileName=os.path.join(dirName,f)
					fileList.append(fileName)
					if dirName not in dirList:
						dirList.append(dirName)
						aFile.close()
			    
	return count
	
theStr=raw_input("What string to look for? \n")
fileList=[]
dirList=[]
count=0
count=check(theStr,count,fileList,dirList)
print "looked %d txt files"%(count)
print 'found %d directories containing files \with ".txt" suffix and target string:%s' %(len(dirList),theStr)
print 'found %d files containing files \with ".txt" suffix and target string:%s' %(len(dirList),theStr)
print '\n ***** Directory List *****'
for d in dirList:
	print d
	
print '\n ----- File List-----'
for f in fileList:
	print f

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

这里我直接使用了rake deploy这个字符串因为我本来有一个doc里面的使用备忘。同时自己新添加了几个文件作为
测试。

效果

![tu1](/images/Python/os/tu9.png)

