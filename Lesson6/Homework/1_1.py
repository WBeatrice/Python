# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a1 = int(input("Enter the first element: "))
n = int(input("Enter the difference: ")) 
d = int(input("Enter the number of items: "))
print(a1 + (n-1) * d)

#------------------------------------------------

# a1 = int(input())
# d = int(input())
# n = int(input())
# for i in range(n):
#     print(a1 + i * d, end = " ")