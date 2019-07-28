---
layout: post
title: "Reading Notes of Grokking Deep Learning Chapter 4"
date: 2019-04-21 23:21
comments: true
categories: Deep Learning
---

## Foreword

Following the last post, I will continue to summarize key points of Chapter 4 in this blog.

Nearly all supervised learning projects can be divided into 3 parts,

> predict, compare, learn

so chapter 3 focus on predicting part and chapter will focus on comparing and learning.

## Chapter 4

Simple Code and Simple Math but the concept is very important:

### Learning in brief

> Learning is adjusting the weight to reduce the error to 0!

> With derivatives, you can pick any two variables in any formula, and know how they interact! It is the sensitivity between two variables.

### Why learning rate alpha

> the simplest way to prevent overcorrecting weight updates!

Not solving the overshooting problem just a way to make weight update smaller. 

### Transfer Learning Benefits

The benefits of transfer learning:

* Transfer learning needs less training data
* Transfer learning makes the learned model generalizes better
* Transfer learning makes training process less brittle
* Transfer learning makes deep learning easier
