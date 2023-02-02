---
layout: post
title: "Scala 学习总结"
date: 2022-12-05 23:54
comments: true
categories: 工作 学习
---

最近常用 Scala 这里总结下自己在使用中觉得值得注意的地方。

<!--more-->

## Scala 中 Join 的用法

如果我们希望在 Scala 里 join 两个 dataframe 常见的结果是会多出几列如果你直接按照官方语法操作。这里其实是因为你使用的方法不对。参考这个帖子得到更多细节，这里我只总结下最基本的语法和操作。

[How to avoid duplicate columns after join?](https://stackoverflow.com/questions/35258506/how-to-avoid-duplicate-columns-after-join)

最重要的答案就是

> perform the join where the joined columns are expressed as an array of strings (or one string) instead of a predicate.

也就是指定两个 Dataframe 按照哪几列 join

```scala
left.join(right, Seq("firstname", "lastname"))
```

而不是 left.column == right.column 。

```scala
left.join(right, left("firstname")===right("firstname") &&
                 left("lastname")===right("lastname"))
```

当然 Scala 值得学习的东西还有很多，比如 join 就有 6 种，参考这个 [Introduction to Join in Spark SQL](https://www.educba.com/join-in-spark-sql/) 


* INNER JOIN
* CROSS JOIN
* LEFT OUTER JOIN
* RIGHT OUTER JOIN
* FULL OUTER JOIN
* LEFT SEMI JOIN
* LEFT ANTI JOIN

## 在不对称 Dataframe，一大一小 DF 的 join 中积极使用 Broadcast Joins

参考资料 [Broadcast Joins in Apache Spark: an Optimization Technique](https://blog.rockthejvm.com/spark-broadcast-joins/)

其实最大的核心是，在 Join 中，为了保证结果的正确性，我们需要 Loop Through all records to find matching ones。 所以原来的帖子中说，

> Normally, Spark will redistribute the records on both DataFrames by hashing the joined column, so that the same hash implies matching keys, which implies matching rows.

而 Boradcast 的核心就是把小数据集在每个 Spark 核心上复制一遍，这样可以保证小数据集都被遍历。那么寻找 matching pairs 的任务也完成了。

在 Large-Small Join Problem 中，往往复制小数据集的开销可以忽略不计。所以 Broadcast 可以大大加速 Join。

事实上 Spark 对于小于 10 MB 的数据集有自动的开启 Broadcast 优化，但是对于 local 的 DataFrame 这个不会打开，因为测量数据集大小本身就是 O(N) 的开销。

> In many cases, Spark can automatically detect whether to use a broadcast join or not, depending on the size of the data. If Spark can detect that one of the joined DataFrames is small (10 MB by default), Spark will automatically broadcast it for us. 

> Spark will not determine the size of a local collection because it might be big, and evaluating its size may be an O(N) operation, which can defeat the purpose before any computation is made.

> Spark will perform auto-detection when

> * it constructs a DataFrame from scratch, e.g. spark.range
> * it reads from files with schema and/or size information, e.g. Parquet

