---
layout: post
title: "Github Too Large File Deny"
date: 2019-02-05 22:13
comments: true
categories: 工作
---

今天 push code 到 Github 被拒绝了，真是比较恼火。Fix 这个问题花了好久，这里记录下怎么修复。


<!--more-->

# 原因

具体的原因其实很简单就是因为 Github 限制可以同步文件的 size, 100 MB，如果你不购买 Github 的大文件存储服务。


```Bash

remote: error: File Archive/Models/20181201/snapshot_model_100000.npz is 484.52 MB; 

this exceeds GitHub's file size limit of 100.00 MB

remote: error: File Archive/Models/20181202/snapshot_model_100000_20181202.npz is 484.48 MB; 

this exceeds GitHub's file size limit of 100.00 MB


```

# 解决办法

其实很简单的方法就是首先删除已经记录下来的文件，然后重新推送。

### 修改 `.gitignore`

当然 Git 本身考虑了这种情况，所以重要的一个概念是保持 `.gitignore` 的精准，一般你创建一个文件的时候就应该考虑是不是要记录该文件，所有不需要记录的文件可以放在 `tmp` 文件夹中，然后忽略该文件夹。


### 如何恢复 `.gitignore`

如果你遇到了大文件错误，其实你就已经记录了大文件的修改。这个时候需要从已经 commit 的修改中删除掉。

这次恢复在修改内部 Git 的缓存区花了大量的时间，最后其实是直接重置了 commit 的 HEAD 到提交之前，然后在重新提交。这样彻底恢复了 Git 的历史记录。

```bash

git filter-branch --index-filter 'git rm -r --cached --ignore-unmatch stage2' HEAD

```

参考这个 Stackoverflow 的帖子 [Can't push to GitHub because of large file which I already deleted](https://stackoverflow.com/questions/19573031/cant-push-to-github-because-of-large-file-which-i-already-deleted)

优点就是直接忽略掉你已经提交的历史，不需要处理复杂的内部循环删除问题。

当然再次 push 的时候需要用 `-f` 选项。

如果不太复杂的 commit 可以 `git rm --cached .idea`

[Clear git local cache](https://stackoverflow.com/questions/41863484/clear-git-local-cache)
