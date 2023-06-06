# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

def Sum_of_numbers(a,b):
    sum = a + b
    return sum
    
if a < 0 or b < 0:
    print("The entered number is negative!")
else:
    print(Sum_of_numbers(a,b))