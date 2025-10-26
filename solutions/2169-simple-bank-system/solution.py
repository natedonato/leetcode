class Bank:

    def __init__(self, balance: List[int]):
        self.accts = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self.exists(account1) or not self.exists(account2) or self.get(account1) < money:
            return False
        self.set_acct(account1, -money)
        self.set_acct(account2, money)
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self.exists(account) or money < 0:
            return False
        self.set_acct(account, money)
        return True
            

    def withdraw(self, account: int, money: int) -> bool:
        if not self.exists(account) or money < 0 or self.get(account) < money:
            return False
        self.set_acct(account, -money)
        return True

    def exists(self, account: int) -> bool:
        if account < 1 or account > len(self.accts) + 1:
            return False
        return True 

    def get(self, account):
        return self.accts[account - 1]
    
    def set_acct(self, account, diff):
        self.accts[account - 1] += diff

    

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
