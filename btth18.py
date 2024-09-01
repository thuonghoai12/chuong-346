# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 04:15:57 2024

@author: PHANTHITHUONGHOAI
"""
thoi_gian_a = input("Nhập thời gian thứ nhất (giờ:phút:giây): ")
thoi_gian_b = input("Nhập thời gian thứ hai (giờ:phút:giây): ")
gioa, phuta, giaya = map(int, thoi_gian_a.split(":"))
giob, phutb, giayb = map(int, thoi_gian_b.split(":"))
tong_giay_a = gioa * 3600 + phuta * 60 + giaya
tong_giay_b = giob * 3600 + phutb * 60 + giayb

tong = tong_giay_a + tong_giay_b
hieu = tong_giay_a - tong_giay_b

gio_tong = tong // 3600
phut_tong = (tong // 3600) % 60
giay_tong = tong % 60
print(f"Kết quả cộng 2 thời gian: {gio_tong} giờ, {phut_tong} phút, {giay_tong} giây.")

if hieu < 0:
    print("Kết quả không hợp lệ (thời gian âm)") 
else:
    gio_hieu = hieu // 3600
    phut_hieu = (hieu // 3600) % 60
    giay_hieu = hieu % 60
    print(f"Kết quả trừ 2 thời gian: {gio_hieu} giờ, {phut_hieu} phút, {giay_hieu} giây.")

    
    



