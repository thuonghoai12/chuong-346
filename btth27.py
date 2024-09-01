# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 03:33:19 2024

@author: PHANTHITHUONGHOAI
"""
import math
H = input("Nhập hình: ")
if H == "hcn":
    print("Tính S và P của hình chữ nhật")
    a = float(input("Chiều rộng: "))
    b = float(input("Chiều dài: "))
    S = a * b
    P = (a + b) * 2
    print(f"Kết quả: Diện tích = {S}, Chu vi = {P}")
elif H == "hv":
    print("Tính S và P của hình vuông")
    a = float(input("Độ dài cạnh: "))
    S = a ** 2
    P = a * 4
    print(f"Kết quả: Diện tích = {S}, Chu vi = {P}")
elif H == "ht":
    print("Tính S và P của hình tròn")
    r = float(input("Bán kính hình tròn: "))
    S = pow(r, 2) * math.pi
    P = 2 * math.pi * r
    print(f"Kết quả: Diện tích = {S}, Chu vi = {P}")
else:
    print("Hình không hợp lệ! Vui lòng nhập 'hcn', 'hv' hoặc 'ht'.")
          

    