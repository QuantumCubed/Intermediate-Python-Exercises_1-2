class BankAccount:

    account_name = "John Doe"
    starting_balance = 0.00

    def __init__(self, account_name, starting_balance):
        self.account_name = account_name
        self.starting_balance = starting_balance

    def deposit(self, amount):
        self.starting_balance += amount

    def withdraw(self, amount):
        self.starting_balance -= amount

    def get_balance(self):
        return "Account Name: {} \nBalance: {}".format(self.account_name, self.starting_balance)
