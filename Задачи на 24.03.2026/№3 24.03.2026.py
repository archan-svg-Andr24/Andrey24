class Balance:
    def __init__(self):
        self.left = 0
        self.right = 0

    def add_left(self, weight):
        self.left += weight

    def add_right(self, weight):
        self.right += weight

    def result(self):
        if self.left == self.right:
            return "="
        return "L" if self.left > self.right else "R"