---
layout: post
title: "Python编程7——Python比较相同字母组成的单词"
date: 2013-01-13 13:02
comments: true
categories: Python
---

#前言

这个程序比较简单就是比较两个单词是不是可以用相同的字母不同的排序组合出来的。


#程序
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#the programe compares that some word letters can 
#be reput as a new word

def areAnagrames(word1, word2):
	"Return the result of the comparison"
	#resorted the two words in the aplhabeta order
	word1_sorted=sorted(word1)
	word2_sorted=sorted(word2)
	return word1_sorted==word2_sorted
	
print "Anagram Test"
twowords=raw_input("Enter two words separing with whitespace: \n")
twowordsList=twowords.split()
word1=twowordsList[0]
word2=twowordsList[1]

if areAnagrames(word1,word2):
	print "The two words are anagrams."
else:
	print "The two words are not anagrams."
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

<!--more-->

#效果

![tu1](/images/Python/anagrams/tu1.png)

#改进

当然程序还有一处可以更改的，就是使用多重赋值替代两个赋值语句

~~~~~~~~~~~~~~~~~~~~~~~~~~~~
word1,word2=twoWords.split()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~