# Tạo và ghi nội dung vào file
with open("demo_file1.txt", "w", encoding="utf-8") as f:
    f.write("Thuc\nhanh\nvoi\nfile\nIO")

# a) In ra trên một dòng
with open("demo_file1.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print("a) In trên một dòng:")
    print(content.replace("\n", " "))

# b) In theo từng dòng
with open("demo_file1.txt", "r", encoding="utf-8") as f:
    print("\nb) In theo từng dòng:")
    for line in f:
        print(line.strip())