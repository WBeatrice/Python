# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10
s = int(input())
p = int(s/6)
print(p, int(s-(p+p)),  p)

# Пример решения задачи по разботу с лекции 2

# count = int(input())

# if count % 6:
#     print ("The data is incorrect!")
# else:
#     k = 2 * count // 3
#     p = s = count // 6
#     print(p, k, s)