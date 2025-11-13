from abc import ABC, abstractmethod

# Princípio de Segregação da Interface

# Versão errada
# class Account(ABC):
#     @abstractmethod
#     def deposit(self, amount: float):...
#     @abstractmethod
#     def withdraw(self, amount: float):...
#     @abstractmethod
#     def apply_interest(self):...
#     @abstractmethod
#     def charge_fee(self):...

# class SavingsAccount(Account):
#     def deposit(self, amount: float): print(f"Depositou {amount}")
#     def withdraw(self, amount: float):print(f"Sacou {amount}")
#     def apply_interest(self):print("Aplicou juros")
#     def charge_fee(self):pass

# class CheckingAccount(Account):
#     def deposit(self, amount: float): print(f"Depositou {amount}")
#     def withdraw(self, amount: float):print(f"Sacou {amount}")
#     def apply_interest(self):pass
#     def charge_fee(self):print("Cobrou taxa")

class Depositable(ABC):
    @abstractmethod
    def deposit(self, amount: float):...

class Withdrawable(ABC):
    @abstractmethod
    def withdraw(self, amount: float):...

class InterestBearing(ABC):
     @abstractmethod
     def apply_interest(self):...

class FeeChargeable(ABC):
    @abstractmethod
    def charge_fee(self):...

class SavingAccount(Depositable, Withdrawable, InterestBearing):
    def deposit(self, amount: float): print(f"Depositou {amount}")
    def withdraw(self, amount: float):print(f"Sacou {amount}")
    def apply_interest(self):print("Aplicou juros")

class CheckingAccount(Depositable, Withdrawable, FeeChargeable):
    def deposit(self, amount: float): print(f"Depositou {amount}")
    def withdraw(self, amount: float):print(f"Sacou {amount}")
    def charge_fee(self):print("Cobrou taxa")





# Pesquisar: Métodos virtuais de C++    