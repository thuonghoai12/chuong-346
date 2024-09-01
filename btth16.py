# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 19:08:42 2024

@author: PHANTHITHUONGHOAI
"""
thoi_gian = input("Nhập (giờ(h) phút(p) giây(s)) vào đây: ")
h, p, s = map(int, thoi_gian.split(" "))
tong_giay = h * 3600 + p * 60 + s
print("Tổng số giây: ", tong_giay)
