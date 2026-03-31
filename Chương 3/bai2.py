def bai2():
    try:
        n = int(input("Nhập số nguyên n: ").strip())
    except ValueError:
        print("Vui lòng nhập số nguyên hợp lệ.")
        return

    if n > 10:
        print("Số nhập vào phải bé hơn 10.")
        return

    if n <= 0:
        print("Không có số chẵn trong khoảng 1 đến n.")
        return

    chan = [str(i) for i in range(1, n + 1) if i % 2 == 0]
    if chan:
        print("Số chẵn trong khoảng từ 1 đến {}: {}".format(n, ", ".join(chan)))
    else:
        print("Không có số chẵn trong khoảng từ 1 đến {}.".format(n))


if __name__ == "__main__":
    bai2()