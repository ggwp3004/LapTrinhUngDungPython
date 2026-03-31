def bai1():
    try:
        n = int(input("Nhập số nguyên n: ").strip())
    except ValueError:
        print("Vui lòng nhập số nguyên hợp lệ.")
        return

    if n <= 1:
        print("Không có giá trị nào nhỏ hơn n để tính tích 2*.")
        return

    ket_qua = []
    for i in range(1, n):
        tich = 2 * i
        ket_qua.append(f"{tich} = 2*{i}")

    print("Kết quả:")
    print(', '.join(ket_qua))


if __name__ == "__main__":
    bai1()