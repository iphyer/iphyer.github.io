---
layout: post
title: "GRE卡片单词"
date: 2014-10-23 16:17
comments: true
categories: GRE
---
# 前言

最近在网上发现一个非常好的，GRE单词的总结的配图版本，花费了一天时间，终于把图片都下载下来了。

仔细回想一下其实挺简单的，但是一开始没找到最简单的方法，想用Python，在人人网渣渣的HTML代码页面爬行了半天，掉到无数的坑里面爬不出来。

今天下午睡了个午觉,用grep,wget一下子搞定。So Easy.

上两个实例:

![tu１](/images/GRE/GREpicture/a.jpg)

这幅图很好的表达了:

al·lege verb \ə-ˈlej\ 
: to state without definite proof that someone has done something wrong or illegal

不可靠的宣称的意思。

![tu１](/images/GRE/GREpicture/b.jpg)

这个图自己理解。不解释了。

<!--more-->

# 技术过程

需要说明，这个作者制作的时候可能有的单词打错了，大家使用的时候注意。

下载地址:[百度网盘](http://pan.baidu.com/s/1o6ogi5k)

一开始是在Github上找软件的，发现了基于Chrome应用的Renren Album Downloader非常好，但是下载的时候对于文件大小有限制——已知的bug就是对于大于500张照片的情况下会出现崩溃。具体原因不明，而我需要下载的是507张照片，果然崩溃。

然后尝试了Github上的这个Python代码[atifrons/RenrenAlbumDownload](https://github.com/latifrons/RenrenAlbumDownload)其实这个Python的代码写得非常好，但是作者是在2012年写得，几年过去了人人进行了很大的更新所以很多方法都不太可靠了。但是作者的这个程序还是可以使用的，作者在登陆函数设计方面非常好，对于验证码也很好的解决了，读了他的源代码收获很大，非常有帮助。可惜的是，不知道为什么只能在每个相册上下载40张图片。我仔细阅读了作者的页面解析部分，是基于正则规则的搜索。非常复杂而且不是针对现在的人人网代码的所以也就放弃了。

这个时候我发现人人可以选择不分页模式浏览相册，这样的话所有的照片都可以看到，而且为了保证点击可以进入看大图，人人设置了超链接所以只要能够把超链接提取出来，我就可以用wget提取了。又回过来看了wget的ｍanul发现wget是支持从预设的文件输入参数的。所以我就使用了这个方法做页面解析了。

# 代码细节

## 页面解析

使用了BeautifulSoup解析，这里原谅我很粗暴的使用了直接输入HTML的办法，因为不想使用urllib了毕竟已经下载了页面。

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from bs4 import BeautifulSoup

html= """
<!DOCTYPE html>
<!-- saved from url=(0065)http://photo.renren.com/photo/230038558/album-938072917?noPager=1 -->
<html xmlns="http://www.w3.org/1999/xhtml" class=" marginRightForPager"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<meta charset="utf-8"><meta name="Description" content="人人网 校内是一个真实的社交网络，联络你和你周围的朋友。 加入人人网校内你可以:联络朋友，了解他们的最新动态；和朋友分享相片、音乐和电影；找到老同学，结识新朋友；用照片和日志记录生活,展示自我。">

....省略很多HTML代码

"""


soup = BeautifulSoup(html)
img=soup.find_all("img")
print img

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


这段代码的功能就是把所有的img标签提取出来，在terminal里面使用一下重定向把输出直接输入到一个tem的文件里面。本来还想在这个基础上用Python提取url的，后来发现还是不熟悉Python的正则规则，放弃，直接使用grep和wget吧。

## 提取url

这个提取直接使用grep的正则查找，然后把结果重定向，注意我只查找.jpg结尾的url。

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

grep -oP '(?<=")http.*?(jpg)(?=")' tem > url.txt

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## wget下载图片

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

wget -b -i url.txt -c

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

最后把所有得到的照片按照名称排个序，把所有main开头的缩略图删掉只留下orginal开头的原图。

至此全部搞定！

# 总结

其实这次可以发现，我一开始就没怎么想用wget下载结果导致最后花费了不少时间，确实很多时候wget这样的小工具还是相当方便的，多多使用。
