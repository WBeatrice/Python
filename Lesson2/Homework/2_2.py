# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

n = int(input("Enter the sum of the two numbers: "))
m = int(input("Enter the composition of two numbers: "))
duplication = 0
for i in range(n):
    if duplication:
        break
    for j in range(m):
        if i + j == n and i * j == m:
            duplication = 1
            print (i, j)
            
            
