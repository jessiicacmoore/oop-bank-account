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

my_account = BankAccount.create()
your_account = 
print(my_account.balance)
