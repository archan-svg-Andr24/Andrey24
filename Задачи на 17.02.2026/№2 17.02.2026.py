def count_food(days):
    if not hasattr(count_food, 'daily_food'):
        return 0

    total = 0
    for day in days:
        total += count_food.daily_food[day - 1]
    return total

# Тесты
count_food.daily_food = [0, 150, 150]
print("\nТест 1:")
print(count_food([1]))

print("\nТест 2:")
print(count_food([2, 3]))