# ОШИБКА: arr.reverse() изменяет список на месте и возвращает None,
# поэтому mirrored_part становится None вместо перевёрнутого списка.

# ИСПРАВЛЕННАЯ ВЕРСИЯ:
def mirror(arr):
    mirrored_part = arr[::-1]  # Создаем копию перевёрнутого списка через срез
    arr.extend(mirrored_part)  # Добавляем к оригинальному списку

# Тесты
print("\nТест 1:")
arr = [1, 2]
mirror(arr)
print(*arr)

print("\nТест 2:")
arr = [1]
mirror(arr)
print(*arr)