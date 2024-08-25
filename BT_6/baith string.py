# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 15:32:56 2024

@author: PHANTHITHUONGHOAI
"""
nhap_chuoi = ("Đại học Quốc gia, Khu phố 6, P.Linh Trung, Q.Thủ Đức, Tp.HCM")
substrings_1 = nhap_chuoi.split(",")
print(substrings_1)
substrings_2 = nhap_chuoi.replace("P.", "" ).replace("Q.", "").replace("Tp.", "").split(",")
print(substrings_2)

