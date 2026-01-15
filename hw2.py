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

        return f"{self.get_name()}, {self.get_role()}, {self.get_salary()}"

yan = Employee(name="Yan", role="Employee", salary=35000)

print(yan.get_info())
#############################
class BackendDeveloper(Employee):
    def __init__(self, name, role, salary, level):
        super().__init__(name, role, salary)
        self.name = name
        self.role = role
        self.salary = salary
        self.level = level

    def get_name(self):
        return f"Имя: {self.name}"

    def get_role(self):
        return f"Роль: {self.role}"

    def get_salary(self):
        return f"Заработная плата: {self.salary}"

    def get_info(self):
        return f"{self.get_name()}, {self.get_role()}, {self.get_salary()}, {self.get_level()}"

    def get_level(self):
        return f"уровень: {self.level}"

john = BackendDeveloper(name="John", role="Backend", salary=35000, level="junior")

mitch = BackendDeveloper(name="Mitch", role="Backend", salary=42000, level="middle")

satar = BackendDeveloper(name="Satar", role="Backend", salary=52500, level="senior")

print(john.get_info())
print(mitch.get_info())
print(satar.get_info())
####################################
class Manager(Employee):
    def __init__(self, name, role, salary,team_size):
        super().__init__(name, role, salary)
        self.team_size = team_size
    def get_info(self):
        return f"{self.get_name()}, {self.get_role()}, {self.get_salary()}, {self.get_team_size()}"

    def get_team_size(self):
        return f"размер команды:{self.team_size}"

michael = Manager(name="Michael", role="Manager", salary=70000, team_size=10)

print(michael.get_info())
#################################33
class Intern(Employee):

    def __init__(self, name, role, salary, month):
        super().__init__(name, role, salary)
        self.month = month

    def get_name(self):
        return f"Имя: {self.name}"

    def get_role(self):
        return f"Роль: {self.role}"

    def get_salary(self):
        return f"Заработная плата: {self.salary}"

    def get_month(self):
        return f"месяцы: {self.month}"

    def get_info(self):
        return f"{self.get_name()}, {self.get_role()}, {self.get_salary()}"

Kubat = Intern(name="Kubat", role="Intern", salary=17000, month=3)
print(Kubat.get_info())
###########################################
def print_salary(employee):
 return(employee.get_salary())

employees = [
    BackendDeveloper(salary=35000, name="Satar", role="Backend", level="senior"),
    Manager("Michael", role="Manager", salary=35000, team_size=10),
    Intern("Kubat", role="Intern", salary=35000, month=3),
]
print(print_salary(employees[0]))
print(print_salary(employees[1]))
print(print_salary(employees[2]))