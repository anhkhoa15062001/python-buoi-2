a = int(input("Nhap N :"))
sum_le=0
for i in range(a+1):
    if i %2 != 0:
        sum_le += i
    print(f"KetQua : {sum_le}")