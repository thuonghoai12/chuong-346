# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 22:03:56 2024

@author: PHANTHITHUONGHOAI
"""
time = input("Nhập thời gian vào đây (hh:mm:ss): ")
hours, minutes, seconds = map(int, time.split(":"))
sum_seconds = hours * 3600 + minutes * 60 + seconds
print("Tổng số giây là: ", sum_seconds)
