# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:35:52 2024

@author: PHANTHITHUONGHOAI
"""
print("============* MENU *============")
print("1. Hu tieu")
print("2. Chao long")
print("3. Banh canh")
print("4. Bun rieu")
print("5. Pho bo")
print("================================")
khach_chon_mon = input("Moi ban chon mon an: ",)
print("================================")
if khach_chon_mon == '1':
    print("Mon ban chon la Hu tieu.")
elif khach_chon_mon == '2':
    print("Mon ban chon la Chao long.")
elif khach_chon_mon == '3':
    print("Mon ban chon la Banh canh.")
elif khach_chon_mon == '4':
    print("Mon ban chon la Bun rieu.")
elif khach_chon_mon == '5':
    print("Mon ban chon la Pho bo.")
else:
    print("Vui long chon mon trong Menu!")
    