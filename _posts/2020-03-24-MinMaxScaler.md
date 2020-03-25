---
layout: post
title: "Research Notes2: Model Persistence Issue in Machine Learning"
date: 2020-03-24 18:16
comments: true
categories: 科研
---

## Introduction

Today I met this problem and had to slow down my work to rerun some of my models to make sure everything works as expected when I tried to train the machine learning model. The problem is that when I trained the neural network, I forgot to save the preprocessing results like the `MinMaxScaler()` I used, so this caused a huge problem that I had to retrain everything to make sure the model works correctly. 

## Deploy Machine Learning Models

Although this is not an error, it is a big pitfall in your typical training of machine learning. The typical machine learning course tends to focus on the algorithm and mathematical reasoning behind the model, it does not tell you how to deploy the model. This is reasonable because actually nowadays, there are no golden rules about how to deploy machine learning models. 

Deploying a machine learning model is still at its stone ages. The problem is even harder to solve if you take the software dependency issues into consideration. For example, after you trained a good machine learning model, how could you provide it to the public? Assuming there are $10^6$ users who want to use your service, how could you optimize the codes to reduce the latency and computing workload? How to help the user input the correct format of their own data? Is there any method to deal with vicious intention users? 

Actually, if we want to go deeper into the ideas of deploying your machine learning model, it will go to the area of computer systems which is rapidly changing and actively researched areas of computer science. Taking one example, I learned one course in UW-Madison that is taught by Prof. Shivaram Venkataraman in Fall 2018, [CS 744 Big Data Systems - UW Madison, Fall 2018](http://pages.cs.wisc.edu/~shivaram/cs744-fa18/), you can find an entire section goes to how to deploy machine learning models online, e.g. [Ray: A Distributed Framework for Emerging AI Applications](http://pages.cs.wisc.edu/~shivaram/cs744-readings/ray-arxiv.pdf).

![Deploy Machine Learning Models in CS 744](/images/MinMaxScaler/cs744.png)

Check out the article interested to you. 

## Model Persistence

So go back to this article, I want to talk about model persistence and how to make sure you have gotten everything you needed. Generally, it is about tips to help you save the training results successfully.

So three things I think we need to store are:

> Preprocessing Results 

> Neural Network results

> Training logs

so for preprocessing results, I think 
