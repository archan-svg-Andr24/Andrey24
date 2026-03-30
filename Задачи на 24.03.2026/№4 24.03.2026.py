class OddEvenSeparator:
    def __init__(self):
        self.numbers = []

    def add_number(self, num):
        self.numbers.append(num)

    def even(self):
        return [n for n in self.numbers if n % 2 == 0]

    def odd(self):
        return [n for n in self.numbers if n % 2 != 0]