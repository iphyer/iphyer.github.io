---
layout: post
title: "Python编程9——Python分析Gettysburg Address演讲"
comments: true
categories: Python
---

#前言

这是对于葛底斯堡演讲所作的分析。

林肯的这篇演讲是美国历史上的重要演讲，文章最后的“that government of the people, by the people, for the people, shall not perish from the earth.”更是传唱千古的名句。
这里简单分析了这篇演讲，用词并不是很多。

这里的练习是为了让大家熟练掌握需要的语言分析技巧。其实用过的很多的程序，比如R等，但是说实话，分析文本数据处理其他的东西而言
还是Python特别顺手。

<!--more-->

#程序1——简单分析

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#getttsburg addresss analysis
#count words, unique words, common wrods

def makewordList(gFile):
	"""create a list of the words in the address"""
	speech=[]
	for lineString in gFile:
		lineList=lineString.split()
		for word in lineList:
			if word !="--":
				speech.append(word)
	return speech
	
gFile=open("gettysburg.txt","rU")
speech=makewordList(gFile)

print speech
print "Speech Length:",len(speech)		
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

![tu1](/images/Python/gettysburg/tu1.png) 

可以看到全文用词只有271个。


#程序2——改进消除重复

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#getttsburg addresss analysis
#count words, unique words, common wrods
#here is the case that print the unique words in the addresss

def makewordList(gFile):
	"""create a list of the words in the address"""
	speech=[]
	for lineString in gFile:
		lineList=lineString.split()
		for word in lineList:
			word=word.lower()
			word=word.strip('.,')
			if word !="--":
				speech.append(word)
	return speech
	
def makeunique(speech):
	"""this is pick out the unique word and put them in uniquelist"""
	unique=[]
	for word in speech:
		if word not in unique:
			unique.append(word)
	return unique

	
gFile=open("gettysburg.txt","rU")
speech=makewordList(gFile)
unique=makeunique(speech)

print speech
print "Speech Length:",len(speech)		

print unique
print "Length of the unique words",len(unique)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

![tu2](/images/Python/gettysburg/tu2.png) 

这里会发现用词格外的少，去然只有138个不同的用词。可以发现林肯的演讲确实是非常的精炼。