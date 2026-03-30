class BigBell:
    def __init__(self):
        self.next = "ding"

    def sound(self):
        print(self.next)
        self.next = "dong" if self.next == "ding" else "ding"