from collections import defaultdict
import random

# Задаю кількість кубиків та кількість симуляцій кидання кубиків
num_of_dice=2
num_of_dice_roll = 100000

#  Генерую num_of_dice_roll симуляцій для набору із num_of_dice кубиків
d = defaultdict(int)
for dice_roll in [[random.randint(1, 6) for _ in range(num_of_dice)] for _ in range(num_of_dice_roll)]:
    d[sum(dice_roll)] += 1

# Сортую результати
d = dict(sorted(d.items()))

# Готую до виводу таблицю
print(f'Table of probabilities of sums when rolling {num_of_dice} dice {num_of_dice_roll} times')
print('-'*20)
print(f"|sum| probabilities|")
print('-'*20)

# Обраховую ймовірність кожної можливої суми і виводжу в таблиці
for key, value in d.items():
    print(f"|{key:3}|{value/num_of_dice_roll*100:14.4f}|")
print('-'*20)