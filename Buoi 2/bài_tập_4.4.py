a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))
if(a<c+b and b<a+c and c<a+b):
    if(a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b):
        print("Tam giác vuông")
    else:
        print("Không phải tam giác vuông")
else:
    print("không phải tam giác")