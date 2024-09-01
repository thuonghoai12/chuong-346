# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 02:31:19 2024

@author: PHANTHITHUONGHOAI
"""
thoi_gian = input(" Nhập giờ phút giây (hh:mm:ss) vào đây: ")
gio, phut, giay = map(int, thoi_gian.split(":"))
if 23 >= gio >= 0 and 59 >= phut >= 0 and 59 >= giay >= 0:
    print("Thời gian hợp lệ!")
else:
    print("Thời gian không hợp lệ!")
    