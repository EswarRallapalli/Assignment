""".Create an abstract class BankAccount with methods deposit(), withdraw(), and get_balance(). 
Then, create two subclasses:

SavingsAccount, where the withdraw() method ensures that the balance cannot go below $500.
CurrentAccount, where the withdraw() method allows the balance to go negative (up to $1000 overdraft).
Ensure that only deposit() and withdraw() are exposed to the user, and the balance is encapsulated (hidden).
"""
from abc import ABC ,abstractmethod
class BankAccount(ABC):
    def __init__(self,initial_balance):
        self._balance=initial_balance
    @abstractmethod
    def deposit(self,amount):
        
        pass
    @abstractmethod
    def withdraw(self,amount):
        pass
    def get_balance(self):
        pass

class SavingAccount(BankAccount):
    def deposit(self, amount):
         if amount>0:
          self._balance += amount
         else:
             print("Deposit amount must be Positive.")
    def withdraw(self, amount):
        if amount>0:
            if self._balance - amount>=500:
                self._balance -=amount
            else:
                print("Cannot withdraw. Balance  cannot go below $500.")
        else:
            print("Withdraw amount must be positive.")
class CurrentAccount(BankAccount):
    def deposit(self, amount):
        if amount>0:
            
            self._balance += amount
        else :
            print("Desposit amount is postive.")
    def withdraw(self, amount):
        if amount>0:
            if self._balance-amount>=-1000:
                self._balance -=amount
            else:
                print("Cannot withdraw. Balance  cannot go below $500")
        else:
            print("withdrawal amount must be positive.")
    def get_balance(self):
        return self._balance
    
savings=SavingAccount(1000)
current= CurrentAccount(1000)

savings.deposit(500)
print(savings.get_balance())
savings.withdraw(1200)
print(savings.get_balance())
current.withdraw(1500)
print(current.get_balance())
current.withdraw(200)
print(current.get_balance())
    
        
    
    