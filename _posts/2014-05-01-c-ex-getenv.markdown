---
layout: post
title: "C语言getenv的使用"
date: 2014-05-01 21:39
comments: true
categories: 
---

##getenv

getenv得到在bash中使用env命令得到的所有信息。

<!--more-->

##示例

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#include<stdio.h>
#include<stdlib.h>

int main(int argc,char *argv[], char *envp[])
{
	char *home,*host;
	
	home=getenv("HOME");
	host=getenv("LC_TIME");
	printf ("Your Home directory is %s on %s. \n",home,host);
	return 0;
}

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


输出

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Your Home directory is /home/famer on zh_CN.UTF-8.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
