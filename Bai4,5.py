print("Bài 4: Kiểm tra chia hết cho 2 và 3")
n = int(input("Nhập số nguyên dương: "))

if n % 2 == 0 and n % 3 == 0:
    print("Số này chia hết cho cả 2 và 3")
elif n % 2 == 0:
    print("Số này chia hết cho 2")
elif n % 3 == 0:
    print("Số này chia hết cho 3")
else:
    print("Số này không chia hết cho 2 cũng không chia hết cho 3")

print("\nBài 5: Giải phương trình bậc 2")
import math
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

# Trường hợp a = 0 => phương trình bậc 1
if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        x = -c / b
        print("Nghiệm x =", x)
else:
    delta = b**2 - 4*a*c

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("Phương trình có 2 nghiệm phân biệt:")
        print("x1 =", x1)
        print("x2 =", x2)
    elif delta == 0:
        x = -b / (2*a)
        print("Phương trình có nghiệm kép x =", x)
    else:
        print("Phương trình vô nghiệm")