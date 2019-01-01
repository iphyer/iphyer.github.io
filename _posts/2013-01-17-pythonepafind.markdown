---
layout: post
title: "Python寻找环境保护署通车里程数"
date: 2013-01-17 09:35
comments: true
categories: Python
---

# 前言

这个程序是寻找美国环境保护署网站公布的美国各种车辆的通车历程数据。

具体的形式如下：

> CLASS	MFR	CAR LINE	DISPLACEMENT	NUMB CYL	TRANS	DRIVE SYS	INDEX NUMB	CITY MPG (GUIDE)	HWY MPG (GUIDE)	COMB MPG (GUIDE)	UNRND CITY (EPA)	UNRND HWY (EPA)	UNRND COMP (EPA)	FUEL TYPE	GUZLR	TURBO	SPCHGR	AVG 2D PASS VOL	AVG 2D LUGG VOL	AVG 4D PAS VOL	AVG 4D LUGG VOL	AVG HB PAS VOL	AVG HB LUGG VOL	ANL FL CST	ENG BLK TXT	TRANS DESC TXT	VLVS PER CYL	CLS	REL DT	5C CODE

> TWO SEATERS	ASTON MARTIN	V8 VANTAGE	4.3	8	Auto(S6)	R	12	13	20	15	16.1945	27.4018	19.8474	P	G									3002		4MODE	4	1	6-Aug-07	DERIVED

> TWO SEATERS	ASTON MARTIN	V8 VANTAGE	4.3	8	Manual(M6)	R	11	12	19	15	15.2	25.7	18.6241	P	G									3002			4	1	6-Aug-07	DERIVED

> TWO SEATERS	AUDI	R8	4.2	8	Auto(S6)	4	19	13	19	15	16.1944	26.2	19.555	P	G									3002		3MODE CLKUP	4	1	17-Aug-07	DERIVED

这里我们需要的是从零开始的第九列元素和第一列以及第二列元素。

<!--more-->

现在我们使用具体的程序去计算。这里是一步步搭建整个程序网络的。

# 简单程序

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
epaFile=open("epaData.csv","rU")

for line in epaFile:
	if 'FERRARI' in line:
		print line[:75]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# 生成通车里程列表

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#we find out the number of the car of running the miles
#we use  split(',') to separate the csv value

def creatMileageList(epaFile):
	mileageList=[]
	for line in epaFile:
		lineList=line.split(',')
		mileageList.append(lineList[9])
	return mileageList
		

epaFile=open("epaData.csv","rU")

mileageList=creatMileageList(epaFile)

print mileageList
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 找出通车里程列表中的最大值和最小值


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# we further transfer the character into integer
# also ignore the class value of the first line with continue function
#continue can move into the next line without add it into the List
#when we get that done we can use max and min function to get the extreme value

def creatMileageList(epaFile):
	mileageList=[]
	for line in epaFile:
		if line[0:5] == "CLASS":
			continue
		lineList=line.split(',')
		temp=int(lineList[9])
		mileageList.append(temp)
	return mileageList
		

epaFile=open("epaData.csv","rU")

mileageList=creatMileageList(epaFile)

maxMileage=max(mileageList)
minMileage=min(mileageList)

print "The Max and Min in the List is:",maxMileage,minMileage 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 在找出最大值和最小值的基础上在对应相应的制造商


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# in this case we want to also find the car trafe of the max and min Mileage
# to avoid the other visit of all the value 
# we append two value together to get another list of truple

def creatMileageList(epaFile):
	mileageList=[]
	for line in epaFile:
		if line[0:5] == "CLASS" or "VAN" in line or "PICKUP" in line:
			continue
		lineList=line.split(',')
		temp=int(lineList[9])
		carTruple=(temp,lineList[1],lineList[2])
		mileageList.append(carTruple)
	return mileageList
		

epaFile=open("epaData.csv","rU")

mileageList=creatMileageList(epaFile)

maxMileage=max(mileageList)
minMileage=min(mileageList)

print "The Max and Min in the List is:",maxMileage,minMileage 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 找出全部的数据

之所以会有这一步的原因在于Python默认返回的是所有最小最大值中的第一个。

所以我们构建一个列表，再次遍历列表找到相应的元素后添加。

同时对于元组构成的列表，为了美观，我们同样使用遍历的方法打印出列表中的，每一个元素。

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#in this programe we want to find all the case that has the max or min value in the carMileageList
# this is because the min/max function in Python only return back the 
# first found case in the list that has the same value

def creatMileageList(epaFile):
	mileageList=[]
	for line in epaFile:
		if line[0:5] == "CLASS" or "VAN" in line or "PICKUP" in line:
			continue
		lineList=line.split(',')
		temp=int(lineList[9])
		carTuple=(temp,lineList[1],lineList[2])
		mileageList.append(carTuple)
	return mileageList

def FindMaxMinMileage(mileageList,maxMileage,minMileage):
	maxMileageList=[]
	minMileageList=[]
	for carTuple in mileageList:
		if carTuple[0]==maxMileage:
			maxMileageList.append(carTuple)
		if carTuple[0]==minMileage:
			minMileageList.append(carTuple)
	return maxMileageList,minMileageList
	

epaFile=open("epaData.csv","rU")

mileageList=creatMileageList(epaFile)


maxMileage=max(mileageList)[0]
minMileage=min(mileageList)[0]


print "The Max and Min in the List is:",maxMileage,minMileage 

maxMileageList,minMileageList=FindMaxMinMileage(mileageList,maxMileage,minMileage)

#Note the print of Tuple must use visit style to get 
#You can get nothing with only the print function

print "Maximum Mileage Cars:"

for carTuple in maxMileageList:
	print " " ,carTuple[1],carTuple[2]

print "Minimum Mileage Cars:"
for carTuple in minMileageList:
	print " ",carTuple[1],carTuple[2]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

![tu15](/images/Python/epa/tu7.png)


