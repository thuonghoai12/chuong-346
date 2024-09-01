# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 21:18:08 2024

@author: PHANTHITHUONGHOAI
"""
a = int(input(" Nhập số nguyên a = "))
b = int(input(" Nhập số nguyên b = "))
c = int(input(" Nhập số nguyên c = "))
gia_tri_lon_nhat = a
if gia_tri_lon_nhat < b:
    gia_tri_lon_nhat = b
if gia_tri_lon_nhat < c:
    gia_tri_lon_nhat = c
print("Giá trị lớn nhất là: ", gia_tri_lon_nhat)
