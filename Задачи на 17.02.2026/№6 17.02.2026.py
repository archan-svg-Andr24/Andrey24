print("\n--- Одинаковый результат для неизменяемых типов ---")
# Для неизменяемых типов (int, str) результат одинаковый
value1 = 5
value1 = value1 + 3
print("value1 = value1 + 3:", value1)

value2 = 5
value2 += 3
print("value2 += 3:", value2)

print("\n--- Разный результат для изменяемых типов ---")
# Для изменяемых типов (list) результат может отличаться

# Случай 1: value = value + addition создает НОВЫЙ объект
list1 = [1, 2, 3]
list1_copy = list1  # Создаем ссылку на тот же список
print("Оригинальный list1:", list1)
print("list1_copy указывает на тот же объект:", list1_copy)
list1 = list1 + [4, 5]  # Создается новый список
print("После list1 = list1 + [4, 5]:")
print("  list1:", list1)
print("  list1_copy:", list1_copy)
print("list1_copy не изменился, т.к. list1 теперь указывает на новый объект!")

print()

# Случай 2: value += addition изменяет существующий объект
list2 = [1, 2, 3]
list2_copy = list2  # Создаем ссылку на тот же список
print("Оригинальный list2:", list2)
print("list2_copy указывает на тот же объект:", list2_copy)
list2 += [4, 5]  # Изменяет существующий список
print("После list2 += [4, 5]:")
print("  list2:", list2)
print("  list2_copy:", list2_copy)
print("list2_copy ТОЖЕ изменился, т.к. += изменяет объект на месте!")