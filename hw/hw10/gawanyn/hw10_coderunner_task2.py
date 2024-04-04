class BankAccount:
    def __init__(self, account_number, account_holder, balance = 0.0):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance

    @property
    def account_holder(self):
        return print(self.__account_holder)

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def check_balance(self):
        return self.__balance
    

    
# account = BankAccount("123456789", "John Wick", 100)

# print("Account_holder:", account.account_holder())
# print("Balance: ", account.check_balance())

# account.deposit(50)
# print("Balance after deposit: ", account.check_balance())

# account.withdraw(30)
# print("Balance after withdeaw: ", account.check_balance())