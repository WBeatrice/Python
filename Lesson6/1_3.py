# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод: 
# 1 2 3 2 3 
# Вывод:
# 2

lst = list(map(int, input().split()))
lst1 = [lst.count(i) - 1 for i in lst]
print(lst1)
print(sum(lst1) // 2)

#-----------------------------------------------------
# Решение через два цикла 
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         if i != j:
#             if nums[i] == nums[j]:
#                 count += 1
# print(int(count / 2))