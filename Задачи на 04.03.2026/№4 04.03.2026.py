def main():
    # Читаем количество звуков
    n = int(input("Введите количество звуков: "))

    # Создаем пустой список для звуков
    sounds = []
    print("Введите звуки:")
    for i in range(n):
        sound = input(f"Звук {i + 1}: ")
        sounds.append(sound)

    # Читаем объяснения
    print("\nВведите объяснения (для завершения нажмите Enter):")
    explanations = []
    while True:
        line = input()
        # Если строка пустая - выходим из цикла
        if line == "":
            break
        explanations.append(line)

    # Создаем словарь для результатов
    result = {}

    # Обрабатываем каждый звук
    for sound in sounds:
        # Получаем первую букву звука
        first_letter = sound[0]

        # Находим подходящие объяснения
        found_explanation = "nothing to say"
        for explanation in explanations:
            # Проверяем начало и общие символы
            if explanation.startswith(first_letter):
                # Считаем общие символы
                common_chars = 0
                for char in sound:
                    if char in explanation:
                        common_chars += 1
                        # Если нашли 3 общих символа - достаточно
                        if common_chars >= 3:
                            found_explanation = explanation
                            break
            # Если нашли объяснение - прерываем внутренний цикл
            if found_explanation != "nothing to say":
                break

        # Сохраняем результат
        result[sound] = found_explanation

    # Выводим итоговый словарь
    print("\nРезультаты:")
    print(result)


main()
