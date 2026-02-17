def parrot(phrase):
    if not hasattr(parrot, 'heard_phrases'):
        parrot.heard_phrases = set()

    if phrase in parrot.heard_phrases:
        print(phrase)

    parrot.heard_phrases.add(phrase)

# Тесты
print("Тест 1:")
parrot("Привет!")
parrot("Привет!")
parrot("Как дела?")

# Очистка для второго теста
parrot.heard_phrases = set()

print("\nТест 2:")
parrot("Привет")
parrot("Как тебя зовут?")
parrot("Привет")