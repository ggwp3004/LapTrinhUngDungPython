print("Bài 1: Kiểm tra số chẵn hay lẻ")
n = int(input("Nhập số nguyên dương: "))

if n % 2 == 0:
    print("Đây là một số chẵn")
else:
    print("Đây là một số lẻ")

print("Bài 2: Nhập độ dài ba cạnh tam giác")
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))

if a + b > c and a + c > b and b + c > a:
    print("Độ dài ba cạnh tam giác")
else:
    print("Đây không phải độ dài ba cạnh tam giác")

print("Bài 3: Tính tuổi")
import time
nam_sinh = int(input("Nhập năm sinh: "))

x = time.localtime()
nam_hien_tai = x[0]

tuoi = nam_hien_tai - nam_sinh

print(f"Năm sinh {nam_sinh}, vậy bạn {tuoi} tuổi")