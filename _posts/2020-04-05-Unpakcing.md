---
layout: post
title: "Python the unpacking operator and how to use it to traverse grids"
date: 2020-04-05 13:16
comments: true
categories: Python
---

## Introduction

I am learning [Leetcode 807. Max Increase to Keep City Skyline](https://leetcode.com/problems/max-increase-to-keep-city-skyline/) and I encounter the following code for getting the maximum column and row for the input 2D grid.

So in the official answer, to get the column maximum values of each column, the following code is used,

```python

    grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
    row_maxes = [max(row) for row in grid]
    col_maxes = [max(col) for col in zip(*grid)]
    print(col_maxes)

```

The Output is `[9, 4, 8, 7]` which is correct but why?


<!--more-->

## Answer

Usually, `zip(*var)` is used for unzipping some list of tuples, so it is like what was described in this post [Transpose/Unzip Function (inverse of zip)?](https://stackoverflow.com/questions/19339/transpose-unzip-function-inverse-of-zip) because the list is iterable, so each list in the list will be iterated to generate the new list? And it is not required that the iterable must be a tuple, and then actually col is a tuple.

```python

    >>> for col in zip(*grid):
    ...     print(col)
    ... 
    (3, 2, 9, 0)
    (0, 4, 2, 3)
    (8, 5, 6, 1)
    (4, 7, 3, 0)

```

However, if you test this code:

```python

    >>> for col in zip(grid):
    ...    print(col)
    ... 
    ([3, 0, 8, 4],)
    ([2, 4, 5, 7],)
    ([9, 2, 6, 3],)
    ([0, 3, 1, 0],)
```

The function `*` in Python is that it is the unpacking operators. And more details is here [Python args and kwargs: Demystified](https://realpython.com/python-kwargs-and-args/#unpacking-with-the-asterisk-operators)

> **Unpacking With the Asterisk Operators: * & ****

> You are now able to use *args and **kwargs to define Python functions that take a varying number of input arguments. Let’s go a little deeper to understand something more about the unpacking operators.

> The single and double asterisk unpacking operators were introduced in Python 2. As of the 3.5 release, they have become even more powerful, thanks to PEP 448. In short, the unpacking operators are operators that unpack the values from iterable objects in Python. The single asterisk operator * can be used on any iterable that Python provides, while the double asterisk operator ** can only be used on dictionaries.

## Conclusion

The take away is easy, you need to know how to find the maximum values in a 2D list array of Python in two lines of code. The


```python

    row_maxes = [max(row) for row in grid]
    col_maxes = [max(col) for col in zip(*grid)]

```