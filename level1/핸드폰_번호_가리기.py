#!/usr/bin/env python
# coding: utf-8

# In[ ]:


### https://school.programmers.co.kr/learn/courses/30/lessons/12948

def solution(phone_number):
    answer = ''
    phone_number_len = len(phone_number)
    answer = '*' * (phone_number_len - 4)
    answer += phone_number[-4:]
    return answer

