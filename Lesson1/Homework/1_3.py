# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input())
m = int(input())
k = int(input())

temp = int(n*m)-m

if temp == k or temp == k:
    print("Yes")
else:
    print("No")

# Пример решения задачи по разботу с лекции 2

# n = int(input())
# m = int(input())
# k = int(input())

# if (k % n == 0 or k % m == 0) and k < m * n:
#     print("Yes")
# else:
#     print("No")
