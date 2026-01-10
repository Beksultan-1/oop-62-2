class Notification:
    def __init__(self, text):
        self.text = text

    def __str__(self):
            return f"{self.text}"
    def __call__(self):
            return f"{self.text} отправлено"
n = Notification("Новое сообщение")
print(n)
n()
###############################################
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        if isinstance(other, (int, float)):
            return Vector(self.x + other, self.y + other)
        return NotImplemented
    def __eq__(self, other):
        if not isinstance(other, Vector):
            return False
        return self.x == other.x and self.y == other.y

v1 = Vector(2, 3)
v2 = Vector(1, 1)
v3 = v1 + v2
print(v3.x, v3.y)
print(v1 == v2)
######################################################
from tkinter.font import names


class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role
    @classmethod
    def create_admin(cls):
        return cls(name="user", role="admin")
anton = User("Anton", "admin")
print(anton.role)