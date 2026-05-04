class Human:
    def __init__(self, name, *entities, magic=0):
        self.name = name
        self.entities = list(entities)
        self.magic = magic

    def change_name(self, addition):
        self.name += f' {addition}'

    def __iadd__(self, line):
        self.entities.append(line)
        self.magic += len(line) // 4
        return self

    def __sub__(self, other):
        # Новое имя: первые 3 буквы первого + последние 3 буквы второго
        part1 = self.name[:3].capitalize()
        part2 = other.name[-3:].capitalize()
        new_name = part1 + part2

        # Сущности, которые есть у self, но нет у other
        new_entities = sorted(
            [e for e in self.entities if e not in other.entities]
        )

        return Human(new_name, *new_entities)  # magic=0 по умолчанию

    def __call__(self, n):
        return self.entities[:n]

    def __lt__(self, other):
        return self._cmp_key() < other._cmp_key()

    def __le__(self, other):
        return self._cmp_key() <= other._cmp_key()

    def __eq__(self, other):
        return self._cmp_key() == other._cmp_key()

    def __ne__(self, other):
        return self._cmp_key() != other._cmp_key()

    def __gt__(self, other):
        return self._cmp_key() > other._cmp_key()

    def __ge__(self, other):
        return self._cmp_key() >= other._cmp_key()

    def _cmp_key(self):
        # Сравнение: magic (по убыванию → используем отрицание),
        # затем количество сущностей (по убыванию → отрицание),
        # затем имя (по возрастанию, A < Z)
        return (-self.magic, -len(self.entities), self.name)

    def __str__(self):
        entities_str = ', '.join(self.entities)
        return f'Human by name {self.name} ({entities_str}, {self.magic})'

    def __repr__(self):
        return self.__str__()

