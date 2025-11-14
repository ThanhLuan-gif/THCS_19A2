x = int(input("Nhập số năm  : "))
nam_nhuan = (x % 400 == 0) or ( x % 4 == 0 and x % 100 != 0 ) 
print(f"Năm {x} " + "là năm nhuận" * nam_nhuan + "không là năm nhuận" * (not nam_nhuan))

