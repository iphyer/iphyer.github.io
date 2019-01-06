---
layout: post
title: "2018博客更新记录——从 Octopress 迁移到 Jekyll"
date: 2019-01-01 15:56
comments: true
categories: 技术
---

# 起因

刚刚趁着年底把博客更新了一下，主要是从 [Octopress](http://octopress.org/) 迁移到 [Jekyll](https://jekyllrb.com/)。

主要原因是 Octopress 已经好久不更新了，很多库都已经不支持了。很多时候，当我更新了系统的配置的 Ruby，那么整个博客就会失效。其实 Octopress 也是基于 Jekyll 的，但是后者的维护做得好很多。 Octopress 已经 3 年不更新维护了，实在是需要更新换代。同时，Octopress 用了大量我用不到的插件，虽然用着不错，但是太臃肿了，不太喜欢。

当然 Jekyll 很多时候也需要自己配置不少，所以我选择了 [jekyll-now](https://github.com/barryclark/jekyll-now) 这是一个宣传自己可以在几分钟内使用的博客，我自己测试了下确实不错。

用了 6 年的博客，终于第一次大更新。这里记录下过程和注意点。

<!--more-->

# 技术要求

任何时候，迁移或者升级都是一个选择问题，所以我这里说说自己的选型考虑。

## 1. 支持 Github

因为我原来的博客是基于 Github 的，所以这次更新也需要基于 Github ，这样可以保证自己的很多链接不失效。

## 2. 和 Octopress 配合(Markdown, Google Analytics，Disqus)

因为我之前是基于 Octopress 写了 6 年，积累了大量的 Markdown 博客文本，所以有一些基础服务我希望能够支持，主要是 Google Analytics 和 Disqus， 一个负责网站的数据统计，一个是评论记录。

## 3. 使用方便快速

我也看了不少技术方案，感觉还是 [jekyll-now](https://github.com/barryclark/jekyll-now) 设计的最为简单也最方便使用。同时希望代码结构不要太过于复杂，毕竟只是一个博客，不需要一个完整的网站架构。

# 更新步骤

其实按照 [jekyll-now](https://github.com/barryclark/jekyll-now) 的博客非常简单地就可以安装使用。这里不再缀叙。

说两个需要自己调节的。

### 1. 博客的内部链接方式

因为我的 Octopress 使用的日期+标题的方式命名，所以我们需要修改下内部的博客链接。

修改 `_config.yml` 文件中的 `permalink` 选项如下格式，这个需要根据原来的博文源文件命名方式修改。

```bash

permalink: /blog/:year/:month/:day/:title/

```

### 2. 添加 LaTeX 支持

因为写的博文经常会用到 LaTeX， 所以需要修改下原始文件的配置，使之支持 LaTeX.

这里我选择了使用 [MathJax](https://www.mathjax.org/) 来支持公式。[MathJax](https://www.mathjax.org/) 是一个支持在网页中渲染 LaTeX 公式的 JS 框架。

使用也非常简单，修改 `_layout/post.html` 文件，`post.html`是一个生成博客帖子的模板文件，这里只需要在模板文件中包含 [MathJax](https://www.mathjax.org/)。 修改了后的文件如下，...是省略的模板代码。

```html

---
layout: default
---

<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML' async></script>


<article class="post">
...
</article>


```

使用的方式就是连用两个$符即可。我发现和 MathJax 官网的使用有些不同，我猜测是单$被博客引擎占用了，不过不影响使用，所有地方都是用双$符号即可。行内公式和行间公式都可以。

比如 Schrödinger equation

$$
\hat H \Psi=i \hbar \frac{\partial}{\partial t}\Psi 
$$

Dirac 方程

$$
i \hbar \gamma^\mu \partial_\mu \psi - m c \psi = 0 
$$

效果还不错。

当然也可以使用行内公式，比如  

When $$a \ne 0$$, there are two solutions to $$ ax^2 + bx + c = 0 $$ and they are
$$x = {-b \pm \sqrt{b^2-4ac} \over 2a}.$$。