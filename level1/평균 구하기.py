#!/usr/bin/env python
# coding: utf-8

# In[ ]:


### https://school.programmers.co.kr/learn/courses/30/lessons/12944
# 내가 푼 방법

def solution(arr):
    sum = 0
    for i in range(0,len(arr)):
        print(i)
        sum += arr[i]
    answer = sum/len(arr)
    return answer


# In[ ]:


# 통계모듈 이용하는 방법

import statistics

def solution(arr):
    return statistics.mean(list)


# In[ ]:


# reduce 모듈 이용

from functools import reduce

def solution(arr):
    return reduce(lambda x, y : x + y, list) / len(list)
    # **reduce, lambda 활용해서 직관적으로 표현 가능**

