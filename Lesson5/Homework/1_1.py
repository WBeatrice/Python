# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А 
# в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

a = int(input("Enter the number: "))
b = int(input("Enter the degree: "))


def Exponentiation_of_a_number(a, b):
    if a == 1 or a == 0:
        return a
    else:
        a **= b
        return a
 

print(Exponentiation_of_a_number(a,b))