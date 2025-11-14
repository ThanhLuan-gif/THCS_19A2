x = float(input("Nhập mức lương cơ bản : "))
y = float(input("Nhập số ngày công : "))
l1n= y*(x/22)
tt= l1n*0.1*(y > 22)
tp= l1n*0.05*(y<22)
tong=l1n+tt-tp
print(f"Tổng tiền lương thực nhận của nhân viên là {tong}")

