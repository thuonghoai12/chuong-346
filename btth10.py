# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 13:21:54 2024

@author: PHANTHITHUONGHOAI
"""
car_number = int(input("Nhập biển số xe của bạn (4 chữ số) vào đây: "))
hang_nghin_01 = car_number // 1000
hang_tram_01 = car_number // 100 % 10
hang_chuc_01 = car_number // 10 % 10
hang_don_vi_01 = car_number % 10
sum_01 = hang_nghin_01 + hang_tram_01 + hang_chuc_01 + hang_don_vi_01

hang_chuc_02 = sum_01 // 10
hang_don_vi_02 = sum_01 % 10
sum_02 = hang_chuc_02 + hang_don_vi_02

hang_chuc_03 = sum_02 // 10
hang_don_vi_03 = sum_02 % 10
sum_03 = hang_chuc_03 = hang_don_vi_03

print(f"Số xe của bạn có {sum_03} nút!")
