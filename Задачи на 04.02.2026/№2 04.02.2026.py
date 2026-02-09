def space_game():
    n = 0
    text = input()
    for _ in range(len(text)):
        if " " in text:
            n += 1
    if n % 2 == 0:
        print("Вы выиграли")
    else:
        print("Вы проиграли")

space_game()