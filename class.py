import csv
import datetime
import unittest
class BankAccount:
    def __init__(self, owner:str, balance:float):
        self.owner=owner
        self.balance=balance
    @staticmethod
    def to_genetive(name: str)->str:
        cases = {"Иван": "Ивана",
                "Вова": "Вовы"}
        return cases.get(name, name)
    def __str__(self):
        ar=BankAccount.to_genetive(self.owner)
        return f"Счет {ar}: {self.balance} руб."
    def __repr__(self):
        return f"BankAccount({self.owner}, {self.balance})"
    def deposit(self, value):
        if value<0:
            raise ValueError("Запрещено вносить отрицательную сумму")
        self.balance+=value
    def withdraw(self, required):
        if required>self.balance:
            raise ValueError("Запрещено снимать больше, чем есть на счёте")
        return self.balance-required
    @property
    def balance_in_usd(self):
        return self.balance/90
    def __add__(self, other):
        return BankAccount(owner=f"{self.owner} + {other.owner}",
                           balance=self.balance+other.balance)
class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.acc=BankAccount("Вова", 9000)
    def test_to_genetive(self):
        self.assertEqual(BankAccount.to_genetive("Иван"), "Ивана")
        self.assertEqual(BankAccount.to_genetive("Вова"), "Вовы")
        self.assertEqual(BankAccount.to_genetive("Петя"), "Петя")
    def test_deposit_positive(self):
        self.acc.deposit(3000)
        self.assertEqual(self.acc.balance, 12000)
    def test_deposit_negative(self):
        with self.assertRaises(ValueError):
            self.acc.deposit(-500)
    def test_withdraw_valid(self):
        self.acc.withdraw(3000)
        self.assertEqual(self.acc.withdraw, 6000)
    def test_withdraw_invalid(self):
        with self.assertRaises(ValueError):
            self.acc.withdraw(12000)
    def test_balance_in_usd(self):
        self.assertEqual(self.acc.balance_in_usd, 100.0)
class Stack:
    def __init__(self, stack:list):
        self.stack=stack
    def __len__(self):
        return len(self.stack)
    def __str__(self):
        return f"Stack({self.stack})"
    def __contains__(self, item):
        return item in self.stack
    def __iter__(self):
        return reversed(self.stack)
    def __eq__(self, other):
        return self.stack==other.stack
    def peek(self):
        if not self.stack:
            raise IndexError("Нету стека")
        return self.stack[-1]
    def push(self, item):
        self.stack.append(item)
    def pop(self, item):
        if len(self.stack)==0:
            raise IndexError("Поптыка pop() из пустого стека")
        self.stack.pop(item)

class Vehicle:
    def __init__(self, make, year, model):
        self.make=make
        self.year=year
        self.model=model
    def describe(self):
        return f"Марка:{self.make}, Модель:{self.model}, Год выпуска:{self.year}"
    def __str__(self):
        return f"{self.make} {self.year} {self.model}"
    def __lt__(self, other):
        return self.year<other.year
    def __eq__(self, other):
        return self.year==other.year
# cars=[Vehicle("Toyota", 2020, "Corolla"),
#     Vehicle("Honda", 2018, "Civic"),
#     Vehicle("Tesla", 2023, "Model S"),
#     Vehicle("BMW", 2019, "X5")]
# sorted_cars=sorted(cars)
# for car in sorted_cars:
#     print(car)
class Car(Vehicle):
    def __init__(self, make, year, model, doors):
        super().__init__(make, year, model)
        self.doors=doors
    def __str__(self):
        base=super().__str__()
        return f"{base}, {self.doors}"
    def describe(self):
        base=super().describe()
        return f"{base}, Кол-во дверей:{self.doors}"
