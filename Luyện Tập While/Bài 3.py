n = int(input("Nhập n: "))
i = 2
la_snt = True

if n < 2:
    la_snt = False
else:
    while i < n:
        if n % i == 0:
            la_snt = False
            break
        i += 1

if la_snt:
    print("Đây là số nguyên tố")
else:
    print("Không phải số nguyên tố")