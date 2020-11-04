---
layout: post
title: "Python2 Binary String 和 Python3 的转换"
date: 2020-10-23 21:49
comments: true
categories: 科研
---

其实是一个非常特殊的情况，但是还是真是被这个小点坑了。这里记录下来，反思下。


<!--more-->

# 问题描述

这是一个在计算的代码，目的是为了实现对于一个原子体系的 FFT 计算用来模拟 X-ray 的成像。其中，需要统计 Real Space 的电子云分布，这里电子数目是根据具体的原子的类型进行选择的，比如下面这个 `dict` 的 mapping

```python

formfact = {
        'C1': 33,
        'P5': 55,
        'BP4': 40,
        'P4': 40,
        }

```
这个 code 是从一个 ANL 的博士后那里得来的，我没怎么在意他是怎么实现他的 read in code，结果他是用 Python2 read in as binary string。我虽然修改了代码让它 compatible with Python3 但是没有注意这个细节。最后的结果就是我读入的都是 binary string, 但是在我的程序里面只是设置了上面的 Python3 正常 string。而且我还有这么一个代码片段，其实这段是当时博士后加上去为处理一些不存在的原子和分子设置的，这些可能只是一些简单地盐等环境溶液。

```python

for iType in typelist:
    if iType not in formfact:
        formfact[iType] = 1.0

for key in formfact:
    print( key )

```

导致诡异的一点就是，这些没办法和电子数目字典配对的 binary string 都被当成了 1。真是石破天惊。。。其实我一直在生成一个全是 1 + 0 的立方体。

# 解决方法

解决方法其实很简单，但是原理并不简单，参考这个帖子得到更多的背景知识，[字符串和编码](https://www.liaoxuefeng.com/wiki/1016959663602400/1017075323632896)

> 由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。

> 要注意区分 'ABC'和 b'ABC' ，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。

所以修改成为如下的代码，


```python

for iType in typelist:
    if iType.decode('utf-8') not in formfact:
        formfact[iType.decode('utf-8')] = 1.0

```

如果不做 `decode` 那么其实 string 和 byte string 不一样。字典没办法匹配。

# 总结

其实这个故事告诉我们，别人的代码如果要复用，请打印下中间变量，找出他们的内容，和你自己的理解对比下。有的时候其实很简单的转换就会出问题。