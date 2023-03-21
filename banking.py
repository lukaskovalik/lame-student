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
        print("Account creation has been succesfull. Your accunt number is: ", self.accountNumber)

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
            print("Withdrawal was succesfull")
            self.displayBalance()

    def deposit(self, depositAmount):
        self.savingsAccount[self.accountNumber][1] += depositAmount
        print("Deposit was succesfull")
        self.displayBalance()

    def displayBalance(self):
        print("Avaliable balance: ", self.savingsAccount[self.accountNumber][1])

savingAccount = SavingsAccount()
while True:
    print("Enter 1 to create a new account")
    print("Enter 2 to access an existing account")
    print("Enter 3 to exit this program")
    userInput = int(input())
    if userInput == 1:
        print("Enter your name")
        name = input()
        print("Enter your initial deposit")
        deposit = int(input())
        savingAccount.createAccount(name, deposit)
    elif userInput == 2:
        print("Enter your name")
        name = input()
        print("Enter your initial deposit")
        deposit = int(input())
        autenticationStatus = savingAccount.authenticate(name, accountNumber)
        if autenticationStatus is True:
            while True:
                print("Enter 1 to withdraw")
                print("Enter 2 to deposit")
                print("Enter 3 to display avaliable balance")
                print("Enter 4 to go back to previous menu")
                userInput = int(input())
                if userInput == 1:
                    print("Enter a withdrawal amount")
                    withdrawalAmount = int(input())
                    savingAccount.withdraw(withdrawalAmount)
                elif userInput == 2:
                    print("Enter an amount to be deposited")
                    depositAmount = int(input())
                    savingAccount.deposit()
                elif userInput == 3:
                    savingAccount.displayBalance()
                elif userInput == 4:
                    break
    elif userInput == 3:
        quit()
