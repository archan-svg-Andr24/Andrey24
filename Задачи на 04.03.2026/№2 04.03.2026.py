# Вводим контрольное число
k = int(input())

# Вводим количество чисел
n = int(input())

# Вводим все числа
numbers = []
for i in range(n):
    num = int(input())
    numbers.append(num)

# Убираем повторения
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

# Разделяем на друзей и врагов
friends = []
enemies = []

for num in unique_numbers:
    if num % k == 0:  # кратно контрольному числу
        friends.append(str(num))
    elif num % k == 1:  # на 1 больше кратного
        enemies.append(str(num))

# Выводим результат
print("Друзья:", ", ".join(friends))
print("Враги:", ", ".join(enemies))
