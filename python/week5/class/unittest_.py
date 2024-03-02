'''test - can't withdraw more money that the deposit available'''
import unittest

class BankAccount:
    def __init__(self, id):
        self.id = id
        self.balance = 0

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def deposit(self, amount):
        self.balance += amount
        return True

#to test that we can't withdraw more than the deposti, add code below
class TestBankOperations(unittest.TestCase): #create a subclass of unittest.TestCase
    def test_insufficient_deposit(self): #define a single test function with a method that starts with 'test'
        #arrange
        a = BankAccount(1)
        a.deposit(100)
        #act
        outcome = a.withdraw(-200) #test when we deposit a -ve amount
        #assert
        self.assertFalse(outcome) #we expect this test method to return False

