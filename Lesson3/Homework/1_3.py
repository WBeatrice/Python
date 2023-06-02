# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко; 
# D, G – 2 очка; 
# B, C, M, P – 3 очка; 
# F, H, V, W, Y – 4 очка; 
# K – 5 очков; J, X – 8 очков; 
# Q, Z – 10 очков. 
# А русские буквы оцениваются так: 
# А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; 
# Б, Г, Ё, Ь, Я – 3 очка; 
# Й, Ы – 4 очка; 
# Ж, З, Х, Ц, Ч – 5 очков; 
# Ш, Э, Ю – 8 очков; 
# Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, 
# либо только русские буквы.

# *Пример:*

# ноутбук
#     12

ENG = {1: 'AEIOULNSTR',
       2: 'DG',
       3: 'BCMP',
       4: 'FHVWY',
       5: 'K',
       8: 'JK',
       10: 'QZ'}
RUS = {1: 'АВЕИНОРСТ',
       2: 'ДКЛМПУ',
       3: 'БГЁЬЯ',
       4: 'ЙЫ',
       5: 'ЖЗХЦЧ',
       8: 'ШЭЮ',
       10: 'ФЩЪ'}

language = int(input("Enter 1 if you play in russian, 0 if you play in english: "))
word = input("Enter the word: ").upper()

if language == 1:
    print("For your words you get", sum([n for i in word for n, v in RUS.items() if i in v]), "points")
elif language == 0:
    print("For your words you get", sum([n for i in word for n, v in ENG.items() if i in v]), "points")
else:
    print("You have entered the wrong language! Try again!")