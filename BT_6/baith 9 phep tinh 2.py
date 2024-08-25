# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 16:00:25 2024

@author: PHANTHITHUONGHOAI
"""
import math
a = float(input("Nhập số a = "))
b = float(input("Nhập số b = "))
A = (math.sqrt(a) - math.sqrt(b)) / ((math.pow(a, 1/4)) - (math.pow(b, 1/4)))
B = (math.sqrt(a) + (math.pow(a*b, 1/4))) / ((math.pow(a, 1/4)) + (math.pow(b, 1/4)))
print("Kết quả phép tính = ", A - B)