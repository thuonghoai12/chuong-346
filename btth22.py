# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 23:56:58 2024

@author: PHANTHITHUONGHOAI
"""
a = float(input(" Nhập giá trị a = "))
b = float(input(" Nhập giá trị b = "))
if a == 0 and b == 0:
    print("Phương trình có vô số nghiệm")
elif a == 0 and b != 0:
    print("Phương trình vô nghiệm")
else:
    print("Phương trình có nghiệm duy nhất x = ", round(-b/a, 2))
    

