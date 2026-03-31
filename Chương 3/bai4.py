def bai4():
    try:
        n = int(input("Nhập số nguyên n (<20): ").strip())
    except ValueError:
        print("Vui lòng nhập số nguyên hợp lệ.")
        return

    if n >= 20:
        print("Vui lòng nhập n < 20.")
        return

    ket_qua = [str(i) for i in range(1, n + 1) if i % 5 == 0 or i % 7 == 0]
    if ket_qua:
        print("Các số thỏa điều kiện chia hết cho 5 hoặc chia hết cho 7:")
        print(", ".join(ket_qua))
    else:
        print("Không có số thỏa điều kiện trong khoảng 1 đến {}.".format(n))


if __name__ == "__main__":
    bai4()