# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 23:57:41 2024

@author: PHANTHITHUONGHOAI
"""
from datetime import datetime
nam_sinh = int(input("Nhập năm sinh của bạn: "))
nam_hien_tai = datetime.now().year
tuoi = nam_hien_tai - nam_sinh
print(f"Bạn sinh năm {nam_sinh}. Vậy năm nay bạn {tuoi} tuổi! ")
