---
layout: post
title: "Python编程6——Python实现Collatz"
date: 2013-01-13 10:48
comments: true
categories: Python
---

# 前言

这个是需要更多修改的部分。Python实现Collatz序列。
本来以为比较简单，但是看了看维基百科的说明，这个居然可以出现分形，顿时冋了。
这个还需要修改啊。


![tu1](/images/Python/Collatz/CollatzFractal.png) 

<!--more-->

# Collatz序列的定义

所谓的Collatz序列是这样的一种序列：

* 对于偶数，除以2
* 对于奇数，乘以3再加上1

最后直到结果为1时结束程序。



# 生成Collatz序列

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#this is the generator of Collatz Sequece
#we use the programe to generate it
#the Collatz Sequece is the series that has the following character:
#if the number is even , divide it with 2
#if the number it odd, multilply it with 3 and add 1 to get the final result
#if we get 1, exit the programe
#waventropy

numStr=raw_input("Enter a postive number:")
num=int(numStr)
count=0

print "Start with number:",num
print "Sequece is:",
#the ending , is to set Python put the output of print in oneline

while num > 1:
	if num%2:
		num=num*3+1
	else:
		num=num/2
	print num,",",
	
	count+=1
	
else:
	print
	print "Sequece is",count,"number long"

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


