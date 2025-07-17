# Encapsulation

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance


    def deposite(self, amount):
            self.balance+=amount
            print(f"Deposited successful. New Balance : ${self.balance}")

    def check_balance(self):
            print(f"Current Balance: {self.balance}")
        
    def withdraw(self, amount):
            self.balance-=amount
            print(f"Withdraw successful. New Balance : ${self.balance}")

account = BankAccount('12345678', 1000)
account.deposite(5000)
account.withdraw(70000)
account.check_balance()


class Employee:
        def __init__(self, name, emp_id, salary):
            self._name = name
            self._emp_id = emp_id
            self._salary = salary

        def calculaate_bonus(self):
              return self._salary*0.1

        def display_info(self):
            print(f"Name: {self._name}")
            print(f"Employe id: {self._emp_id}")
            print(f"Salary:${self._salary}")

employe = Employee("Bishal", 1,1000)
employe.display_info()
bonus = employe.calculaate_bonus()
print(bonus)


# Abstraction

class Rectangle:
        def __init__(self, len, wid):
            self.len = len
            self.wid = wid

        def calculate_perimeter(self):
            return 2*(self.len + self.wid)

        def get_perimeter(self):
            return self.calculate_perimeter()

rectangle = Rectangle(1,2)
perimeter = rectangle.get_perimeter()
print(perimeter)


# Inheritance

class Vehicle:
        def __init__(self, name, model, year, color):
            self.name=name
            self.model = model
            self.year=year
            self.color=color
        
        def display_info(self):
              print(f"Name: {self.name}")
              print(f"Model: {self.model}")
              print(f"Year: {self.year}")
              print(f"Color: {self.color}")

class Car(Vehicle):
        def __init__(self, name, model, year, color, num_doors):
            super().__init__(name, model, year, color)
            self.num_doors = num_doors

        def display_info(self):
            super().display_info()
            print(f"Number of doors: {self.num_doors}")


car = Car("toyota", 'thiss', 2022, 'red', 5)
car.display_info()