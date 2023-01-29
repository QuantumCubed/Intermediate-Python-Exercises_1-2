from BankAccount import BankAccount

acc_1 = BankAccount("John Doe", 100.00)
acc_1.withdraw(25.00)
acc_1.deposit(75.00)
print(acc_1.get_balance())
