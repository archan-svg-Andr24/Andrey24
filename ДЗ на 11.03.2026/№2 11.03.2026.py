n = int(input())  # количество записей

# Словарь: 'имя':'список телефонов'
phonebook = {}

# Заполняем телефонную книгу
for _ in range(n):
    phone, name = input().split()
    if name not in phonebook:
        phonebook[name] = []
    phonebook[name].append(phone)

# количество запросов
m = int(input())

# Обрабатываем запросы
for _ in range(m):
    query = input()
    if query in phonebook:
        print(' '.join(phonebook[
                           query]))  # выводит телефоны, связанные с именем (если имя найдено), объединив их в строку через пробел
    else:
        print('Нет в телефонной книге')
