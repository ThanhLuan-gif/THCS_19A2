n = int(input("Nhập số : "))
for x in range(2,n): 
    nt =True
    y=2
    while y*2 <= x : 
        if x % y == 0 :
            nt = False
            break
        y+=1
    if nt==True :
        print(x)
