# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.
# массив чисел вводиться серез пробел 
print(len(set(map(int, input().split()))))

# Решение через функцию random

# import random

# number = int(input("Введите максимум чисел: "))
# num = []
# for i in range (number):
#     num.append(random.randint(-3, 3))
# print (num)
# print(len(set(num)))