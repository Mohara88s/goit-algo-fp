

def greedy_algorithm(items, budget):
    dishes = items.copy()
    for dish, value in dishes.items():
        # ctpr -> calories to price ratio
        dishes[dish]['ctpr'] = value["calories"]/value["cost"] 
    
    #  Сортую страви за ctpr
    sorted_dishes = dict(sorted(dishes.items(), key=lambda item: item[1]['ctpr'], reverse=True))
    
    set_of_dishes = {}
    for dish, value in sorted_dishes.items():
        dish_cost = int(value["cost"])
        if budget >= dish_cost:
            budget -= dish_cost
            set_of_dishes[dish] = value
    return set_of_dishes, budget

def dynamic_programming(items, budget):
    print()


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}
budget = 100
print(greedy_algorithm(items, budget))
