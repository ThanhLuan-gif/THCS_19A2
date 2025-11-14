x = float(input("Nhập số kWh : "))
kWh_1= x * (x <= 100 ) +100* (x -100)
kWh_2= (x-100) * (100<x<=200) +100 * (x > 200)
kWh_3=(x-100)* (200<x<300) + 100 * (x > 200)
tong= kWh_1*1678+kWh_2*1734+kWh_3*2014
print(f"Tổng số tiền điện phải trả là {tong}")