# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 19:42:54 2024

@author: PHANTHITHUONGHOAI
"""
a = int(input(" Nhập số nguyên a = "))
b = int(input(" Nhập số nguyên b = "))
c = int(input(" Nhập số nguyên c = "))
d = int(input(" Nhập số nguyên đ = "))
gia_tri_nho_nhat = a
if gia_tri_nho_nhat > b :
    gia_tri_nho_nhat = b
if gia_tri_nho_nhat > c:
    gia_tri_nho_nhat = c
if gia_tri_nho_nhat > d:
    gia_tri_nho_nhat = d
print("Giá trị nhỏ nhất là:", gia_tri_nho_nhat)
