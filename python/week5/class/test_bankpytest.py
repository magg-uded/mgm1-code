'''first test function'''
def test_insufficient_deposit():
    #arrange
    a = BankAccount(1)
    a.deposit(100)
    #act
    outcome = a.withdraw(200)
    #assert
    assert outcome == False

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

    def test_insufficient_deposit():
        #arrange
        a = BankAccount(1)
        a.deposit(100)
        #act
        outcome = a.withdraw(200)
        #assert
        assert outcome == False

    def test_negative_deposit():
        #arrange
        a = BankAccount(1)
        #act
        outcome = a.deposit(-100)
        #assert
        assert outcome == False
