---
layout: post
title: "Python编程1——Python计算圆的周长和面积"
date: 2013-01-13 10:17
comments: true
categories: Python
---

# 前言

这是我对于"The Practice of Computing Using Python"的读书笔记。
总结了这本书很多有趣的编程题目。初次练手大家轻拍。

# Python计算圆的周长和面积
<!--more-->
这个程序比较简单，直接上程序了。

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#this is the programe taught by the book 
#the practice of Python 
#By waventroy

import math 

radiusString = raw_input("Please input the radius of the circle: \n")
radiusInterger = int(radiusString)
circumference = 2 * math.pi * radiusInterger

area = math.pi*(radiusInterger**2)

print "The circumference of the circle is : " ,circumference ,"\n", \
      "The area of the circle is:" ,area

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
