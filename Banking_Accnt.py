class Account: 
    def __init__(self, title, balance): 
        self.title = title 
        self.balance = balance 
class SavingsAccount(Account): 
    def __init__(self, title, balance, interestRate): 
        super().__init__(title, balance) 
        self.interestRate = interestRate 

account = Account("Ashish", 5000) 
print(f"Account Title: {account.title}") 
print(f"Account Balance: {account.balance}") 

savings_account = SavingsAccount("Ashish", 5000, 5) 
print(f"Savings Account Title: {savings_account.title}") 
print(f"Savings Account Balance: {savings_account.balance}") 
print(f"Savings Account Interest Rate: {savings_account.interestRate}")