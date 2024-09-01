# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 03:05:10 2024

@author: PHANTHITHUONGHOAI
"""
print("Bài 26a:")
a = int(input(" Nhập số nguyên a = "))
b = int(input(" Nhập số nguyên b = "))
c = int(input(" Nhập số nguyên c = "))
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, a
print(f"Thứ tự tăng dần của 3 số a, b, c lần lượt là {a}, {b}, {c}")
print("Bài 26b:")
N = int(input(" Nhập số nguyên N: "))
chuoi_so = str(N)
chuoi_sap_xep = ''.join(sorted(chuoi_so))
print("Kết quả các chữ số theo thứ tự tăng dần: ", chuoi_sap_xep)

