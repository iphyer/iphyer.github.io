---
layout: post
title: "Linux打印目录下多个文件"
date: 2014-01-06 13:47
comments: true
categories: Linux
---

今天因为要打印多个文档在Linux下，所以尝试着使用Linux下的lpr命令打印，现在才发现Linux的打印命令确实很多，而且非常智能。这里总结一下。

<!--more-->

##虚拟打印和物理打印

物理打印对应着一台真实的打印机，这个就不再赘叙了。

虚拟打印顾名思义就是使用打印服务就将内容打印到pdf文档中去，而不是在真正的物理打印机上打印。这里首先需要配置下CUPS，比如安装CUPS-pdf包（至少我的Ubuntu12.04是需要的）。 可以用 `lpstat -a`命令察看，比如在我的机器上结果是：`PDF accepting requests since Mon 06 Jan 2014 01:45:23 PM CST`。或者是`lpstat -s`这个命令可以用来察看系统默认的打印机，结果是:
`system default destination: PDF`

`device for PDF: cups-pdf:/`

对于陌生的机器或者自己不确定的系统设置，这个命令非常有效果。具体请参看man的结果。

##普通打印

CUPS打印组件支持两种打印方法，分别是Berkeley和SysV。Berkeley或LPD（UNIX的Berkeley软件发行版本中使用的）方法，运用的是lpr命令；SysV（来源于UNIX的System V版本）方法，运用的是 lp 命令。

具体的使用非常方便，命令名+文件名，中间也有些参数可以制定信息，请参考man或者这个网页[ Printing Under Linux](http://www.tldp.org/HOWTO/Printing-Usage-HOWTO-2.html)。可以选择所有的我们常见的打印命令如纸张，份数，正反打印等等。

##批量打印

###批量打印成一个文件

这个比较简单，直接使用正则匹配即可。当然前提是这里我的文件都在一个目录下且都是需要打印的，lpr自动在home目录生成PDF目录并且以打印文件所在目录下第一个文件命名的文件合集。

```bash

lpr *.pdf

```


###批量打印成多个文件
这时用bash的一个循环结束任务。

```bash

for myfile in *.pdf; do lpr -p $myfile; done

```
这样lpr同样会在home目录生成PDF目录并且保留打印文件所在目录的文件结构。

##注意

我发现lpr命令对于文件的名称要求比较严格，比如文件名中含有空格基本就失效了，这个可能需要在用bash处理下。
