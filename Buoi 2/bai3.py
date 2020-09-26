a = int(input("Nhap N :"))
sum_chan=0
for i in range(a+1):
    if i %2 == 0:
        sum_chan += i
        print(f"KetQua : {sum_chan}")