def creature_registry(*args):
    creatures = {}
    for line in args:
        words = line.split()
        creature = None
        props = []
        for word in words:
            if word.lower().endswith('gon') or word.lower().endswith('phinx'):
                creature = word
            else:
                props.append(word.upper())
        if creature:
            if creature not in creatures:
                creatures[creature] = []
            for prop in props:
                if prop not in creatures[creature]:
                    creatures[creature].append(prop)
    return creatures


data = [
    'Dragon fire flying',
    'dragon strong',
    'Sphinx riddle wise',
    'sphinx mysterious'
]
print(creature_registry(*data))