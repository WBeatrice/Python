# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

n = int(input("Enter the number: "))
k = 1

while k <= n:
    if(k <= n):
        if (k * 2 > n):
            print(k)
            break
        else:
            print(k) 
            k = k*2