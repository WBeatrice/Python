# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

N = int(input("Enter the size of the array: "))
A = list(range(1, N+1))
print(A)

X = int(input("Enter the desired number: "))

for i in A:
    if X == i:
        print(f"There is a number in the array equal to {X}: {i}")
    if i == X - 1:
        print(f"The smallest closest number: {i}")
    if i == X + 1:
        print(f"The largest closest number: {i}")