---
layout: post
title: "Python编程11——Python作葛底斯堡演讲和美国独立宣言的比较分析"
date: 2013-01-13 16:21
comments: true
categories: Python
---

# 前言

这里其实是把葛底斯堡演讲和独立宣言联合在一起分析了。
这里的作用不在于取得最后的结果只是简单分析就可以知道这两篇文章都是反应美国建国思想的文献资料。不出意料的话，两者会有很多的共同点。
分析的结果也支持这个观点。

独立宣言是北美十三州脱离英国殖民统治的政治宣言，葛底斯堡演讲是林肯在美国内战的重要战场葛底斯堡发表的演说。美国内战事实上
的一个重要原因是解决美国建国时南北双方的政治妥协破裂后的矛盾与危机。所以两篇文章都可以认为是美国的建国思想体现。
比如两篇文章的高频词汇中都出现了，civil， government， people， nation，liberty等这些美国建国思想。

当然我们的重点不是这些而是Python作文本分析的一些技巧。

<!--more-->

# 程序

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#compare two files to help Python understand what's different or common
#things in the declearation of Independence and the Gettysburg Address
#this programe mostly features in the set datatype of Python
import string

def processLine(line,theSet):
	#cut the whitespace before and after everyline
	#sitll use strip method to seperate different words
	wordlist=line.strip().split()
	for word in wordlist:
		if word !="--":
			word=word.lower()
			word=word.strip()
			word=word.strip(string.punctuation)
			addword(word,theSet)

def addword(w,theSet):
	if len(w)>3:
		theSet.add(w)


def prettyPrint(gaSet,doiSet):
	print 'Count of the unique of the files in the comparsion(Length >=4):'
	print 'Gettysburg Addr: %d, Decl of Ind: %d \n'%(len(gaSet),len(doiSet))
	print '%15s %15s'%('operation','Count')
	print '-'*35
	print '%15s %15d'%('Union',len(gaSet.union(doiSet)))
	print '%15s %15d'%('Intersection',len(gaSet.intersection(doiSet)))
	print '%15s %15d'%('Sym Diff',len(gaSet.symmetric_difference(doiSet)))
	print '%15s %15d'%('GA-DoI',len(gaSet.difference(doiSet)))
	print '%15s %15d'%('DoI-GA',len(doiSet.difference(gaSet)))
	intersectionSet=gaSet.intersection(doiSet)
	wordList=list(intersectionSet)
	wordList.sort()
	print '\n Common words to both the two files'
	print '-'*20
	cnt=0
	for w in wordList:
		if cnt%5==0:
			print
		print '%13s'%(w),
		cnt+=1

#main programe
GAset=set()
DoIset=set()
GAObj=open("gettysburg.txt",'r')
DoIObj=open("declOfInd.txt","r")
for line in GAObj:
    processLine(line,GAset)
for line in DoIObj:
    processLine(line,DoIset)
prettyPrint(GAset,DoIset)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 效果

![tu15](/images/Python/gettysburg/tu5.png)

