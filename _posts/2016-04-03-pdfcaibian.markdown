---
layout: post
title: "PDF裁边总结"
date: 2016-04-03 08:39
comments: true
categories: Linux
---

今天打印文献，以前都是在Windows下用Briss打印因为打印机只支持Windows下的双面打印，虽然HP官网说是支持Linux但是谁用谁知道啊，特别坑。

今天是因为需要打印的文献比较多，所以我觉得每次都用Briss裁边比较麻烦。但是不裁边的话很多论文，特别是比如PR系列的，公式就会很小。所以还是要裁边的，所以我还是需要裁边的。

搜索了下还是有不少工具的，但是还是这个博客介绍的最靠谱[Linux 下裁剪pdf文件白边的简单命令](https://linhan.blog.ustc.edu.cn/?p=196)。

总结下就是

```
pdfcrop input.pdf output.pdf 

```

当然一般还是要留一点白边的.

```
pdfcrop --margins 10 input.pdf output.pdf 
```

虽然最后打印的文档会变大，但是对于我来说无所谓，本来这样的裁边文件就只是为了打印而不需要存储。

当然如果你需要存储在移动设备中使用可能还需要参照博客的介绍用重新打印减小体积。

给出一个Bash脚本方便批量操作:

```bash

#! /bin/bash 

count=0

for f in *.pdf; do
    let count++
    name="output$count"
    pdfcrop --margins 10 $f $name.pdf 	
done

echo "Done"

```
