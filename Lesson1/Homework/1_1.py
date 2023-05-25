# Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

n = int(input("Enter a three-digit number: "))
print(int(n/100)+int(n/10)%10+n%10)

#Пример решения задачи по разботу с лекции 2

# num = int(input())
# num_sum = 0

# while num:
#     num_sum += num % 10
#     num //= 10

# print(num_sum)