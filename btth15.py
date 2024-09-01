# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 17:38:42 2024

@author: PHANTHITHUONGHOAI
"""
a = float(input(" Nhập giá trị a = "))
b = float(input(" Nhập giá trị b = "))
A = ((a + b) / (pow(a, 1/3) + pow(b, 1/3))) - pow(a * b, 1/3)
B = pow(pow(a, 1/3) - pow(b, 1/3), 2)
print("Kết quả phép tính là: ", round(A / B, 3))
