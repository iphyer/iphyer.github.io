---
layout: post
title: "Matplotlib 移除白边"
date: 2019-07-28 17:44
comments: true
categories: Leetcode
---

## 前言

需求很简单就是需要在 Python 的做图中，生成的图片都是不含白边的。

参考这个帖子解决了问题，[Removing white space around a saved image in matplotlib](https://stackoverflow.com/questions/11837979/removing-white-space-around-a-saved-image-in-matplotlib/27227718)。

<!--more-->

发现最有效的答案不是高分那个，那个答案还是需设置才行。

但是后面的答案还是更加有效。

```python

plt.axis("off")

fig=plt.imshow(image array,interpolation='nearest')

fig.axes.get_xaxis().set_visible(False)

fig.axes.get_yaxis().set_visible(False)

plt.savefig('destination_path.pdf',bbox_inches='tight', pad_inches = 0, format='pdf', dpi=1200)

```

记录下，这个更加简单也高效。