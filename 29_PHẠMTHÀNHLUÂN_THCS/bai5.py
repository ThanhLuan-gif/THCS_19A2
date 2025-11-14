x = float(input("Nhập số tiền gửi ban đầu x : (VNĐ)"))
y = float(input("Nhập lãi suất hàng năm y : (%)"))
# chuyển lãi suất phần trăm sang lãi suất thập phân
z = y / 100 
a = x * z*(1/12)
b = x * z*(6/12)
c= x*z*3
print(f"Tiền lãi sau 1 tháng là {a} VNĐ")
print(f"Tiền lãi sau 3 quý là {b} VNĐ ")
print(f"Tiền lãi sau 3 năm là {c} VNĐ")