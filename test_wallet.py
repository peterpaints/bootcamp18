""" Tests our wallet """

import unittest
from wallet import Wallet


class TestWallet(unittest.TestCase):
    """ Tests Wallet functionality """

    def setUp(self):
        """ Gives all test cases access to an instance of the Wallet """
        self.wallet = Wallet()

    def test_deposit_works(self):
        """ Checks that deposit adds money to wallet
            1. Get amount to be deposited
            2. Update balance with amount
            3. Output = updated balance
        """
        self.wallet.balance = 0
        self.assertEqual(self.wallet.deposit(1000), 1000)
        self.assertEqual(self.wallet.deposit(500), 1500)

    def test_amount_is_a_number(self):
        # self.assertEqual(self.wallet.deposit("1000"), "Please input a number")
        self.wallet.deposit("A thousand")
        self.assertRaises(Exception, "Please input a number")
