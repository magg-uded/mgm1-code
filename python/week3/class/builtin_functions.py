#built_in functions
#these set of functions can be used without needing to import a library


#abs() - returns the absolute value of a numeric argument
num1 = 5 #using integers
num2 = -7

abs_num1 = abs(num1)
abs_num2 = abs(num2)

print('abs value of', num1, 'is', abs_num1)
print('abs value of', num2, 'is', abs_num2)

num3 = 3.14 #using floating numbers
num4 = -2.897

print('abs value of', num3, 'is', abs(num3))
print('abs value of', num4, 'is', abs(num4))

num5 = 3 + 4j
num6 = -4 - 6j

print('abs value of', num5, 'is', abs(num5))
print('abs value of', num6, 'is', abs(num6))

#all() - returns True if every item in an iterable evaluates to True, otherwise, it returns False.
numbers = [2, 3, 4, 8, 10] #define list of numbers
result = all(num % 2 == 0 for num in numbers) #check if every number in list is even
print(result)

#any() - takes in an iterable object such as a list or tuple and returns True if any of the elements in the iterable are True. If none of the elements in the iterable are True, returns False.
my_list = [False, True, False, False] #define list with some boolean values
result = any(my_list) #check if any element in the list is True
print(result)

#ascii() - receives as input an object containing string data, and returns the object as a printable representation with escapes for non-ASCII characters (accented characters).
my_string = 'hello, esta bien ċotť?' #define string with both ASCII and no-ASCII characters
print('original string: ', my_string)

ascii_rep = ascii(my_string) #convert to ascii
print('ascii string: ', ascii_rep)

#bin() - converts an integer into its binary equivalent string.
num = 42
binary_string = bin(num) #convert integer to binary string
print(f'binary equivalent of {num} is: {binary_string}') #0b in output shows output is in binary format

#bool() - converts a value to a Boolean True or False value.
print(bool(0)) #false
print(bool(0.0)) #false
print(bool(1)) #true - any non-zero numeric value, non-empty containers like lists, sets, dictionaries etc and non-empty strings evaluate to true
print(bool(-1)) #true
print(bool(0.1)) #true
print(bool(-3.14)) #true
print(bool('')) #false
print(bool('hello')) #true
print(bool([])) #false
print(bool([1, 2, 3])) #true

#breakpoint() - engages, configures, and changes the debugger program used in a script.
def divide(a, b): #define a function that divides a by b and returns result
    result = a / b
    return result

def main(): #set up variable x and y and call divide function with x and y
    x = 10
    y = 2 #throws error is this is 0

    #set breakpoint
    breakpoint() #umute to see how it works - before calling divide function, use breakpoint function to pause execution and allow us to inspect variable and step through the code with python debugger
    z = divide(x, y)
    print(f'result of division is: {z}')

if __name__ == '__main__': #checks if current script is the main script being executed and if so execute the main() function
    main()

#bytearray() - returns an array of the given bytes of an object.

#bytes() - returns a byte immutable object representing the given bytes of an object.

#callable() - returns True if an object is callable, and False if an object is not callable.

#chr() - returns Unicode characters represented by integers ranging between 0 and 1,114,111.

#classmethod() - converts a given function into a class method.
class MyClass:
    class_variable = 'i am a class variable'

    def __init__(self, value):
        self.value = value

    @classmethod
    def class_method(cls):
        print('this is a class method')
        print('accessing class variable: ', cls.class_variable)

    def instance_method(self):
        print('this is an instance method')
        print('accessing instance variable: ', self.value)

obj = MyClass('i am an instance variable') #creating an instance of MyClass
obj.instance_method() #calling the instance method
MyClass.class_method() #calling the class method

#compile() - returns a runnable code object created from a string.

#complex() - converts a given string into a complex number.
complex_str = input('enter a complex number: ')

try:
    complex_num = complex(complex_str) #convert input string into a complex number
    print('complex number is: ', complex_num)
except ValueError:
    print('invalid input, please enter a complex number')

#delattr() - allows the user to delete attributes from an object
class Person: #define a person class with name age attributes
    def __init__(self, name, age): #use special method __init__ to initialize the objects of class Person ie name and age
        self.name = name
        self.age = age

person = Person('alice', 30) #create an instance of the person class

print('before deletion: ') #display attributes before deletion
print('name: ', person.name)
print('age: ', person.age)

delattr(person, 'age') #delete age attribute from the object

