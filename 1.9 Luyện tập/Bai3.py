_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even = [i for i in _list if i % 2 == 0]
odd = [i for i in _list if i % 2 != 0]

print("Số chẵn:", even)
print("Số lẻ:", odd)