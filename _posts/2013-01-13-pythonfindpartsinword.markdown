---
layout: post
title: "Python编程8——Python寻找单词中符合顺序的元音字母"
date: 2013-01-13 13:22
comments: true
categories: Python
---

# 前言

程序的目的就是标题。

# 程序

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#to find a word that contians the specific parts in it
#in this case it is "aeiou" , all the Vowel letters

datafile=open("dictionary.txt","r")

def cleanWord(word):
	"""Return word in lower case without whitespace"""
	return word.strip().lower()
	
def getVowelsInword(word):
	vowelsStr="aeiou"
	vowelsInword=""
	for char in word:
		if char in vowelsStr:
			vowelsInword+=char
	return vowelsInword

#main program
print "Find words containing vowels 'aeiou' in that order: \n"
for word in datafile:
	word = cleanWord(word)
	if len(word)<=6:
		continue
	vowelStr=getVowelsInword(word)
	if vowelStr=="aeiou":
		print word

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

<!--more-->

# 效果

![tu1](/images/Python/findvowels/tu1.png)
