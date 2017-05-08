""" Demonstrates virtual wallet """


class Wallet(object):
    """ Defines blue print for digital wallet """
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        """ Adds money to wallet
            1. Get amount to be deposited
            2. Update balance with amount
            3. Output = updated balance
        """
        if isinstance(amount, int):
            self.balance += amount
            return self.balance
        else:
            return TypeError("Please input a number")

    def withdraw(self):
        """ Withdraws money from wallet """
