---
layout: post
title: "Reading Notes of Grokking Deep Learning Chapter 1 to 3"
date: 2019-04-19 19:36
comments: true
categories: Deep Learning
---

## Foreword

I usually use Chinese to write this blog but then I gradually learned that it would be a good idea if I could use English more to summarize all the ideas and personal thinkings in English. So from this blog, I will switch to use English mainly unless there is no need to use it.

So this is reading summary notes about the book *Grokking Deep Learning* book, a book I am currently reading and enjoy it a lot. So I will spend time to summarize some key points I like here.

<!--more-->

## About the book

*Grokking Deep Learning* is a book written by Andrew W. Trask and it tries to explain concepts, math, and coding in deep learning with simple Python/Numpy codes which is a great source I think everyone should try to learn. With the advancement of the deep learning community, we can build a deep learning network in less than 10 lines of codes but this is not the best way to learn things. This book is exactly the opposite. It opens all the details of deep learning with simple but not simpler Python codes. And the book uses great figures and easy English to help you understand deep learning and as little math as possible to avoid intimidating the beginners. I strongly recommend this book if you are new to the deep learning word.

And a few personal comments, this book is very good at the first part from beginning chapters to the chapter of CNN but the second half especially the LSTM and NLP part is not very good. This is the first book introducing LSTM without any figures which are quite strange and not reasonable. I think the author needs to improve that part and if it is due to length limitations, he needs to drop NLP or uses simple examples than LSTM.  

## Chapter 1 - 3 Summary

### Chapter 1

Chapter 1 introduces deep learning and talks about why you should learn deep learning and the logistics of the book. So no need to summarize.

### Chapter 2

Chapter 2 talks about some basics of deep learning to help newcomers learn the basics of this area which is quite concise and direct. The author focus on the differences between supervised learning and unsupervised learning. He also discusses parametric learning and non-parametric learning although I believe he can drop the parametric/non-parametric discussion since he actually completely omits discussion about the non-parametric part which means there is no need to put the notation non-parametric here. Also, a small suggestion, it would be great if he can discuss reinforcement learning a little bit since this is the most heated topic in both academic and industrial nowadays.

### Chapter 3

First, a neural network is just another way to say how to do weighted sum of different input and there is nothing special here. We do not need to consider NN as a too complex thing it is just a way to say that you have different measure values and you want to come up with a better way to summarize them or represent them so you use NN to do a weighted sum of all those different values.

Second, although we understand NN as a weighted sum of different values, it does not mean you can only do a sum for the input. Actually, there is completely normal that we have one input value but three output values. All you need is just a three components vector to represent the weights. So this is also a "weighted sum" although the form looks completely different.

Thirdly, since NN can be understood as a form of weighted sum, it is natural to stack them layer by layer which leads to the name network. And still here is just a weighted sum of previous weighted sum.

Finally, we need to understand how to use Numpy to vectorize all the computations in deep learning which is the great help in speed. 

Key Point List:

* **Input** is the *information* we have, **weight** is the *Knowledge* we know in advance, and **prediction** is the *final results* we want.
* You can also understand NN as the NN gives scores for the inputs based on how similar they are to the weights. This is another way to understand the weighted sum.
* The prediction of NN is also called forward propagation and it can be understood as a form of the weighted sum of information and previous knowledge.