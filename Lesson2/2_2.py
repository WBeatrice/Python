# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φи(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6 

n = int(input())

n1 = 0 
n2 = 1
i = 2

while n2 <= n:
    if n2 == n:
        print (i)
        break
    n1, n2 = n2, n1 + n2
    i += 1
else:
    print(-1)