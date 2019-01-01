---
layout: post
title: "Python编程2——Python实现计算篮球比赛是否领先安全的程序"
date: 2013-01-13 10:26
comments: true
categories: Python
---

# 前言

这个程序的算法部分是Bill James 博士的'Safe lead calculator'

网址：http://www.slate.com/articles/sports/sports_nut/2008/03/the_lead_is_safe.html

这里有一个基于swf的计算器的实现http://img.slate.com/media/53/LeadCalc2.swf


![tu1](/images/Python/Leadissafe/tu1.png)

<!--more-->

# 程序

这里我全部略过算法的说明部分，直接上程序了。

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Bill James 'Safe lead calculator'
#from http://www.slate.com/id/2185975/

#take the number of points one team ahead
pointsStr=raw_input("Enter the number of the lead in the play: \n")
pointsInt=int(pointsStr)

#subtract threee
points=pointsInt-3

#add a half-point or not 
#depenf the ball is has or not
has_ball=raw_input("Does the lead team has the ball or not(Yes or No): \n")

if has_ball == 'Yes':
	points=points+0.5
else:
	points=points-0.5
if points < 0:
	points=0
#square the points to get the conclusion
points=points **2

#to judge the condition whether we should judge there should the
#time that left

seconds=int(raw_input("Enter the number of seconds remaining: \n"))

if points > seconds:
	print "Lead is safe!"
else:
	print "Lead is not safe!"	

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
