class pointer:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"
    

p1 = pointer(736, 22)
print(p1)