class ElectricCar(Vehicle):
    def __init__(self, make, year, model, doors, battery_capacity,efficiency):
        super().__init__(make, year, model)
        self.doors=doors
        self.battery_capacity=battery_capacity
        self.efficiency=efficiency
    def __str__(self):
        base=super().__str__()
        f"{base}, {self.battery_capacity}, {self.efficiency}"
    def describe(self):
        base=super().describe()
        return f"{base}, Кол-во дверей: {self.doors}, Емкость батареи:{self.battery_capacity}, Расход энергии в час: {self.efficiency}"
    def charge_time(self, km, charger_power=50):
        required_energy=km / self.efficiency
        hours=required_energy / charger_power
        return f"Для {km} км нужно заражать примерно {hours:.2f} ч."
class Truck(Vehicle):
    def __init__(self, make, year, model, doors, cargo_capacity):
        super().__init__(make, year, model)
        self.doors = doors
        self.cargo_capacity=cargo_capacity
    def __str__(self):
        base=super().__str__()
        return f"{base}, {self.cargo_capacity}"
    def describe(self):
        base=super().describe()
        return f"{base}, {self.cargo_capacity}"
    def __lt__(self, other):
        return super().__lt__(other)
    def __eq__(self, other):
        return super().__eq__(other)
t1 = Truck("Volvo", 2018, "FH16", 2, 20000)
t2 = Truck("MAN", 2020, "TGX", 2, 18000)
t3 = Truck("Scania", 2020, "R500", 2, 22000)
print(t1 > t2)
print(t2 == t3)
class CSVLogger:
    def __init__(self, filename):
        self.filename=filename
        self.writer=None
        self.file=None
    def __enter__(self):
        self.file=open(self.filename, mode="a", newline="", encoding="utf-8")
        self.writer=csv.writer(self.file)
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.writer.writerow([datetime.datetime.now(), f"ERROR: {exc_val}"])
        self.file.close()
        return False
    def log(self, message):
        self.writer.writerow([datetime.datetime.now(), message])
# class UserProfile:
#     def __init__(self, username: str, email: str, age:int, full_name:str):
#         self.username=username
#         self._email=email
#         self._age=age
#         self.full_name=full_name
#     @property
#     def username(self):
#         return self._username
#     @username.setter
#     def username(self, name_user:str):
#         if not (3<=len(name_user)<=20 and name_user.isalnum()):
#             raise ValueError("Должно быть от 3 до 20 символов, и включать только буквы/цифры")
#         self._username=name_user
#     @property
#     def email(self):
#         return self._email
#     @email.setter
#     def email(self, user_email:str):
#         if not ('@' in user_email):
#             raise ValueError("Должно быть @ и .")
#         self._email=user_email
#     @property
#     def age(self):
#         return self._age
#     @age.setter
#     def age(self, value: int):
#         if not (3<=value<=120):
#             raise ValueError("Должен быть в диапозоне от 3 до 120")
#         self._age=value
#     @property
#     def fullname(self):
#         return self.full_name.split(" ")
#     @staticmethod
#     def is_strong_password(pwd:str) -> bool:
#         if len(pwd)<8 or not any(ch.isdigit() for ch in pwd):
#             raise ValueError("Пароль должно состоять из 8 символов, и включать только буквы/цифры")
#         return True
#     @property
#     def data(self):
#         dictionary={"username": self.username,
#                     "email": self.email,
#                     "age": self.age,
#                     "full_name": self.full_name}
#         return dictionary
#     @classmethod
#     def from_dict(cls, data:dict):
#         return cls(username=data["username"],
#                    email=data["email"],
#                    age=data["age"],
#                    full_name=data["full_name"])
# data={"username": "Ivan123", "email": "ivan@mail.com", "age": 25, "full_name": "Иван Петров"}
# user=UserProfile.from_dict(data)
# user_1=UserProfile.is_strong_password("vova123@gmail.com")
# print(user_1)
class InsufficientStockError(Exception):
    def __init__(self, product_name:str, requested:int, available:int):
        self.product_name=product_name
        self.requested=requested
        self.available=available
        super().__init__(f'Товар {self.product_name}: запрошено {self.requested}, в наличии только{self.available}')









