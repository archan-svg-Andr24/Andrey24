def magic_artifacts(*args):
    artifacts = {}
    for line in args:
        words = line.split()
        artifact = None
        props = []
        for word in words:
            if any(c.isdigit() for c in word):
                artifact = word
            else:
                props.append(word.lower())
        if artifact:
            if artifact not in artifacts:
                artifacts[artifact] = []
            for prop in props:
                if prop not in artifacts[artifact]:
                    artifacts[artifact].append(prop)
    for artifact in artifacts:
        artifacts[artifact] = sorted(set(artifacts[artifact]), key=lambda x: (-len(x), x), reverse=True)
    return artifacts


data = [
    'Ring1 powerful ancient',
    'Amulet3 glowing protective',
    'ring1 shiny',
    'AMULET3 enchanted'
]
print(magic_artifacts(*data))