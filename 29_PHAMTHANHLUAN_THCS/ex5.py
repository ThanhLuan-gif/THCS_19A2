# S1
n = int(input("Nhập số : "))
tong=0
for i in range(1,n+1) : 
    tong= tong+ i 
print(tong)
#S2
n = int(input("Nhập số : "))
tich=1
for i in range(1,n) : 
    tich= tich * i 
print(tich)
#S3
n = int(input("Nhập số : "))
s3=0
for i in range(1,n+1) : 
    s3 = s3 - (((-1)**i)/i)
print(f"s3={s3}")
#S4
n = int(input("Nhập số : "))
s4 = 0
for k in range(0, n+1):
    s4 = s4 + k / (k + 2)
print(f"s4 = {s4}")
