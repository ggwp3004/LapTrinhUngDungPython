import database

database.create_table()

while True:
    print("\n--- QUẢN LÝ NHÂN SỰ ---")
    print("1. Thêm")
    print("2. Hiển thị")
    print("3. Sửa")
    print("4. Xóa")
    print("5. Tìm kiếm")
    print("0. Thoát")

    choice = input("Chọn: ")

    if choice == "1":
        cccd = input("CCCD: ")
        hoten = input("Họ tên: ")
        ngaysinh = input("Ngày sinh: ")
        gioitinh = input("Giới tính: ")
        diachi = input("Địa chỉ: ")

        database.them_nhansu(cccd, hoten, ngaysinh, gioitinh, diachi)

    elif choice == "2":
        for ns in database.hien_thi():
            print(ns)

    elif choice == "3":
        cccd = input("Nhập CCCD cần sửa: ")
        hoten = input("Họ tên mới: ")
        ngaysinh = input("Ngày sinh: ")
        gioitinh = input("Giới tính: ")
        diachi = input("Địa chỉ: ")

        database.sua_nhansu(cccd, hoten, ngaysinh, gioitinh, diachi)

    elif choice == "4":
        cccd = input("Nhập CCCD cần xóa: ")
        database.xoa_nhansu(cccd)

    elif choice == "5":
        keyword = input("Nhập từ khóa: ")
        for ns in database.tim_kiem(keyword):
            print(ns)

    elif choice == "0":
        break