#Problem1:
# class Hero:
#     def __init__(self, name, lvl, hp):
#         self.name = name
#         self.lvl = lvl
#         self.hp = hp
#     def action(self):
#         return f"{self.name} готов к бою!"
#
# barbarian = Hero(name="Barbarian", lvl=35, hp=350)
# print(barbarian.action())
#
# class HeroMage(Hero):
#
#     def __init__(self, name, lvl, hp, mp):
#         super().__init__(name, lvl, hp)
#         self.mp = mp
#
#     def cast_spell(self):
#         return f"{self.name} кастует заклинание, MP:!!"
#
#
# gendalf = HeroMage(name="Gendalf", lvl=100, hp=1000, mp=100)
#
# print(gendalf.cast_spell())
#
# class WarriorHero(HeroMage):
#    def action(self):
#     return f"{self.name} рубит мечом!"
# arthur = WarriorHero(name="Arthur", lvl=150, hp=2000, mp=80)
# print(arthur.action())
# """"""""""""""""""""""""""""""""""""""""""
# class Hero:
#     def __init__(self, name, level):
#         self.name = name
#         self.level = level
#
# class BankAccount:
#     bank_name = "SimBank"  # Атрибут класса
#
#     def __init__(self, hero, balance, password):
#         self.hero = hero                # Объект героя
#         self._balance = balance         # Защищённый атрибут
#         self.__password = password      # Приватный атрибут
#
#     def login(self, password):
#         """Проверяет пароль."""
#         if self.__password == password:
#             print("Доступ разрешен!")
#             return True
#         else:
#             print("Неверный пароль!")
#             return False
#
#     @property
#     def full_info(self):
#         """Свойство (только чтение)"""
#         return f"Герой: {self.hero.name} | Баланс: {self._balance} золотых"
#
#     def get_bank_name(self):
#         return self.bank_name
#
#     def bonus_for_level(self):
#         return self.hero.level * 37
#
#
# my_hero = Hero(name="Paladin", level=15)
#
# account = BankAccount(hero=my_hero, balance=500, password="secure_pass_2026")
#
# print(f"Добро пожаловать в {account.get_bank_name()}!")
#
# account.login("wrong_pass")
# account.login("secure_pass_2026")
#
# print(account.full_info)
#
# bonus = account.bonus_for_level()
# print(f"Ваш бонус за {my_hero.level} уровень: {bonus} монет")
#
# print(account._balance)
#######################################################################
class Hero:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"{self.name}, Balance: {self.balance} SOM"

Azeroth = Hero(name="Azeroth", balance=100)
print(Azeroth)
##########
def __add__(self, other):
    if isinstance(other, Hero):
        new_name = f"{self.name} & {other.name}"
        new_balance = self.balance + other.balance

        return Hero(new_name, new_balance)

    if isinstance(other, (int, float)):
        return Hero(self.name, self.balance + other)

    return NotImplemented

hero1 = Hero("Azeroth", 100)
hero2 = Hero("Asgore", 210)
hero3 = hero1 =+ hero2
print(hero3.name)
print(hero3.balance)
##################################################
