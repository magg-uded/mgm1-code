#strings#
#sequence of characters
#use '' or "" for representation

##accessing characters in strings
#indexing
greet = "hello"
print(greet[1])

#negative indexing
greet = "hello"
print(greet[-4]) #prints 'e' since we begin from -1

#slicing
greet = "hello"
print(greet[1:4]) #excludes 4th index 'o'

#python strings are immutable
#but we assign a variable name to a new string
message = "hola amigo"
# message[0] = 'l' #cannot change value at specific index returns error
message = "hello friends"
print(message)

#multiline string - use triple single quotes
message = '''
Never gonna give you up
Never gonna let you down
'''
print(message)

##string operations
#comparison - using == operator
str1 = 'hello, world'
str2 = 'i love you'
str3 = 'hello, world'

print(str1 == str2)
print(str1 == str3)

#join strings
greet = 'hello, '
name = 'jack'

result = greet + name
print(result)

#iterating through strings
greet = 'hello'

for letter in greet:
    print(letter)
    
#size of string
greet = 'hello'

print(len(greet))

#string membership test
print('a' in 'program') #true
print('at' not in 'battle') #false

##methods
#capitalize() - convert first character to upper case
txt = 'hello, and welcome to my world'
x = txt.capitalize()
print(x)

#casefold() - converts string into lower case
txt = 'Hello, And Welcome to My WORLD'
x = txt.casefold()
print(x)

#center() - returns a centered string
txt = 'banana'
x = txt.center(30)
print(x)

#count() - number of times specified value occurs in string
txt = "I love apples, apple are my favorite fruit"
x = txt.count('apple') #twice since count is sequential
print(x)

#encode() - runs encoded version of string UTF-8
txt = "My name is Ståle"

x = txt.encode()
print(x)

#endswith() - return true if string ends with specified value
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)

#expandtabs() - sets tab sizing of string
txt = "H\te\tl\tl\to"
x = txt.expandtabs(3)
print(x)

#find() - searches string for specified value and returns position
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

#format() - formats specified values in a string
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

quantity = 3
itemno = 560
price = 50
myorder = 'i want {} pieces of item number {} for {:.2f} dollars'
print(myorder.format(quantity, itemno, price))
      
#format_map() - formats specified values in string
point = {'x':4, 'y':-5}
print('{x} {y}'.format_map(point))

point = {'x':4, 'y':-5, 'z':0}
print('{x} {y} {z}'.format_map(point))

#index() - searches string for specified value and returns position
txt = "Hello, welcome to my world."
x = txt.index('to')
print(x)

#isalnum() - returns True if all chxters in string are alphanumeric
txt = "Company12"
x = txt.isalnum() #True
print(x)

#isalpha() - returns True if all chxts in string are in the alphabet
txt = "CompanyX"
x = txt.isalpha()
print(x)

#isascii()
txt = "Company123"
x = txt.isascii()
print(x)

#isdecimal()
txt = "1234"
x = txt.isdecimal()
print(x)

#isdigit() - returns true if all chxts in string are digits
txt = "50800"
x = txt.isdigit()
print(x)

#isidentifier() - returns true if string is a valid identifier ie letters, number 0-9 pr underscore - no spaces or start with number
txt = 'Demo'
x = txt.isidentifier()
print(x)

#islower - true if all chxts are lower case
txt = "hello world!"
x = txt.islower()
print(x)

#isupper - true if all chxts are upper case
txt = "heLlo WOrld!"
x = txt.islower()
print(x)

#isnumeric() - if all numeric
#isprintable() - all are printable
txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)

#isspace() - true if all are whitespaces
txt = "   "
x = txt.isspace()
print(x)

#istitle() - if string follows rules of title ie each word starts in upper case
txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)

#join() - convert elements of an iterable into a string
my_tuple = ('john ', 'peter ', 'ceck')
x = '#'.join(my_tuple)
print(x)

#ljust() - returns left-justified version of string
txt = "banana"
x = txt.ljust(20)
print(x, 'is my favorite fruit')

#lower() - converts string to lower case
#rjust() does the opposite
txt = "Hello my FRIENDS"
x = txt.lower()
print(x)

#upper() - converts string to upper case
txt = "hello my friends"
x = txt.upper()
print(x)

#lstrip() - returns left trim of string
txt = "     banana     "
x = txt.lstrip()
print('of all fruits', x, 'is my fav')

#rstrip - right trims
txt = "     banana     "
x = txt.rstrip()
print('of all fruits', x, 'is my fav')

#maketrans() - use mapping table to make translations
txt = "Hello Sam!"
mytable = str.maketrans('S', 'P')
print(txt.translate(mytable))

#partition() - returns tuple where string is partitioned into 3 parts
#eveything before match
#'bananas'
#everything after match
txt = "I could eat bananas all day"
x = txt.partition('bananas')
print(x)

#replace() - replace specified value with specified value
txt = "I like bananas"
x = txt.replace('bananas', 'apples')
print(x)

#rsplit() - split string at specified separator and returns list
#split string using comma followed by space as separator
txt = "apple, banana, cherry"
x = txt.rsplit(',')
print(x)

#split() - split string at specified separator and return list
txt = "welcome to the jungle"
x = txt.split()
print(x)

#splitlines() - split string at line breaks and return list
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)

#startswith() - returns true if string starts ith specified value
txt = "Hello, welcome to my world."
x = txt.startswith('Hello')
print(x)

#strip() - returns trimmed version of string
txt = '      banana     '
x = txt.strip()
print(x)

#swapcase() - lower to upper case and vice versa
txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)

#zfill() - fills string with specified number of 0 values at beginning
txt = '50'
x = txt.zfill(10)
print(x)

##escape sequence
    #escape some of the chxts inside a string
    #example = "He said, "What's there?""
    #print(example) #throws error
example = "He said, \"What's there?\"" #escape double quotes
print(example)

example = 'He said, "What\'s there?\"' #escape single quotes
print(example)

##string formatting
#f-strings make it easy to print values and variables elegantly
name = 'cathy'
country = 'uk'
print(f'{name} is from the {country}')