# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 21:54:08 2024

@author: PHANTHITHUONGHOAI
"""
N = int(input(" Nhập số nguyên dương N có hai chữ số: "))
hang_chuc = N // 10
hang_don_vi = N % 10
tong_hai_chu_so_N = hang_chuc + hang_don_vi
if 99 >= N >= 10:
    print(" Kết quả tổng hai chữ số của N là : ", tong_hai_chu_so_N)
else:
    print(" Vui lòng nhập lại!")
