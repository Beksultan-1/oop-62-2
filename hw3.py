from asyncio import Transport
from http.client import CannotSendRequest


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def show_email(self):
        print(self.email)

    def _check_password(self, password_to_run):
        return password_to_run == self.password

    def change_password(self, old_password, new_password):
        if self._check_password(old_password):
            self.password = new_password
            return True
        return False


user = User("Ardager", "aboba@mail.com", "2874")

print(user.name)
user.show_email()

print(user._check_password("2874"))  # True
print(user._check_password("0000"))  # False

user.change_password("2874", "abcd")
print(user._check_password("abcd"))  # True
#####################################################################
from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def move(self):
        """Начинает движение."""
        pass


class Car(Transport):
    def move(self):
        print("машина начинает движение.")


class Bicycle(Transport):
    def move(self):
        print("педали начинают крутиться.")

car = Car("Chevrolet")
bike = Bicycle("BMX")

car.move()
bike.move()
