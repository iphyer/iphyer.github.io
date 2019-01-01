---
layout: post
title: "压缩博客图片尺寸"
date: 2017-05-13 10:01
comments: true
categories: 博客
---

# 原因

之前一直没管博客图片的大小因为感觉其实不太重要，毕竟是 Github　的免费空间，没有那么大的动力优化图片。

但是最近发现有的博客确实图片太多了，所以加载起来很慢，所以才开始了优化。

现在把最后的成品写成这个博客。

<!--more-->

# 原理

原理非常简单，列出当前文件夹全部的图片文件(JPG,PNG)，然后处理所有的大于 1M　的图片。

然后循环运行脚本，知道不在出现大于 1M 的图片即可。

# 脚本

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#! /bin/bash 

#获取脚本所在文件目录
#大于1M图片缩小一半




    for file in  `find ./ -name "*.[jJ][pP][gG]"`;
    do    	
    	if [ `stat --printf="%s" $file` -gt 1000000 ]
		then
    		echo $file
    		mogrify -resize 50% $file
		fi

	done

	for file in  `find ./ -name "*.[pP][nN][gG]"`;
    do 
    	if [ `stat --printf="%s" $file` -gt 1000000 ]
		then
    		echo $file
    		mogrify -resize 50% $file
		fi
	done


echo "Done"



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 效果
最后配图文件夹减少了 2/3 的体积还是很不错的。
