class Turtle:
    def __init__(self, x=0, y=0, s=1):
        self.x = x
        self.y = y
        if s <= 0:
            raise ValueError("Шаг должен быть положительным!")
        self.s = s

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s - 1 <= 0:
            raise ValueError("Шаг не может быть <= 0")
        self.s -= 1

    def count_moves(self, x2, y2):
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)

        # Если dx или dy не делятся на шаг s, то добраться невозможно
        if dx % self.s != 0 or dy % self.s != 0:
            return -1

        return dx // self.s + dy // self.s
