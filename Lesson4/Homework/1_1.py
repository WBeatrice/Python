# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. 
# n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

import random 
import itertools

n = int(input("Enter the size of the 1 array: "))
A = [random.randint(0, 9) for x in range(n)]
print(f"The first array: {A}")

m = int(input("Enter the size of the 2 array: "))
B = [random.randint(0, 9) for x in range(m)]
print(f"The second array: {B}")
print()

unification = list(itertools.chain(A,B))
print(f"Combined arrays: {unification}")

for crawls in range (len(unification) - 1):
    for i in range (len(unification) - 1 - crawls):
        if unification[i] > unification[i + 1]:
            unification[i], unification[i + 1] = unification[i + 1], unification[i]
print(f"Sorted combined array: {unification}")
print()

remove = list(set(unification))
print(f"Without repetitions, in ascending order, all elements: {remove}")

#---------------------------------------------------------------------------------------

# n, m = input().split()
# first = [int(i) for i in input().split()]
# second = [int(j) for j in input().split()]

# print(*sorted(set(first).intersection(second)))