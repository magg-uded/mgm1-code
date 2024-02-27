#child class inherots all data members, properties and functions of parent class
#e.g. we can create a car by inheriting properties of a vehicle like wheels, colors, fuel tank, engine
#and add extra properties in car as desired

#syntax:
#   class ParentClass:
#       body of Parent class
#   class ChildClass(ParentClass):
#       body of Child class

#5 types of inheritance

#single - child class inherits from single parent class
class Vehicle: #create base or parent class
    def Vehicle_info(self):
        print('inside Parent(Vehicle) class')

class Car(Vehicle): #create child class
    def car_info(self):
        print('inside Child(Vehicle) class')

car = Car() #create object of Car

car.Vehicle_info() #access Vehicle's info using car object
car.car_info()

#multiple - child class inherits from multiple parent classes
class Person: #create first parent class
    def person_info(self, name, age):
        print('inside Person class')
        print('name: ', name, 'age: ', age)

class Company: #create second parent class
    def company_info(self, company_name, location):
        print('inside company class')
        print('name: ', company_name, 'location: ', location)

class Employee(Person, Company): #create child class that inherits from bothh parents
    def employee_info(self, salary, skill):
        print('inside employee class')
        print('salary: ', salary, 'skill: ', skill)

emp = Employee() #create object of employee

emp.person_info('john', 20)
emp.company_info('msft', 'seattle')
emp.employee_info(15000, 'ai')

#multi-level - chain of classes. child inherits from parent that inherits from grandparent
class Vehicle: #create base class ie super class/ grandparent
    def vehicle_info(self):
        print('inside vehicle class')

class Car(Vehicle): #create child class ie parent in this case
    def car_info(self):
        print('inside car class')

class SportsCar(Car): #create child class
    def sports_car_info(self):
        print('inside sportscar class')

s_car = SportsCar() #create object of SportsCar

s_car.vehicle_info() #use object to access Vehicle and Car info
s_car.car_info()
s_car.sports_car_info()

#hierarchical - multiple derived child classes from a single parent
class Vehicle:
    def info(self):
        print('this is vehicle')

class Car(Vehicle):
    def car_info(self, name):
        print('car name is:', name)

class Truck(Vehicle):
    def truck_info(self, name):
        print('truck name is:', name)

obj1 = Car()
obj1.info()
obj1.car_info('benz')

obj2 = Truck()
obj2.info()
obj2.truck_info('leland')

#hybrid - child inherits from grandparents and parents ie combined
#e.g. hierarchical and multiple inheritance example below
class Vehicle:
    def vehicle_info(self):
        print('inside vehicle class')

class Car(Vehicle):
    def car_info(self):
        print('inside car class')

class Truck(Vehicle):
    def truck_info(self):
        print('inside truck class')

class SportsCar(Car, Vehicle): #sportscar can inherit properties from vehicle and car
    def sports_car_info(self):
        print('inside sportscar class')

s_car = SportsCar() #create object

s_car.vehicle_info()
s_car.car_info()
s_car.sports_car_info()





