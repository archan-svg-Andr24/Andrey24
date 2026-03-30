class BoundingRectangle:
    def __init__(self):
        self.min_x = None
        self.max_x = None
        self.min_y = None
        self.max_y = None

    def add_point(self, x, y):
        if self.min_x is None:
            self.min_x = self.max_x = x
            self.min_y = self.max_y = y
        else:
            self.min_x = min(self.min_x, x)
            self.max_x = max(self.max_x, x)
            self.min_y = min(self.min_y, y)
            self.max_y = max(self.max_y, y)

    def width(self):
        return self.max_x - self.min_x

    def height(self):
        return self.max_y - self.min_y

    def bottom_y(self):
        return self.min_y

    def top_y(self):
        return self.max_y

    def left_x(self):
        return self.min_x

    def right_x(self):
        return self.max_x