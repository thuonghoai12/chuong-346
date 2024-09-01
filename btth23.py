# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 02:20:56 2024

@author: PHANTHITHUONGHOAI
"""
import math
a = float(input(" Nhập giá trị a = "))
b = float(input(" Nhập giá trị b = "))
c = float(input(" Nhập giá trị c = "))
delta = (b * b) - (4 * a * c)
if a == 0:
    print("Phương trình có 1 nghiệm duy nhất x = ", -b/c)
else:
    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        print("Phương trình có nghiệm kép x1=x2= ", -b/(2 * a))
    else:
        print("Phương trình có nghiệm phân biệt x1 = ", (-b + math.sqrt(delta)) / (2 * a))
        print("Phương trình có nghiệm phân biệt x2 = ", (-b - math.sqrt(delta)) / (2 * a))