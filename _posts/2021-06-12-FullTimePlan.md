---
layout: post
title: "FullTime Job Plan"
date: 2021-06-14 23:49
comments: true
categories: 工作
---

这里总结下自己在这个实习中想实现的一些目标和注意事项。主要参考了这么三个帖子，

* [东部不知名学校BA专业New Grad四个月时间找湾区非主流大厂DS岗超详细经验分享](https://www.1point3acres.com/bbs/thread-589653-1-1.html)
* [SDE上岸的经验贴，有你想不到的套路，楼主说的都是大实话](https://www.1point3acres.com/bbs/thread-609783-1-1.html)
* [狗家 offer 已签，分享下心得和 filter](https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=446715&fromguid=hot&extra=&mobile=2))
* [“硬”闯谷歌之路](https://www.1point3acres.com/bbs/thread-538502-1-1.html)
* [转专业一年找工终于上岸, 心路历程和经验分享!](https://www.1point3acres.com/bbs/thread-528402-1-1.html)

<!--more-->

# Timeline -- Be an early bird

最终目标

* BayArea + big name + DS
* Austin + big name + DS
* Chicago + big name + DS
* AnyLocation + big name + DS
* AnyLocation + big name + SDE

1. 准备简历等自己的profile
2. 8-9月 连续的，大量的，高质量的申请和电话面试
3. 10月-11月 面试
4. 毕业前时间(11月)，如果不行，寻找 contractor

> 有了这个找工作最终目标后，开始从后往前推有个时间线，比如12月毕业，那就是尽量在这之前找到工作，找不到还有 OPT Grace period 三个月，也就是最晚四月底就要被赶回国。这个毕业的时间点就是找工作的时候一个重要的节点，如果到毕业的时候还找不到工作，就开始在大厂找 Contractor 作为自己的最后的保险方案。

> 这个过程是个dynamic的过程，一边往前走一遍修正自己之前准备的东西

# 简历

## 关键词填充

楼主自己就是udemy上项目比如web develop bootcam+ react, redux 然后慕课网的java spring boot 项目. 瞄准的是fullstack和backend.套用这个 使用了什么框架+ 做了什么+ 达到什么目的/feature这个模板去写你的简历内容.
然后建议简历适当”包装”一下, 这也不是说让你去作假, 而是能加上一下比较好的框架和feature. 这样会吸引hr的眼球 让他找到关键词.然后你的feature里 最好能展现出你对这个框架有advacned 理解, 比如一些plugin的使用, 一些performance的提升.

## 项目选择

建议至少有三个软件相关的Projects：一个数据库，一个网站，一个其他（Big Data, Machine Learning, 游戏等等）。
简历是一个绝对头疼的东西，不管你的简历多好，挂在地里大家肯定能指出一大堆问题，而且说得不一定对。

如果你实在一个拿得出手的Project都没有，我有以下几点建议：

1. 在Udemy报一个Web development的课，肯定能出一个project.

2. 报一个big data的班，能出两三个Hadoop的projects.

3. 把自己工作时的东西“软件包装”。比如你平时的工作时技术支持，要记录用户的问题，那你就说你使用数据库来记录。当然我们不要骗人，最好真的自己搭一个数据库。再比如你平时做实验需要run三样东西，你就说你用script来run这些东西。同样的，建议你真的写script来试试run。

你一定要有一个自己特别了解的Project，面试时几乎100%会被问题，目的是考你是否能讲清楚一样东西，具体内容不重要。

# 内推

## 一亩三分地

> 先看各位大神post的时间，一般post超过3-7天的就最好不要投了，最佳的投递时间是几个小时或者1-2天之内。你看到可能没几个人给大米点赞，殊不知大神的邮箱已经爆了。

# 面试顺序

我计划的面公司的顺序是这样的：

1. 几乎不想去的公司（Ebay, Walmart, Cisco, Pure Storage等等）。
2. 喜欢但是很远的公司（Uber, Lyft, Pinterest, Yelp, Salesforce, Twitter等等）。
3. 喜欢的公司（Microsoft, Apple, Tesla, PayPal等等）。
4. Dream Companies（Google, Facebook, LinkedIn, Amazon, Netflix等等）。

楼主找工作整体有一个strategy，把在美国找工作的结果分为四个梯度：

* 第一梯度，湾区大厂
* 第二梯度，湾区startup
* 第三梯度，其他地方大厂或小厂
* 第四梯度，湾区大厂contractor

# 编程面试

> 时间的话，我训练的标准是 easy 10 mins，medium 20 mins， hard 30 mins。如果没有按时写完，用 easy 5m, medium 10m, hard 15m 的时间看 discussion board。如果还没看懂，就把题目记下来，以后多看几遍。


1. 多搜面经、知己知彼

在面试前，你要多搜下面经，看看要应聘的公司的面试题难易程度和面试官的喜好，有针对性的准备。比如有的公司喜欢面试动态规划，面试前就去leetcode多刷下这类题目，有的公司的算法面试比较简单，面试前找简单题目练一下就好了。当然，这个只是为了有个大概的了解，要想压到题目还是很难的。因为很多公司，比如Google，要求如果某个题目已经被泄露，坚决就不能再被使用。
 
2. 练习白板编程

我们平时都是在IDE中写代码。IDE本身有自动提示功能，而且可以随意修改代码。但是，在面试中，我们一般都是在白板或者纸上写代码。而在纸上写代码，对整洁度的要求很高，因为写好之后就不好改了，不然改的乱七八糟，面试官会觉得你思路混乱。所以，在面试前，你要在纸上多练习一下，能够做到脑袋里想好算法之后，能一气呵成的写出代码。如果实在写的太乱，写完之后，再重新抄一遍。所以，去面试的时候，自己多准备几张白纸，以免面试官给你的纸不够用😂。
 
3. 尽量保证代码没有bug

实际上，算法面试不仅仅考察你的算法能力，还考察你的代码能力。你的代码是否能做到bug free这个非常关键。在面试中，如果你写出来的代码，bug很多，即便算法正确，也不大可能被录用。所以，在写代码的时候，你一定要注意非法输入的判断、一些特殊边界情况的处理。在写完代码之后，你也要认真检查一遍，并且用测试用例检查一下你的代码是否能运行正确。测试用例起码要包含正常情况、错误情况、以及一些边界情况（corner case）。
 
4. 尽量保证代码规范

除了刚刚说的代码要没有bug之外，你还需要注意代码规范，比如变量、函数的命名一定要规范，可读性强。大的代码片段要拆分成小的函数、模块，这样不管是面试官读你的代码，还是你自己写代码，都会比较清晰些。如果你代码写的不规范，有些面试官会因此联想到你工作中写代码是不是也不规范呀。
 
5. 要有时间意识

实际上，面试官不只是看你是否能想出算法、写出答案，对于一些简单算法题目，面试官还会考察你是否能快速写出代码。如果简单题目都写的磕磕绊绊，在很多优秀的候选人中，你就很难脱颖而出了。一般来讲，一个算法题目的思考时间不能超过10分钟（不包括代码实现）。超过10分钟，你就会紧张，面试官也会等的不耐烦了😂。所以，很长时间想不到解题思路的时候，要多个面试官沟通下。
 
6. 先用最简单的方法解决

一般来说，我的一个面试习惯是，拿到一道算法题目之后，先想最简单的解决办法，说给面试官听，然后再行优化，想更加好的解决方案。这样做的目的，一方面是缓和自己紧张的情绪，不至于脑袋放空、卡壳，另一方面，一开始就想最优的解法，可能要闷头想很久，面试官很难知道你的进度，也没法做指导。

## coding interview 的详细过程

- 开场：不卑不亢。你就假装其实你已经有了另一个FLAGUAP的Offer了，就不会太患得患失的，你的气场会感染面试官的。见过太小心的面试者，第一印象不好。

- 其他大厂也许不一样，但是狗家技术面寒暄之类的都是过场，所以你的回答别太长了，因为你占用的是自己一会儿解题的时间。但也别就两句话，自己把握吧。亚麻有LP内容，还是需要认真答的，但是面试官应该给你留够时间解题。

- 一定要重复题目，确认要求，甚至确认sample input/output。然后问一些edge cases，这样一来表明你的确有考虑这些问题（面试官在等你说呢），二来也是给你自己时间想题目了。

- 思考过程千万不要沉默，也不能完全的自言自语（因为他需要听你的思考过程）。如果你会紧张，把面试官想像成你的teammate或者一起做题的小伙伴（就是那种你熟悉的，给你信心的场景），你们一起来解这道题，你给他讲解你的想法。

- 先在白板上把你的数据结构和算法解释了，给出space and time complexity（别等人问）。 不要马上写code。 如果你秒杀暴力算法，就直接接着优化吧. 有的题目很明显是要优化的，但是你还是可以很快的提一下暴力解法。Of course you are not looking for this brute force implementation. OK, this can be optimized by .... 展示一个有层次的分析问题的过程，远远好于上来就提出最优解。多说话才能展示你对不同数据结构和算法的掌握啊。Communication在打分里是和data structure，algorithm并列的一项，你说有多重要。

- 开始写code之前问一下：should I start implement it in code, or you want me to conitnue to optimize it? 这样你也大概知道你的位置和面试官的期待在哪里
。

- 写完code一定要跑test cases，不是盯着你的code自己看，要说出来。你刚开始问的那些edge cases就是一个提醒。

- 字迹不要太潦草。你不赶时间，除非你思如泉涌怕自己忘了。一些null checking的无聊但是必须的语句，在征得面试官同意的情况可以只写一个comment： // check null etc... (May I skip these checks to save time?). 但是这个comment一定要写，否则面试官可能写报告的时候会忘记。

- class和变量名不要那么长，给自己找麻烦，但是需要解释一句，免得面试官对你的coding style有疑问（sorry I will keep the variable names short just for convenience. In real code I will sure use more descriptive names).

# System Design

常用的设计题参考了网上的各个资源，都写了自己理解的答案，这里我写的有tinyurl, twitter，messenger，uber，youtube，typeahead，dropbox，yelp，web crawler，search engine，rate limiter，key value store，instagram，online chess game

# Other Tips

## Form a team

> 我在整个找工作开始之前，就和班里的同学组了一个五人小队，大家都从六七月份就开始定期互相批改简历，做项目，上AB/testing的课程，分享找工作的资料，资源，一起去GHC career fair，总之就是一路互帮互助。这些实际的练习是一方面，另一方面就是有了伙伴来帮助，能够帮助自己在精神上不会崩溃。

## Consistency

> 所有的策略，技巧，方法，都需要consistency，需要你持之以恒，每日如一的去做，再好的方法遇到三天打鱼两天晒网都是没有用的。

## Regularly workout

>找工作还是挺辛苦的，每天都是大量的时间投入，一坐就是好几个小时，所以每周定期去运动运动还是很有帮助的。

## 别犹豫，行动起来


