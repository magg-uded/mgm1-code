#write test that defines desired behavior of your code
#run test to see if it fails
#write code to pass test
#Run test again to see if code produces expected ouput
#refactor code to make it efficient/ aesthetic
#repeat

'''the code below will throw a NameError since we are referencing Banking class but have not created it'''
import unittest #import unittest module

class Tdd_python(unittest.TestCase):
    def test_desired_result(self):
        bank = Banking()
        final_bal = bank.credit(1000)

        self.assertEqual(1000, final_bal)

#corrected code
import unittest

class Banking:
    def __init__(self):
        self.balance = 0

    def credit(self, amount):
        self.balance += amount
        return self.balance

class TestBanking(unittest.TestCase):
    def test_credit(self):
        bank = Banking()
        final_bal = bank.credit(1000)
        self.assertEqual(1000, final_bal)

'''example 2'''
import unittest

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):
    def test_add(self):
        result = add(10, 20)
        self.assertEqual(result, 30)

