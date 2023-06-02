# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

lst = list(map(int, input().split()))
k = int(input()) % len(lst) + 1
lst = [lst[i - k] for i in range(len(lst))]
print(lst)

# Второй вариан решения 
# list_nums = list(map(int, input().split()))
# steps = int(input())

# for i in range(steps):
#             list_nums.insert(0, list_nums.pop())
# print(list_nums)