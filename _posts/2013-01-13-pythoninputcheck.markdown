---
layout: post
title: "Python编程5——Python实现对与输入的检查"
date: 2013-01-13 10:42
comments: true
categories: Python 
---

#前言

这里实现的是Python对于输入的检查。

只有经过检验的输入才是可以接受的——这句话是书中普遍强调的。

对于输入的检验有两种思路：


* 第一个就是对于用户的输入进行修改，比如用户可能会yes，Yes，YES等等，都让其通过
* 第二个就是强制只有一种输出可以，但是换个方式，在程序的输出语句中进行提示，比如yes or no？

这里作者推荐第二种，这也是符合Python哲学的方式，做一件事情只有一种方法。


<!--more-->

#程序

这个程序其实是简单的一个累加程序，但是这里强制了用户必须按照提示的方式输入，否则无法执行。
个人感觉这个也是Python的哲学，必须使用惟一的正确的方式解决问题。

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#sum up all the numbers
#make usre the input is right

print "All the user to input all the numbers to get the sum"
print "Ingore non-numeric input. End the input with '.'"

theSum=0
theNum=raw_input("The number is:\n")
while theNum !='.':
	if not theNum.isdigit():
		print "Error!Please re-enter a number \n"
	else:
		theSum+=int(theNum)
	theNum=raw_input("Number: \n")

print "The sum is:",theSum

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~