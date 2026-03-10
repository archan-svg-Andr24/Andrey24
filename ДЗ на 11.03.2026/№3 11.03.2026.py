birthdays = {}  # Словарь для месяцев

# количество одноклассников
n = int(input())

# Заполняем словарь: 'месяц':'список (день, имя)'
for _ in range(n):
    name, day, month = input().split()
    day = int(day)

    if month not in birthdays:
        birthdays[month] = []
    birthdays[month].append((day, name))

# Сортируем записи для каждого месяца
for month in birthdays:
    # Сортировка по дню, затем по имени
    birthdays[month].sort()

# количество запросов
m = int(input())

# Обрабатываем запросы
for _ in range(m):
    month = input()

    if month in birthdays and birthdays[month]:
        result = []
        for day, name in birthdays[
            month]:  # перебирает кортежи (день, имя) в списке, соответствующем месяцу в словаре birthdays
            result.append(f"{name} {day}")
        print(' '.join(
            result))  # выводит все элементы списка result, объединив их в одну строку с пробелами между элементами
    else:
        print()  # если для указанного месяца нет именинников, выводит пустую строку
