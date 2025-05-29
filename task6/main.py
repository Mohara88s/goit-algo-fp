import copy
from itertools import zip_longest

def greedy_algorithm(items, budget):
    # Роблю повну копію страв
    dishes = copy.deepcopy(items)
    # Перебираю стави та визначаю їх ранг по відношенню калорійності до ціни (calories to price ratio)
    for name, dish in dishes.items():
        # ctpr -> calories to price ratio
        dishes[name]['ctpr'] = dish["calories"]/dish["cost"] 
    #  Сортую страви за ctpr
    sorted_dishes = dict(sorted(dishes.items(), key=lambda item: item[1]['ctpr'], reverse=True))
    # Ініціалізую список страв та додаю страви в черзі обрахованого рангу
    set_of_dishes = {}
    for name, dish in sorted_dishes.items():
        dish_cost = int(dish["cost"])
        if budget >= dish_cost:
            budget -= dish_cost
            set_of_dishes[name] = dish
    # Знаходжу калорійність списку обраних страв
    calories = 0
    for name, dish in set_of_dishes.items():
        calories += dish["calories"]
    # Повертаю список обраних страв та невикористаний бюджет
    return set_of_dishes, calories, budget

def dynamic_programming(dishes, budget):
    dishes_list = list(dishes.items())
    num_of_dishes = len(dishes_list)
    # Таблиця для збереження максимальних калорій
    max_calories = [[0 for _ in range(budget + 1)] for _ in range(num_of_dishes + 1)]
    # Таблиця для збереження наборів страв
    sets_of_dishes = [[{} for _ in range(budget + 1)] for _ in range(num_of_dishes + 1)]
    # Проходжу по стравах
    for i in range(1, num_of_dishes + 1):
        name, dish = dishes_list[i-1]
        cost = dish["cost"]
        calories = dish["calories"]
        # Розглядаю випадки для кожного бюджету
        for b in range(budget + 1):
            # Якщо страва в бюджеті та дає більше калорій то оновлюємо максимум
            if cost <= b and max_calories[i-1][b] < max_calories[i-1][b-cost] + calories:
                max_calories[i][b] = max_calories[i-1][b-cost] + calories
                # Копіюю попередній набір страв та додаю актуальну
                sets_of_dishes[i][b] = copy.deepcopy(sets_of_dishes[i-1][b-cost])
                sets_of_dishes[i][b][name]=dish
            else:
                # Залишаю той же масимум і набір страв
                max_calories[i][b] = max_calories[i-1][b]
                sets_of_dishes[i][b] = copy.deepcopy(sets_of_dishes[i-1][b])
    # Функція повертає оптимальні набір страв та кількість калорій в бюджеті
    return sets_of_dishes[num_of_dishes][budget], max_calories[num_of_dishes][budget]


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}
budget = 100


print(f'Calculations for budget: {budget}:')
greedy_set_of_dishes, calories, unused_budget = greedy_algorithm(items, budget)
dynamic_programming_set_of_dishes, max_calories, = dynamic_programming(items, budget)

print('-'*65)
print(f'|       greedy set     |calories|dynamic programing set|calories|')
print('-'*65)
for g_s, d_p_s  in zip_longest(greedy_set_of_dishes.items(), dynamic_programming_set_of_dishes.items(), fillvalue=(None)):
    g_s_name = g_s[0] if g_s else ''
    d_p_s_name = d_p_s[0] if d_p_s else ''
    g_s_calories = g_s[1]['calories'] if g_s else ''
    d_p_s_calories = d_p_s[1]['calories'] if d_p_s else ''
    print(f'|{g_s_name:21} | {g_s_calories:6} | {d_p_s_name:21}| {d_p_s_calories:6} |')
print('-'*65)
print(f'| Total:               | {calories:6} | Total:               | {max_calories:6} |')
print('-'*65)
print(f'The greedy algorithm unused budget: {unused_budget}')

