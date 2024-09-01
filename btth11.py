# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 14:18:47 2024

@author: PHANTHITHUONGHOAI
"""
ky_tu_thuong = input("Nhập vào đây ký tự thường: ")
ky_tu_hoa = ky_tu_thuong.upper()
if ky_tu_thuong.islower():
    print("Ký tự viết hoa tương ứng là: ", ky_tu_hoa)
else:
    print("Vui lòng nhập lại ký tự thường!")
    