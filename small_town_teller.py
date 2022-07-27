import pickle


class Person:


    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name


class Account:
    def __init__(self, number, account_type, owner, balance):
        self.acc_number = number
        self.acc_type = account_type
        self.owner = owner
        self.balance = balance

class Bank:
    def __init__(self):
        self.customers = {}
        self.accounts = {}


    def add_customer(self, first_name, last_name):
            if Person.id in self.customers:
                print("Customer already exists.")
            else:
                self.person[Person.id] = Person


    def add_account(self, account):
        if account.owner.id not in self.Person:
            print('ID is not a valid customer ID')
        elif account.number in self.accounts:
            print('Account ID already exists')
        else:
            self.account[account.number] = account

    def remove_account(self, account_id):
        if account_id in self.account:
            del self.account[account_id]
        else:
            print('Account number does not exist')

    def deposit(self, account_id, amount):
        if account_id in self.accounts:
            account = self.accounts.get(account_id)
            account.balance += amount

    def withdrawl(self, account_id, amount):
        if account_id in self.accounts:
            account = self.accounts.get(account_id)
            account.balance -= amount

    def balance_inquiry(self, account_id):
        if account_id in self.account:
            balance = self.account.get(account_id).balance
            return balance
        else:
            print('Account does not exist')

