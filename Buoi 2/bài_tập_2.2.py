n = int(input("nhập n: "))
x = float(input("nhập x: "))

s1 = 0
for i in range(1,n+1):
    s1 += (x**i)
print("s1 = " ,1+s1)

s2 = 0
for i in range(1,n+1):
    if i == n+1:
        s2 = (-1)**i*(x**i)
    else:
        if i%2==0:
            s2+= x**i
        else:
            s2-= x**i
print("s2 = ", 1+s2)

# hàm tính giai thừa
def giaiThua(a):
    giai_thua = 1
    if  (a == 0 or a == 1):
        return giai_thua
    else:
        for i in range (2, n+1):
            giai_thua = giai_thua*i
        return giai_thua

s3 = 0
for i in range(1,n+1):
    if i == n:
         s3+= (x**(i)) / (giaiThua(i))
    else:
        s3+= x/giaiThua(i)
print("s3 = ", 1+s3)



        


