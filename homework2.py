# ✅ Задание
# 1.
# Базовый класс(обязательное)
# Создай базовый класс Employee(Сотрудник).
# Требования:
#
# Поля
# класса:
# name — имя
# сотрудника
# salary — базовая зарплата
# Методы:
# get_salary() — возвращает зарплату сотрудника
# get_role() — возвращает строку"Employee"
# get_info() — возвращает строку с информацией о сотруднике
#emp = Employee("Alex", 30000)
# print(emp.get_info())
# Имя: Alex | Роль: Employee | Зарплата: 30000
##############################################################################
class Employee:
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary

    def get_name(self):
        return f"Имя: {self.name}"

    def get_role(self):
        return f"Роль: {self.role}"

    def get_salary(self):
        return f"Заработная плата: {self.salary}"

    def get_info(self):
        # Вызываем внутренние методы через self
        return f"{self.get_name()}, {self.get_role()}, {self.get_salary()}"

# Создаем объект вне класса
yan = Employee(name="Yan", role="Employee", salary=35000)

print(yan.get_info())
