class Account:
    def __init__(self):
        self._balance=0
        
    @property
    def balance(self):
        return self._balance
    
    def deposite(self, n):
        self._balance +=n
        
    def withdraw(self,n):
        self._balance -=n
        
        
    def main():
        account= Account()
        print("Balance:" + account.balance)
        account.deposite(100)
        account.withdraw(50)
        print("Balance:" , account.balance)