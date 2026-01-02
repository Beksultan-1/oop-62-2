class Tank: # 2 usages

    # Конструктор класса
    def __init__(self, name, lvl, hp):
        # Атрибуты класса
        self.name = name
        self.lvl = lvl
        self.hp = hp

    # Добавляем базовый метод для демонстрации
    def describe(self):
        return f"{self.name} Сверхтяжелый танк Германии!!"

# Объект/Экземпляр класса
ratte = Tank(name="ratte", lvl=13, hp=18000)

print(ratte.name)
print(ratte.describe())
class Tank: # 2 usages

    # Конструктор класса с использованием стандартных имен атрибутов
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        return f"{self.name} атакует нашу базу!!"
ratte = Tank(name="ratte", lvl=13, hp=18000)
print(ratte.action())
""""""""""""""""""""""""""""""""""""""""""""""""
class Tank: # 2 usages

    # Конструктор класса
    def __init__(self, name, lvl, hp):
        # Атрибуты класса
        self.name = name
        self.lvl = lvl
        self.hp = hp

    # Добавляем базовый метод для демонстрации
    def describe(self):
        return f"{self.name} Сверхтяжелый танк СССР!!"

# Объект/Экземпляр класса
tg_5 = Tank(name="tg_5", lvl=13, hp=18100)

print(tg_5.name)
print(tg_5.describe())
class Tank: # 2 usages

    # Конструктор класса с использованием стандартных имен атрибутов
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        return f"{self.name} начал атаку вражеской базы!!"
tg_5 = Tank(name="tg_5", lvl=13, hp=18100)
print(tg_5.action())
