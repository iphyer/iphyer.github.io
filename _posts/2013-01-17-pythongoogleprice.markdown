---
layout: post
title: "Python分析Google股价数据"
date: 2013-01-17 12:57
comments: true
categories: Python
---

# 前言

这是为了分析Google的股价数据，所作的数据挖掘。
比较简单，但是数据挖掘的基本分析过程和思想都有所体现。

# 寻找数据

去

http://finance.yahoo.com/ 

上下载我们所需要的信息，也就是Google的股价数据。

我们选择历史数据这一栏：

![tu1](/images/Python/google/google.png)

下载即可。

<!--more-->

#程序

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def creatlist(Gfile):
	datalist=[]
	sumall=0
	
	for line in Gfile:
		if line[0:4]=='Date':
			continue
		datanew=line.strip().split(',')
		vol=int(datanew[5])
		adj=float(datanew[6])
		yearmonth=datanew[0][0:7]
		monthsum=vol+adj
		pricetuple=(yearmonth,monthsum)
		datalist.append(pricetuple)
	return datalist
	

def getthesumofmonth(datalist):
	monthlyaverageprice=[]
	temp=[]
	indexdate=datalist[0][0]
	sumall=0
	days=0
	for pricetuple in datalist:
		if pricetuple[0]==indexdate:
			sumall=sumall+pricetuple[1]
			days=days+1
		else:
			monthlyaverageprice.append((sumall/days,indexdate))
			indexdate=pricetuple[0]
			sumall=pricetuple[1]
			days=1
			#monthlyaverageprice.append((indexdate,sumall/days))
	return monthlyaverageprice

#find the best and worst 6 month of Google
def findbest6months(monthlyaverageprice):
	newlist=sorted(monthlyaverageprice)
#	lengthlist=len(newlist)
	return newlist[0:6],newlist[-6:]

def printinfo(newlist):
	print '-'*20
	for newtuple in newlist:
		print newtuple[1],',',newtuple[0],'\n'
	return 'END'
	 
	

Gfile=open("table.csv","r")
datanewlist=creatlist(Gfile)
monthlyaveragenewlist=getthesumofmonth(datanewlist)
maxlist,minlist=findbest6months(monthlyaveragenewlist)

print "The max monthes is :"
print printinfo(maxlist)
print "The min monthes is:"
print printinfo(minlist)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

![tu12](/images/Python/google/tu8.png)
