class BankAccount:
    def __init__(self, bank, account_name, account_balance):
        self.__name = self.set_name(account_name)
        self.__bank = self.set_bank(bank)
        self.__account_balance = self.set_balance(account_balance)

    def set_balance(self, balance):
        if not isinstance(balance, float):
            raise Exception
        return balance

    def set_name(self, name):
        if not isinstance(name, str):
            raise Exception
        return name

    def set_bank(self, bank):
        if not bank.isalpha():
            raise Exception
        return bank

    def get_balance(self):
        return self.__account_balance

    def get_name(self):
        return self.__name

    def get_bank(self):
        return self.__bank

    def update_balance(self, balance):
        self.__account_balance += balance
        return self.__account_balance

    def __str__(self):
        return f'{self.get_name()} -> {self.get_balance():.2f} ({self.get_bank()})'

accounts = []
data = input()

while data != 'end':
    bank = data.split(' | ')[0]
    name = data.split(' | ')[1]
    balance = float(data.split(' | ')[2])

    searched = list(filter(lambda x: x.get_bank() == bank and x.get_name() == name, accounts))
    
    if len(searched) == 0:
        account = BankAccount(bank, name, balance)
        accounts.append(account)
    else:
        index = accounts.index(searched[0])
        accounts[index].update_balance(balance)
    
    data = input()

sorted_accounts = sorted(accounts, key=lambda x: (-x.get_balance(), x.get_bank()))


for account in sorted_accounts:
    print(account)