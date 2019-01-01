---
layout: post
title: "kindle漫画的制作"
date: 2012-09-23 04:21
comments: true
categories: kindle
---

文章的原理来自，kindle迷的文章，链接如下：<http://www.kindlemi.com/archives/312>。

这篇文章讲的十分具有创意没有使用很多复杂的工具，而是联合使用了很多的小工具就达到了很好的效果。非常欣赏。

但是有些小不足，比如图片尺寸的调整并不能实现批量处理，降低了效率。所以我针对这个不足，做了调整。


<!--more-->

## 需要的软件：

JPG批量重命名工具(<http://www.xiazaiba.com/html/2970.html>)（将漫画文件夹批量重命名并合并到一个文件夹下） 

iSee图片专家( <http://www.onlinedown.net/soft/39528.html> ) （将JPG转为PDF前，需先将图片缩小减少PDF体积） 

JPG转PDF工具(<http://www.xiazaiba.com/html/2658.html>)该工具小巧实用，将在下面介绍具体的使用方法） 
 

## 重命名图片
这一步主要是方便图片的命名。

当然还有更好的方法，使用firefox的downthemall可以实现图片的自动重命名。当然如果是已有的图片文件，那么
使用重命名的效果是很好的。 

## 图片尺寸调整
因为kindle是6寸屏幕，所以我们需要把图片尺寸进行调整。 

使用isee可以很容易的统一调整尺寸。将JEPG的尺寸调整为460×678（注：这不是最佳的分辨率，最佳是600×800，但是消耗体积）


![tu1](/images/kindlecomic/1.png)

![tu2](/images/kindlecomic/2.png)



## 图片生成pdf
下面这步比较简单就是用jpegtopdf这个工具实现把图片连缀成pdf的功能。

当然依靠word等软件的功能也可以实现生成pdf的功能，但是只在图片数量较少的情况下可以使用且图片顺序不一定可以实现自己的要求。 

![tu3](/images/kindlecomic/3.png) 

注：With设置为80，Height设置为120，布局Top-Left Corner 

## 讨论 

其实我一直在研究怎么在linux平台上实现这个功能。现在看来其他的功能全部可以实现，但是jpg to pdf不太好实现。图片尺寸可以用ImageMagick实现，但是实现pdf这个功能则是百思不得其解。
 希望可以和大家讨论。
