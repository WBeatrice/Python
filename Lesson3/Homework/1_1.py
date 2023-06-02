# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

N = int(input("Enter the size of the array: "))
A = list(range(1, N+1))
print(A)

number = int(input("Enter the desired number: "))
count = 0

for i in A:
    if number == i:
        count += 1
print(count)