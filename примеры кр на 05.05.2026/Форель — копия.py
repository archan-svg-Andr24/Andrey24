def angling(*args):
    fish_dict = {}

    for line in args:
        words = line.split()
        fish = None
        characteristics = []

        for word in words:
            if word[0].isupper():
                fish = word
            else:
                characteristics.append(word.lower())

        if fish not in fish_dict:
            fish_dict[fish] = set()
        fish_dict[fish].update(characteristics)

    # Сортируем в обратном алфавитном порядке
    result = {}
    for fish, chars in fish_dict.items():
        result[fish] = sorted(chars, reverse=True)

    return result

