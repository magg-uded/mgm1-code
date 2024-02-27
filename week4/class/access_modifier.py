#helps secure data from unathorized access and exploitation
#we use underscore (_)

#3 types of access modifiers

#public
#variables and methods declared inside the specific class can be accessed by that class and other classes outside
#all members in a python class are public by default

class Student: #example of public attributes
    school_name = 'plp academy' #class attribute

    def __init__(self, name, age):
        self.name = name #instance attribute
        self.age = age #instance attribute

>>> std = Student('ken', 25) #how to access public members via Thonny shell
>>> std.school_name
>>> std.name

>>> std.age = 23 #modify age to 23
>>> std.age

#protected
#members accessible from within class and subclasses
#specific resources of parent class canbe inherited by child class
#add prefix _ to instance
class Student:
    _schoolName = 'xyz school' #protected class attribute

    def __init__(self, name, age):
        self._name = name #protected instance attribute
        self._age = age #protected instance attribute

#how to access protected members
>>> std = Student('tembo', 25)
>>> std._name
>>> std._name = 'dax'
>>> std._name
>>> std._age

#private
#use double underscore __
class Student:
    __schoolName = 'xyz school' #private class attribute

    def __init__(self, name, age):
        self.__name = name #private instance attribute
        self.__age = age #private instance attribute
    def __display(self): #private method
        print('this is private method')

#accessing using Thonny
>>> std = Student('ken', 32)
>>> std._Student__name
'ken'
>>> std._Student__name = 'coy'
>>> std._Student__name
'coy'
>>> std._Student__display()
this is private method
>>>
