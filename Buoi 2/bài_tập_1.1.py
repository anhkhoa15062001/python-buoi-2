# giải và biện luận phương trình bậc 2
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
import math
if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình vô số nghiệm!")
        else:
            print("Phương trình vô nghiệm!")
    else:
        if c == 0:
            print("Phương trình có 1 nghiệm x = 0")
        else:
            print("Phương trình có 1 nghiệm x = ", -c / b)
else:
    delta = b * b - 4 * a * c
    if delta < 0:
        print("Phương trình vô nghiệm!")
    elif delta == 0:
        print("Phương trình có 1 nghiệm x = ", -b / (2 * a))
    else:
        print("Phương trình có 2 nghiệm phân biệt!")
        print("x1 = ", float((-b - math.sqrt(delta)) / (2 * a)))
        print("x2 = ", float((-b + math.sqrt(delta)) / (2 * a)))