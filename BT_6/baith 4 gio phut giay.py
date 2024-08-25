# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 16:07:21 2024

@author: PHANTHITHUONGHOAI
"""
thoi_gian = input("Nhập thời gian (hh mm ss): ")
gio, phut, giay = map(int, thoi_gian.split(' '))
tong_giay = gio * 3600 + phut * 60 + giay
print("Tổng số giây là:", tong_giay)


