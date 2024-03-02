#lambda function
#special type of function without a name ie anonymous function
#useful for functions with simple expressions or when we want to use a function once
#use lambda keyword instead of def

#syntax
#lambda arguments(x): expression
#or
#lambda <function_parameter>: <return_value>

#below we define a lambda function and assign it to the variable snack
#then we call it to execute using snack()
snack = lambda: print('njugu')
snack() #calling the lambda

#lambda also accepts arguments like other functions
#lambda functions can take any number of functions but have only one expression
#example - function num_square takes an argument num and returns a square of num
def num_square(num):
    return num ** 2
print('square of num is: ', num_square(2))

#rewriting the above using lambda
num_square = lambda num: num ** 2 #num after lambda keyword specifies that lambda function accepts the argument num
print('square of num is: ', num_square(4)) #call lambda function in print function

#when to use lambda function
#when creating simple expressions that do not include comples conditionals or loops

#normal function to determine a palindrome
def is_palindrome(string):
    if (string == string[::-1]):
        return 'is palindrome'
    else:
        return 'is not palindrome'

#enter input string
string = input('enter string: ')

#call function and pass input from user
print(is_palindrome(string))

#rewrite above code using lambda function
is_palindrome = lambda string: 'is palindrome' if string == string[::-1] else 'is not palindrome'
string = input('enter string: ')

print(is_palindrome(string)) #calling the lambda function and passing the string argument
