# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 16:00:49 2024

@author: PHANTHITHUONGHOAI
"""

N = int(input(" Nhập số nguyên dương N có 2 chữ số ="))
chu_so_hang_don_vi = N % 10
chu_so_hang_chuc = N // 10
tong = chu_so_hang_don_vi + chu_so_hang_chuc
print(" Tổng các chữ số N =", tong)

