class BankAccount:
  interest_rate = 0.03
  accounts = []

  def __init__(self):
    self.balance = 0
  
  def deposit(self, amount):
    self.balance += amount

  def withdraw(self, amount):
    self.balance -= amount

  @classmethod
  def create(cls):
    account = BankAccount()
    cls.accounts.append(account)
    return account

  @classmethod
  def total_funds(cls):
    total = 0
    for account in cls.accounts:
      total += account.balance
    return total

  @classmethod
  def interest_time(cls):
    for account in cls.accounts:
      account.balance *= (1 + cls.interest_rate)


my_account = BankAccount.create()
your_account = BankAccount.create()
print(my_account.balance)
print(BankAccount.total_funds())
my_account.deposit(200)
your_account.deposit(1000)
print(my_account.balance)
print(your_account.balance)
print(BankAccount.total_funds())
BankAccount.interest_time()
print(my_account.balance)
print(your_account.balance)
print(BankAccount.total_funds())
my_account.withdraw(50)
print(my_account.balance)
print(BankAccount.total_funds())