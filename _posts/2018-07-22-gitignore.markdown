---
layout: post
title: "gitignore忽略Mac的DS_store文件"
date: 2018-07-22 00:16
comments: true
categories: git
---

其实很简单的，参考这个帖子[How can I Remove .DS_Store files from a Git repository?](https://stackoverflow.com/questions/107701/how-can-i-remove-ds-store-files-from-a-git-repository),这里记录下。


<!--more-->

## 清除已经记录的文件

```bash
find . -name .DS_Store -print0 | xargs -0 git rm -f --ignore-unmatch
```

## 以后不记录该文件

```bash
echo .DS_Store >> .gitignore
git add .gitignore
git commit -m '.DS_Store banished!'
```