print('\nafter deletion: ') #display attributes after deletion
print('name: ', person.name)

try: #try accessing deleted attribute - will raise an AttributeError
    print('age: ', person.age)
except AttributeError:
    print('age attribute has been deleted')


#dict() - initializes a new dictionary from mapping n-number of object (key, value) pairs.

#eval() - returns the value of a Python expression passed as a string.
expression = '3 + 4 * 2'
result = eval(expression)
print('evaluates to: ', result)

expression = '[x**2 for x in range(5)]'
result = eval(expression)
print('evaluates to: ', result)

#filter() - returns a filter object that applies a function to each item in an iterable and returns the values that are True.
def is_even(x): #define function to check if number is even
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #create a list of numbers

even_numbers = filter(is_even, numbers) #use filter() to filter out even numbers from list

even_numbers_list = list(even_numbers) #convert filter object to a list

print('even numbers are: ', even_numbers_list)


#float() - returns a float value based on a string, numeric data type, or no value at all.
str_value = '3.14' #converting string to float
float_value = float(str_value)
print('float value is: ', float_value)

int_value = 42 #int to float
float_value = float(int_value)
print('float is: ', float_value)

bool_value = True #boolean to float
float_value = float(bool_value)
print('float is: ', float_value)

float_value = float() #no value to float
print('float is: ', float_value)

invalid_str = 'abc' #handling invalid string input
try:
    float_value = float(invalid_str)
    print('float is: ', float_value)
except ValueError:
    print('invalid conversion to float')


#frozenset()- returns a new frozenset using an optional iterable object such as a string or list.

#hasattr() - returns True if an object has an attribute and False otherwise.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 30) # Create an instance of the Person class

has_name = hasattr(person, 'name') # Check if the object has the 'name' attribute
print("Does the object have the 'name' attribute?", has_name)  # Output: True

has_age = hasattr(person, 'age') # Check if the object has the 'age' attribute
print("Does the object have the 'age' attribute?", has_age)    # Output: True

has_gender = hasattr(person, 'gender') # Check if the object has the 'gender' attribute
print("Does the object have the 'gender' attribute?", has_gender)  # Output: False

#help() - displays documentation of an object using the Python help utility.
#help(list)
#import math
#help(math)
#help(str.upper)

#input() - prompts the user for data and returns it as a string.

#int() - takes in a value that can be converted into an integer, and returns a copy of the value in the int datatype.

#len() - returns the length of an object, which can either be a sequence or collection.

#list() - returns a list from an iterable.

#map() - returns an iterator that takes a function and applies it to every item in an iterable.
def square(x): #define function to square a number
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers) #apply square function to each item in list using map

new_list = list(squared_numbers) #convert map object to list

print('squared numbers: ', new_list)


#max() - returns the highest value from values given or an iterable.
num_list = [10, 5, 20, 15] #max value in list
print('max value is: ', max(num_list))

num_tuple = (10, 5, 20, 15) #max value in tuple
print('max value is: ', max(num_tuple))

max_val = max(10, 5, 15, 20) #max value in arguments in function
print('max value is: ', max_val)

strings = ['apple', 'banana', 'orange'] #max value from list of strings using lexicographical order
print('max value is: ', max(strings))

#min() - returns the lowest value from values given or an iterable.
num_list = [10, 5, 20, 15] #min value in list
print('min value is: ', min(num_list))

#next() - returns the next element from an iterable object.
my_list = [1, 2, 3, 4, 5] # Define an iterable object (in this case, a list)

my_iterator = iter(my_list) # Create an iterator from the iterable object

next_element = next(my_iterator) # Get the next element from the iterator using next()

print("Next element:", next_element)  # Output: 1

next_element = next(my_iterator) # Get the next element again
print("Next element:", next_element)  # Output: 2

#open() - used for opening files in a Python program.
file_path = '2.txt' #open a file named 2.txt in read mode
file = open(file_path, 'r')

file_contents = file.read() #read contents of file

print('contents of file') #print contents of file
print(file_contents)

file.close() #close file


#pow() - returns the value of a base number x to the power of an exponent y, with an optional modulus z.
print('2 raised to 3: ', pow(2, 3))

print('3 raised to power 4 with modulus 5: ', pow(3, 4, 5))

#print() - prints the string representation of an object.

