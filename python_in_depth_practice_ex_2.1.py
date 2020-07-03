class Bank_Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def display(self):
        print('O cliente ' + self.name + ' tem R$' + str(self.balance) + ' em conta.')

    def withdraw(self, withdraw):
       
        self.balance -= withdraw

    def deposit(self, deposit):
        
        self.balance += deposit


