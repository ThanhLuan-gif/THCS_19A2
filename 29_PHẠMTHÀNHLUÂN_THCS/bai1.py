x=int(input("nhập giá sản phẩm :"))
y=int(input("nhập số lượng mua:"))
tong_chi_phi=x + y
thue_vat=x*y*0.1
tong_tien_phai_tra=(thue_vat)+(tong_chi_phi)
print(f"Tổng số tiền phải trả là {tong_tien_phai_tra :.2f} ")
