# Nhập số dòng cần đọc
n = int(input("Nhập số dòng cần đọc: "))

# Mở file (thay 'data.txt' bằng tên file của bạn)
with open("data.txt", "r", encoding="utf-8") as f:
    for i in range(n):
        line = f.readline()
        if not line:  # nếu hết file
            break
        print(line.strip())