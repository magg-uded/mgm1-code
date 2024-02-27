#super() function
#makes child class inherit all the methods and properties from its parent

class Company():
    def company_name(self):
        return 'google'

class Employee(Company):
    def info(self):
        #calling super class method using super() function
        c_name = super().company_name()
        print('ken works at', c_name)

#creating object of the child class
emp = Employee()
emp.info()


