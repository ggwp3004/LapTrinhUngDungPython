# Nhập nội dung từ bàn phím
text = input("Nhập đoạn văn bản: ")

# Ghi vào file
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(text)

# Đọc lại nội dung file và hiển thị
with open("output.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print("\nNội dung trong file:")
    print(content)