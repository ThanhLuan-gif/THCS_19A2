x = input("Nhập tên đăng nhập :")
y = input("Nhập mật khẩu : ")
welcome= (x == "admin" ) and (y == "password123")
print(f"Đăng nhập thành công"  * welcome + " Tên đăng nhập hoặc mật khẩu không chính xác " *(not welcome) )