#range() - returns a sequence of numbers based on the given range
sequence = range(5) #0 to 4
print("Sequence:", list(sequence))  # Output: [0, 1, 2, 3, 4]

sequence = range(1, 11) #1 to 10
print("Sequence:", list(sequence))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sequence = range(2, 11, 2) #2 to 10 in steps of 2
print("Sequence:", list(sequence))  # Output: [2, 4, 6, 8, 10]

#reversed() - takes in an iterator object, such as a list or string, and returns a reversed iterator object.
original_list = [1, 2, 3, 4, 5]
reversed_list = list(reversed(original_list)) #reverse original list and convert object to list

print('original list: ', original_list)
print('reversed list: ', reversed_list)

#round() - takes a number and an integer as parameters, and returns the number with decimal places equal to the integer.
print('rounded float: ', round(3.14159)) #round floating point number to nearest integer

print('rounded float: ', round(3.14159, 2)) #round floating point number to 2 decimal place

print('rounded float: ', round(12345.6789, -2)) #round floating point number to nearest integer


#set() - returns a new set based on an optional iterable object such as a list.
my_list = [1, 2, 3, 4, 5]
my_set = set(my_list)

print('my list: ', my_list)
print('my set: ', my_set)


#sorted() - takes in an iterator object, such as a list, tuple, dictionary, set, or string, and sorts it according to a parameter.
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3] #sorting list of numbers in ascending order
sorted_numbers = sorted(numbers)
print("Sorted numbers (ascending):", sorted_numbers)

fruits = ["apple", "banana", "orange", "kiwi", "grape"] #sorting a list of strings in alphabetical order
sorted_fruits = sorted(fruits)
print("Sorted fruits (alphabetical):", sorted_fruits)

word = "hello" #sorting a string in alphabetical order
sorted_word = sorted(word)
print("Sorted word (alphabetical):", sorted_word)

ages = {"Alice": 30, "Bob": 25, "Charlie": 35, "Abel": 43, "betty": 23} #sorting a dictionary by its keys
sorted_ages = sorted(ages.items())
print("Sorted ages (by keys):", sorted_ages)

numbers_set = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3} #sorting a set of numbers in descending order
sorted_numbers_set = sorted(numbers_set, reverse=True)
print("Sorted numbers set (descending):", sorted_numbers_set)

#str() - takes in a value that can be converted into a string, and returns a copy of the value in the string datatype.
num = 123 #converting int to str
num_str = str(num)
print("String representation of the integer:", num_str, type(num_str))

bool_value = True #boolean to str
bool_str = str(bool_value)
print("String representation of the boolean value:", bool_str, type(bool_str))

my_list = [1, 2, 3, 4, 5] #list to string
list_str = str(my_list)
print("String representation of the list:", list_str, type(list_str))

#super() - returns a temporary object that allows a given class to inherit the methods and properties of a parent or sibling class.
class Parent: #define a parent class with __innit__() method and greet() method
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f'hello, {self.name}'

class Child(Parent): #define child class that inherits from parent class
    def __init__(self, name, age): #use Child class' __init__() method to call parent class' __init__() method allowing child class to initialize the name attribute inherited from the parent class
        #call parent class's constructor using super()
        super().__init__(name)
        self.age = age

    def greet(self):
        #call parent class's greet() method using super()
        #extend greeting with additional information specific to the child class
        parent_greeting = super().greet()
        return f'{parent_greeting} i am {self.age} years old'

child = Child('alice', 5) #create instance of Child class

greeting = child.greet() #call greet() method of Child class
print(greeting)


#tuple() - creates a new tuple.
empty_tuple = tuple() #creating empty tuple
print('empty tuple: ', empty_tuple)

my_list = [1, 2, 3, 4, 5] #tuple from list
tuple_from_list = tuple(my_list)
print("Tuple from list:", tuple_from_list)  # Output: (1, 2, 3, 4, 5)

repeated_values = tuple("abc" * 3) #tuple with repeated values
print("Tuple with repeated values:", repeated_values)  # Output: ('a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c')

#type() - returns the data type of the argument passed to the function.

#zip() - takes multiple iterators as input and returns a single zip object made up of a list of tuples.
names = ['alice', 'bob', 'charlie'] #create two lists
ages = [30, 25, 34]

zip_object = zip(names, ages) #use zip to combine lists into a zip object of tuples
zip_list = list(zip_object) #convert zip object to a list of tuples

print('zipped list of tuples: ', zip_list)
