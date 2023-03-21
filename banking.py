from abc import ABCMeta, abstractmethod
from random import randint

class Account(metaclass = ABCMeta):
    @abstractmethod
    def createAccount(self):
        pass

    @abstractmethod
    def autenticate(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def displayBalance(self):
        pass


class SavingsAccount(Account):
    def __init__(self):
        self.savingsAccount = {}
    def createAccount(self, name, initialDeposit):
        self.accountNumber = randint(10000, 99999)
        self.savingsAccount[self.accountNumber] = [name, initialDeposit]
    def authenticate(self, name, accountNumber):
        if accountNumber in self.savingsAccount.keys():
            if self.savingsAccount[accountNumber][0] == name:
                print("Authentication succesfull")
                self.accountNumber = accountNumber
                return True
            else:
                print("Authentication failed")
                return False
        else:
            print("Authentication failed")
            return False
    def withdraw(self, withdrawalAmount):
        if withdrawalAmount > self.savingsAccount[self.accountNumber][1]:
            print("Insufficient amount")
        else:
            self.savingsAccount[self.accountNumber][1] -= withdrawalAmount
            print("Withdrawal was succesfull. Avaliable balance: ", self.savingsAccount[self.accountNumber][1])

    def deposit(self, depositAmount):
        self.savingsAccount[self.accountNumber][1] += depositAmount
        print("Deposit was succesfull. Avaliable balance: ", self.savingsAccount[self.accountNumber][1])
    def displayBalance(self):
        print("Avaliable balance: ", self.savingsAccount[self.accountNumber][1])



