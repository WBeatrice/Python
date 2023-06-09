# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# диапозон значений == 5, 15

import random
n = int(input("Enter the size of the array: "))
Array = [random.randint(5, 15) for x in range(n)]
print(Array)

print([i for i in range(0, len(Array))])