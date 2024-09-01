# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:41:09 2024

@author: PHANTHITHUONGHOAI
"""
time = input("Nhập ngày tháng năm (dd mm yyyy): ")
dd, mm, yyyy = time.split(" ")
print(f" Kết quả định dạng ngày tháng năm thứ nhất là: {dd}/{mm}/{yyyy}")
print(f" Kết quả định dạng ngày tháng năm thứ hai là: {dd}/{mm}/{(yyyy)[2:]}")
print(f" Kết quả định dạng ngày tháng năm thứ ba là: {yyyy}/{mm}/{dd}")
#ngược lại
dinh_dang_a = input("Nhập ngày tháng năm theo định dạng Ngày/Tháng/Năm: ")
dda, mma, yyyya = map(int, dinh_dang_a.split('/'))
print(" Kết quả định dạng a là: ", dda, mma, yyyya)
dinh_dang_b = input("Nhập ngày tháng năm theo định dạng Ngày/Tháng/2 số cuối của năm: ")
ddb, mmb, yyyyb = map(int, dinh_dang_b.split('/'))
if yyyyb > 50:
    yyyyb = yyyyb + 1900
else:
    yyyyb = yyyyb + 2000
print(" Kết quả định dạng b là: ", ddb, mmb, yyyyb)
dinh_dang_c = input("Nhập này tháng năm theo định dạng Năm/Tháng/Năm: ")
yyyyc, mmc, ddc = map(int, dinh_dang_c.split('/'))
print(" Kết quả định dạng c là: ", yyyyc, mmc, ddc)
