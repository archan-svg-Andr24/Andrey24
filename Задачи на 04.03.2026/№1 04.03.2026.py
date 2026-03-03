# Читаем строки до пустой строки
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

# Создаем списки для каждой категории
class_lesson = []  # строки с class или lesson
troll = []  # строки с troll
other = []  # строки без этих подстрок

# Распределяем строки по категориям
for line in lines:
    has_class_lesson = False
    has_troll = False

    # Проверяем наличие подстрок
    if "class" in line or "lesson" in line:
        has_class_lesson = True
        class_lesson.append(line)

    if "troll" in line:
        has_troll = True
        troll.append(line)

    if not has_class_lesson and not has_troll:
        other.append(line)

# Вычисляем средние длины
# Для строк с class или lesson
sum_length = 0
for s in class_lesson:
    sum_length += len(s)
avg_class_lesson = sum_length / len(class_lesson)

# Для строк с troll
sum_length = 0
for s in troll:
    sum_length += len(s)
avg_troll = sum_length / len(troll)

# Для остальных строк
sum_length = 0
for s in other:
    sum_length += len(s)
avg_other = sum_length / len(other)

# Выводим результат
print(avg_class_lesson, avg_troll, avg_other)
