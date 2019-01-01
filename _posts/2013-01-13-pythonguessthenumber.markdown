---
layout: post
title: "Python编程4——Python实现猜数字的程序"
date: 2013-01-13 10:36
comments: true
categories: Python
---

# 前言

这个也不多说了，python大家经常见到的猜数字游戏。

这里我print了原来生成的随机数，只是为了验证方便，正式的实现的时候需要删去。

<!--more-->


# 程序

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# while-else 
# Simple guessing game: start with a random number and  
# guess with hints until:
#    guess is  correct
#    the guess is out of range indicating the user is quitting

import random  # get the random number module
number = random.randint(0,100) # get a random number 
                               # between 0 and 100 inclusive

print "Hi,this is the guess the number game. You can enter the number between 0 to 100 to guess it"
print number

guessStr=raw_input("Please enter the number (0~100):")
guess=int(guessStr)
while 0<= guess <=100:
	if guess > number:
		print "Too high. \n"
	elif guess < number:
		print "Too low \n"
	else:
		print "You get the answer. The number is", number
		break
		
	guessStr=raw_input("Please enter the number (0~100):")
	guess=int(guessStr)

else:
	#if the input is not in 0 to 100
	print "You quit too early.The number is:", number

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 效果

![tu1](/images/Python/guessnumber/tu1.png)