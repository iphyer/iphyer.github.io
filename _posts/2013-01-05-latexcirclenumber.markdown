---
layout: post
title: "latex中输入20个带圈字符的方法"
date: 2013-01-05 22:34
comments: true
categories: Latex
---

# 前言

今天写专利课老师的论文，发现必须要求我们遵循《中国法学》的文献格式要求。
这里小不爽一下，就是这本杂志要求

> （二）文中注释一律采用脚注，全文连续注码，注码样式为：①②③等。

本来以为这个在latex里面可以集成了功能结果发现特别痛苦啊，有么有！！

<!--more-->

# 实现

latex有几个包可以实现这个功能，比如很多人推荐的\fnsymbol和\textcircled{\scriptsize 1}或者还有 pifont 包的 \ding{} 命令。

但是\fnsymbol命令太过复杂了，\textcircled{\scriptsize 1}要一个个手动的判断具体的字符大小，太烦。pifont 包的 \ding{} 命令确实不错，但是每页只能支持10个同时还有不可以连续编号的限制，舍弃。

后来发现了这个 [LaTex中带圆圈脚注或带圆圈文本](http://vardesa.blog.hexun.com/58537832_d.html "LaTex中带圆圈脚注或带圆圈文本") 确实是太棒了！

可以说各种需要的情况所需要使用的命令都给出来了。
所以基于这个生成了以下的代码，支持符合《中国法学》格式要求的脚注标示。最多支持到20，再多的，请自行使用word等的带圈字符功能添加后重新粘贴进来。


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

\makeatletter
\newskip\@footindent
\@footindent=1em
\renewcommand\footnoterule{\kern-3\p@ \hrule width 0.4\columnwidth \kern 2.6\p@}

\long\def\@makefntext#1{\@setpar{\@@par\@tempdima \hsize
\advance\@tempdima-\@footindent
\parshape \@ne \@footindent \@tempdima}\par
\noindent \hbox to \z@{\hss\@thefnmark\hspace{0.2em}}#1}
\renewcommand\thefootnote{\myfootnotestyle{\arabic{footnote}}}
\def\@makefnmark{\hbox{\textsuperscript{\@thefnmark}}}
\newcommand\myfootnotestyle[1]{\ifcase#1 \or ① \or ② \or ③ \or ④ \or ⑤ \or ⑥ \or ⑦ \or ⑧ \or ⑨ \or  ⑩ \or ⑪ \or ⑫ \or ⑬ \or ⑭ \or ⑮ \or ⑯ \or ⑰ \or ⑱\or ⑲ \or ⑳ \else *\fi\relax}
\makeatother
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


把上述代码直接加入序言部分，在正文部分正常使用\footnote{content}的语法就可以生成最后的效果如下：


![tu1](/images/Latex/带圈字符脚注.png)


## 必须改字体的问题

今天重新使用了，latex作测试的时候把脚注加到大于10的时候做了新的测试，结果发现除了bug还是没有办法解决。
在上网提问后知道原来这样不能大于10的限制还是和每个不同的字体本来的设计有关的。
有个字体本身就不支持大于10的带圈字符，所以即使这样设置了也没有办法。

从[这个帖子得到解答](http://bbs.ctex.org/forum.php?mod=viewthread&tid=74491&pid=443704&page=1&extra=page%3D1#pid443704)

换了新的Linux Libertine O字体。

这个字体其实并不是想wiki百科说的libreoffice自带，必须在Ubuntu的仓库里面搜索后重新安装。

但是这样还是不行。

问题就处在我的texlive上。我的texlive还是texlive2009，没办法当时懒，直接使用了仓库里面的texlive。

## 升级texlive

可以参考这个帖子，非常棒。[对于Ubuntu系统](http://blog.sina.com.cn/s/blog_6d0984870101961n.html#bsh-24-178876407)

按着这个一步步来，缺少包的话就按照后半部分教程重新安装即可。

## 最后效果

![tu1](/images/Latex/new.png)



