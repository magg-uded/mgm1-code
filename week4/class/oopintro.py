#object oriented program relies on classes and objects
#program is structured as simple reusable code blueprints called classes
#classes used to create individual instances of objects
#building blocks of oop:
#   classes - blueprint of objects
#   objects - instances of classes
#   methods - represent behaviors
#   attributes - information stored in classes about objects

#principles of oop:
#   inheritance - child class inherit data and attributes from patent class
#   encapsulation - containing information in an object exposing only selected information
#   abstraction - only exposing high level public methods for accessing objects
#   polymorphism - many methods can do the same task

#class attributes
class Person:
    name = 'ken'

#constructor
#has special name __init__() and special parameter self
class Person:
    def __init__(self): #constructor method
        print('constructor invoked')

#instance attributes
class Person:
    nationality = 'ethiopian' #class attribute
    def __init__(self): #constructor
        self.name = '' #instance attribute
        self.age = 0 #instance attribute

#setting attribute values
class Person:
    #name and age parameters passed in constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

#setting default values of instance attributes
class Person:
    def __init__(self, name = 'ken', age = 30):
        self.name = name
        self.age = age

#class methods
#python function in a class is called class method - defined using def keyword
#each method must have self as first parameter
class Person:
    def __init__(self, name, age): #class constructor
        self.name = name
        self.age = age

    def py_class_method(self): #class method
        print('person name: ', self.name, 'age: ', self.age)
