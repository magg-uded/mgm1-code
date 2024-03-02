#1#data types
    #built data structures incl List, tuple, set, dictionary
    #user-defined data structures include stack, tree, graph, queue, linked list and hash map
    #Lists, tuples, dictionaries, and sets are all iterable

##data type
num1 = 5
print(num1, 'is of type', type(num1))

num2 = 5.5
print(num2, 'is of type', type(num2))

num3 = 5+2j
print(num3, 'is of type', type(num3))

#list - ordered can be accessed by slicing index
#elements can be changed
languages = ["swift", "java", "python"]
print(languages)
print(languages[0])

#tuple - ordered but elements cannot be changed
product = ('xbox', 4.99)
print(product[0])

#set - unordered but elements cannot be sliced with indexing
student_id = {1, 2, 3, 4}
print(student_id, 'is of type', type(student_id))

#dictionary - ordered items in key-value pairs
#use key to extract value not other way round
capital_city = {'Nepal':'Kathmandu', 'Italy':'Rome',
                'England':'London'}
print(capital_city)
print(capital_city['Nepal'])

#2#type conversion
#conversion of one data type to another

##implicit - done automatically by python interpreter
integer_num = 123
float_num = 1.23
new_num = integer_num + float_num
print(new_num, 'is of data type',type(new_num))

##explicit - type casting using built in functions like int(), float(), str()
num_string = '12'
num_integer = 23

num_string = int(num_string)
print(num_string,'is now of data type', type(num_string))
num_sum = num_string + num_integer
print(num_sum)

#3#basic operations

#addition
a = 5
b = 2
print('sum: ', a+b)

a += b #a = a + b
print(a)

#subtraction
print('subtraction: ', a-b)

#multiplication
print('multiplication: ',a*b)

#division
print('division: ', a/b)

#modulo
print('modulo: ', a%b)

#floor division
print('floor division: ', a//b)

#power
print('power: ', a**b)

#assignment - assign values to variables
a = 4
b = 2

#subtraction
a -= b #a = a - b
print(a)

#multiplication
a *= b #a = a * b
print(a)

#division
a /= b #a = a / b
print(a)

#modulo
a %= b #a = a % b
print(a)

#exponent
a **= b #a = a**b
print(a)

##comparison - compares two values/ variables and returns a boolean result
a = 5
b = 2
print(a > b)
print('a == b =', a==b)
print('a != b =', a != b)
print('a > b =', a > b)
print('a < b =', a < b)
print('a >= b =', a >= b)
print('a <= b =', a <= b)

##boolean - to check if expression is true or false
a = 5
b = 6
print((a > 2) and (b >= 6))

##bitwise - act on operators as if they were strings of binary digits
#e.g. 2 is 10 and 7 is 111

##special
#identity
x1 = 5
y1 = 5
x2 = 'hello'
y2 = 'hello'
x3 = [1,2,3]
y3 = [1,2,3]

print(x1 is not y1)
print(x2 is y2)
print(x3 is y3) #x3 and y3 are equal but not identical since the interpreter locates them separately in memory

#membership
x = 'hello world'
y = {1:'a', 2:'b'}

print('h' in x) #print true since 'h' is in x
print('hEllo' not in x) #print false since hEllo is not in x
print(1 in y) #check if '1' key is present in y
print('a' in y) #check if 'a' key is present in y

#4#print function and taking user input

#end enables printing on same line else default /n enables things to be printed on separate lines
print('Good morning!', end= ' ')
print('It is rainy today')

#sep enables separation of output by commas or fullstops etc
print('New Year', 2023, 'See you soon!', sep= '; ')

#concatenation
print('PowerLP is' + ' awesome')

#output formatting - to make output aesthetically better
x = 5
y = 10
print('The value of x is {} and y {}'.format(x,y)) #curly braces are used as placeholders

#user input
num = int(input('Enter a number: '))
print('You entered:', num)
print('Data type of num:', type(num))
