# ОШИБКА: sequence = sequence + [next_element] создает НОВЫЙ список
# вместо изменения существующего. Из-за этого изменения не видны
# за пределами функции.

# ИСПРАВЛЕННАЯ ВЕРСИЯ:
def continue_fibonacci_sequence(sequence, n):
    for i in range(n):
        next_element = sequence[-1] + sequence[-2]
        sequence.append(next_element)  # Используем append вместо конкатенации

# Тесты
print("\nТест 1:")
sequence = [1, 1]
continue_fibonacci_sequence(sequence, 1)
print(*sequence)

print("\nТест 2:")
sequence = [1, 1, 2, 3, 5]
continue_fibonacci_sequence(sequence, 0)
print(*sequence)