tu_so = int(input("Nhập tử số : "))
mau_so = int(input("Nhập mẫu số : "))
x = tu_so
y = mau_so
while x !=y :
    if x > y :
        x = x- y
    else :
        y = y-x
UCLN = x
print(f"Phân số rút gọn là {tu_so//UCLN}/{mau_so//UCLN}")