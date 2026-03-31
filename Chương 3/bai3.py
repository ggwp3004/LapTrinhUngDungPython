def bai3():
    ket_qua = [str(i) for i in range(80, 101) if i % 2 == 0 and i % 3 == 0]
    if ket_qua:
        print("Các số trong khoảng 80-100 vừa chia hết cho 2 vừa chia hết cho 3:")
        print(", ".join(ket_qua))
    else:
        print("Không có số thoả điều kiện.")


if __name__ == "__main__":
    bai3()