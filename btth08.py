# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 00:50:11 2024

@author: PHANTHITHUONGHOAI
"""
import math
chieu_cao = float(input("Nhập chiều cao của bạn vào đây(m): "))
can_nang = float(input("Nhập cân nặng của bạn vào đây(kg): "))
BMI = can_nang / math.pow(chieu_cao, 2)
print("Chỉ số BMI của bạn là: ", round(BMI, 1))




