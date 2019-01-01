---
layout: post
title: "Python编程3——Python计算是否是perfect number"
date: 2013-01-13 10:32
comments: true
categories: Python
---

#前言

这里是实现0～100之内数字输出全部的完美数，所谓完美数也就是这个数的所有因子的和等于这个数。

比如：

6=1+2+3

28=1+2+4+7+14


<!--more-->

#程序

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#the programe is judging whether the number is perfect
#the perfect number is number that the sum of its factor equals itself
#like 6=1+2+3,28=1+2+4+7=14

topNum=raw_input("Please enter the upper number of the range: \n")
topNum=int(topNum)
theNum=2


while theNum<=topNum:
	#sum up all the factor
	divisor=1
	sumofDivisors=0
	#judge whether it is the factors of theNum
	while divisor<theNum:
		if theNum%divisor==0:
			sumofDivisors=sumofDivisors+divisor
		divisor=divisor+1
	if theNum==sumofDivisors:
		print theNum,"is perfect"
	theNum+=1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

当然可以看出来100以内也就只有6和28两个数字。