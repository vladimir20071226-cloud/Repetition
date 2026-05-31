import unittest
from class1 import BankAccount
class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.acc=BankAccount("Вова", 9000)
    def test_to_genetive(self):
        self.assertEqual(BankAccount.to_genetive("Иван"), "Ивана")
        self.assertEqual(BankAccount.to_genetive("Вова"), "Вовы")
        self.assertEqual(BankAccount.to_genetive("Петя"), "Петя")
    def test_deposit_positive(self):
        self.acc.deposit(3000)
        self.assertEqual(self.acc.balance, 12000)
    def test_deposit_negative(self):
        with self.assertRaises(ValueError):
            self.acc.deposit(-500)
    def test_withdraw_valid(self):
        result=self.acc.withdraw(3000)
        self.assertEqual(result, 6000)
    def test_withdraw_invalid(self):
        with self.assertRaises(ValueError):
            self.acc.withdraw(12000)
    def test_balance_in_usd(self):
        self.assertEqual(self.acc.balance_in_usd, 100.0)