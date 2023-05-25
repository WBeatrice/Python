# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

n = int(input("Enter the number of coins: "))
one = 0
zero = 0

for i in range(n):
    number = int(input("Enter the number: "))
    if number == 1:
        one += 1
    elif number == 0:
        zero += 1
    if number != 1 and number != 0:
        print("The entered digit is neither 1 nor 0! Try again")
        break

if one > zero:
    print (f"It is necessary to flip {zero} heads")
elif one < zero:
    print(f"It is necessary to turn over {one} tails")
else:
    print(f"Heads and tails on the table in equal numbers. Flip {zero} heads or {one} tails")

#---------------------------------------------------------------------------------------------------
# Решение с инспльзование Random

# import random

# n = int(input("Enter the number of coins: "))
# one = 0
# zero = 0

# for i in range(n):
#     number = random.randint(0,1)
#     print(number)
#     if number == 1:
#         one += 1
#     elif number == 0:
#         zero += 1
#     if number != 1 and number != 0:
#         print("The entered digit is neither 1 nor 0! Try again")
#         break

# if one > zero:
#     print (f"It is necessary to flip {zero} heads")
# elif one < zero:
#     print(f"It is necessary to turn over {one} tails")
# else:
#     print(f"Heads and tails on the table in equal numbers. Flip {zero} heads or {one} tails")