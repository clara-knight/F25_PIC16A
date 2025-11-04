class Vector2D:
    def __init__(self, x_coord, y_coord):
        self.x = float(x_coord)
        self.y = float(y_coord)

    def magnitude(self):
        return (self.x**2 + self.y**2) ** (0.5)

    def normalize(self):
        norm_x = self.x / self.magnitude()
        norm_y = self.y / self.magnitude()
        return Vector2D(norm_x, norm_y)

    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        if isinstance(other, Vector2D):
            self.x += other.x
            self.y += other.y

    def __eq__(self, other):
        if isinstance(other, Vector2D):
            return self.x == other.x and self.y == other.y
        return False

    def __str__(self):
        return str(f"Vector({self.x}, {self.y}), magnitude = {self.magnitude()}")

    def __repr__(self):
        return str(f"Vector2D(x={self.x}, y={self.y})")
