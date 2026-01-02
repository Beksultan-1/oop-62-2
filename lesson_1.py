class Hero: # 2 usages

    # Конструктор класса
    def __init__(self, name, lvl, hp):
        # Атрибуты класса
        self.name = name
        self.lvl = lvl
        self.hp = hp

    # Добавляем базовый метод для демонстрации
    def action(self):
        return f"{self.name} выполняет базовое действие!"

# Объект/Экземпляр класса
kirito = Hero(name="Kirito", lvl=100, hp=1000)

print(kirito.name)
print(kirito.action())
class Hero: # 2 usages

    # Конструктор класса с использованием стандартных имен атрибутов
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        return f"{self.name} base action!!"

# Объект/Экземпляр класса
kirito = Hero(name="Ardager", lvl=100, hp=1000)
asuna = Hero(name="Asuna", lvl=99, hp=999)

# Дополнительные переменные
my_str = "text"
my_float = 1.12
my_list = [1, 2, "123"]

print(f"{kirito.name} is level {kirito.lvl}")
print(f"{asuna.name}'s action: {asuna.action()}")