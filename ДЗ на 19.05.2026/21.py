def herb_garden(*args):
    plants = {}
    for line in args:
        words = line.split()
        plant = None
        props = []
        for word in words:
            if word.isupper() and word.isalpha():
                plant = word
            else:
                props.append(word.lower())
        if plant:
            if plant not in plants:
                plants[plant] = []
            for prop in props:
                if prop not in plants[plant]:
                    plants[plant].append(prop)
    for plant in plants:
        plants[plant] = sorted(set(plants[plant]))
    return plants



data = [
    'RED rose fragrant BEAUTIFUL',
    'TULIP red spring',
    'ROSE thorny',
    'tulip colorful'
]
print(herb_garden(*data))