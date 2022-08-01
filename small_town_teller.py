import pickle


class Person:

    def __init__(self, person_id, first_name, last_name):
        self.person_id = person_id
        self.first_name = first_name
        self.last_name = last_name


class Account:
    def __init__(self, number, account_type, owner):
        self.number = number
        self.acc_type = account_type
        self.owner = owner
        self.balance = 0

class Bank:
    def __init__(self):
        self.customers = {}
        self.accounts = {}


    def add_customer(self, customer):
        if customer.person_id in self.customers:
            print("Customer already exists.")
        else:
            self.customers[customer.person_id] = [customer.first_name, customer.last_name]
            print('Customer ' + str(customer.person_id) + 'added.')


    def add_account(self, account):
        if account.owner.person_id not in self.customers:
            print('ID is not a valid customer ID')
        elif account.number in self.accounts:
            print('Account ID already exists')
        else:
            self.accounts[account.number] = [account.acc_type, account.owner, account.balance]
            print('Account added')

    def remove_account(self, account_id):
        if account_id in self.accounts:
            del self.accounts[account_id]
            print('Account deleted')
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
        if account_id not in self.accounts:
            print('Account does not exist')
        else:
            balance = self.accounts[account_id][3]
            print('Your balance is: $' + str(balance))


            # def balance_inquiry(self, account_id: int):
            #     if account_id in self.account:
            #         balance = self.account.get(account_id).balance
            #         return round(balance, 2)
            #     else:
            #         raise ValueError(f'Account with id {account_id} does not exist.')

                    # ef
            # balance_inquiry(self, accountNum):
            # print(accountNum)
            # if accountNum not in self.accounts.keys():
            #     print('Your account number does not exist')
            # else:
            #     return 'Balance Inquiry: Account number ' + str(accountNum) + ' has a balance of ' + '{:.2f}'.format(
            #         self.accounts[accountNum][3]) + ' dollars\n'



# Append the following methods to the Bank class:
#
# save_data
# load_data

    def save_data (self):
        curr_data = [self.customers, self.accounts]
        with open ('./customer_accounts saved', 'wb') as f:
            pickle.dump(curr_data, f)

    def load_data(self):
        with open('./customer_accounts saved', 'rb') as f:
            loaded = pickle.load(f)
        del(self.customers)
        del(self.accounts)
        self.customers = loaded[0]
        self.accounts = loaded[1]


