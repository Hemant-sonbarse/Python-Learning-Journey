'''
Definition:
Encapsulation is the practice of bundling data and methods that operate on the data within a class and restricting direct access to some variables.

🔹 Example:
Think of a bank account:

You can’t access the balance directly.

You must use methods like deposit() and withdraw() to modify it.
'''

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds!")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}. Remaining balance: {self.__balance}")

    def get_balance(self):  # Getter method
        return self.__balance

# Creating an account
account = BankAccount(5000)
account.deposit(2000)  # Output: Deposited 2000. New balance: 7000
account.withdraw(1000)  # Output: Withdrew 1000. Remaining balance: 6000

# Trying to access private variable (will raise an error)
# print(account.__balance)  # ❌ AttributeError

# Correct way to access private data
print(account.get_balance())  # ✅ Output: 6000
