# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 14:34:07 2024

@author: PHANTHITHUONGHOAI
"""
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

tong = a + b
hieu = a - b
tich = a * b
thuong = a / b
chia_lay_du = a % b
chia_lay_nguyen = a // b
thuong_tron_2_chu_so = round(thuong, 2)

print("tổng hai số = ", tong)
print("hiệu hai số = ", hieu)
print("tích hai số = ", tich)
print("thương hai số= ", thuong)
print("làm tròn hai chữ số= ", thuong_tron_2_chu_so)

print("chia lấy dư = ", chia_lay_du)
print("chia lấy nguyên = ", chia_lay_nguyen)

