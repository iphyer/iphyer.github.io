---
layout: post
title: "X ray峰的指标化"
date: 2013-12-09 14:50
comments: true
categories: 物理
---

##前言

X射线课的一篇作业，有点意思，所以贴出来。

>EuTiO3具有理想的立方钙钛矿结构,其晶格常数与SrTiO3的
相等,均为3.905 Å,这二者可以组成一个比较理想无应力
体系,用于研究复杂结构的氧化物薄膜无应力生长的机
理。
>从课程网站上下载实验数据,使用任一你喜欢的软件画出$EuTiO_3$粉末的XRD谱,然后计算并标出各个衍射峰的指数(写出计算过程和结果)。

具体的数据在这里(http://pan.baidu.com/s/1w3kOc)

<!--more-->

首先先做图，看一看这个X射线的峰分布。结果如下，这里是以$2 \theta$为横坐标画图：

![tu1](/images/Xray/XRD.png)

由Bragg公式：

$$
2 d_{hkl} \sin \theta = \lambda
$$

然后考虑到EuTiO_3是立方晶系，我们有 

$$d_{hkl}=\frac{a}{\sqrt{h^2+k^2+l^2}}$$ 

，这里a为晶格常数。

所以简单的变形就有：

$$
\frac{\lambda}{2d_{hkl}}=\sin \theta
$$

知道了峰的位置($2\theta$)也就可以求出$\sin \theta$,同时一般X射线的波长也是已知的，这里是可以直接从X射线的数据文件中读出来为$1.540562$ Å。

然后是计算相对应的晶面指数的对应的X射线的$\frac{\lambda}{2d_{hkl}}$，具体可以用python来解决。

```python

# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 00:26:21 2013

@author: famer
"""

import math as m

for h in range(0,5):
    for k in range(0,5):
        for l in range(0,5):
        	print h,k,l,(1.540562/3.905)*m.sqrt(h**2+k**2+l**2)/2.0

```

其实就是生成一系列的随着晶面指数变化的$\frac{\lambda}{2d_{hkl}}$。这里需要注意Python的sin是有范围限制的且以弧度为单位。

当然生成的数据有的时候会有重复，这个时候需要排序数据，然后挑选出合适的数据。最后结果如下：

![tu1](/images/Xray/Graph4.png)


