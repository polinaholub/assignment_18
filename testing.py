# Work from assignment 14:

class Account:
    def __init__(self, balance, account_number):
        self._balance = balance
        self._account_number = account_number
    
    @classmethod
    def create_account(cls, account_number):
        return cls(0.0, account_number)
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError('Amount must be positive')

    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
        else:
            raise ValueError('Amount must be positive')

    def get_balance(self):
        return self._balance
    
    def get_account_number(self):
        return self._account_number
    
    def __str__(self):
        return f'Account number: {self._account_number}, balance: {self._balance}'


class SavingsAccount(Account):
    def __init__(self, balance, account_number, interest_rate):
        super().__init__(balance, account_number)
        self._interest_rate = interest_rate

    def add_interest(self):
        interest_amount = self._balance * (self._interest_rate / 100)
        self._balance += interest_amount

    def __str__(self):
        return f'Savings Account number: {self._account_number}, balance: {self._balance}'


class CurrentAccount(Account):
    def __init__(self, balance, account_number, overdraft_limit):
        super().__init__(balance, account_number)
        self._overdraft_limit = overdraft_limit

    def send_overdraft_letter(self):
        if self._balance < 0:
            print(f'Overdraft letter sent for account {self._account_number}')

    def __str__(self):
        return f'Current Account number: {self._account_number}, balance: {self._balance}'


class Bank:
    def __init__(self):
        self._accounts = []

    def open_account(self, account):
        self._accounts.append(account)

    def close_account(self, account):
        if account in self._accounts:
            self._accounts.remove(account)
        else:
            print("Account not found")

    def pay_dividend(self, amount):
        for account in self._accounts:
            account.deposit(amount)

    def update(self):
        for account in self._accounts:
            if isinstance(account, SavingsAccount):
                account.add_interest()
            elif isinstance(account, CurrentAccount):
                account.send_overdraft_letter()

    def __str__(self):
        return f'Bank with {len(self._accounts)} accounts'
    

bank = Bank()


#Testing:

#Write a test for the Bank class that we wrote in 14 lesson. You should write a test for the open_account method. Ensure that the account is opened and has  balance.

import unittest
from unittest.mock import Mock

class TestBank(unittest.TestCase):

    def test_open_account(self):
        bank = Bank()
        mock_account = Mock()
        mock_account.get_balance.return_value = 250

        bank.open_account(mock_account)
        self.assertIn(mock_account, bank._accounts)
        self.assertEqual(mock_account.get_balance(), 250)

#Test update method. It should check that code added interest and sended a message (print function was called).

#update method:
# def update(self):
        #for account in self._accounts:
            #if isinstance(account, SavingsAccount):
                #account.add_interest()
            #elif isinstance(account, CurrentAccount):
                #account.send_overdraft_letter()


    def test_update(self):

        bank = Bank()

        mock_savings_acc = Mock()
        mock_current_acc = Mock()

        bank.open_account(mock_savings_acc)
        bank.open_account(mock_current_acc)

        bank.update()

        mock_savings_acc.add_interest.assert_called_once()
        mock_current_acc.send_overdraft_letter.assert_called_once()

if __name__ ==  '__main__':
    unittest.main()







            





mock = Mock()

