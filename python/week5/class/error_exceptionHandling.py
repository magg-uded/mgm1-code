#errors encountered during execution are called exceptions
#handling exceptions offers an altertanive path to avoid crashing your program, ruining ux etc

'''try---except example 1 KeyError'''
#dictionary with registered student names
registered_students = {
    'john': 'John Doe',
    'jane': 'Jane Smith',
    'alice': 'Alice Hart'
}

#function to check if student's name is registered
def check_registration(student_name):
    try:
        #check if student's name is in dictionary
        full_name = registered_students[student_name.lower()] #convert to lower case for case insensitive check
        print(f'{student_name} is registered as {full_name}')
    except KeyError:
        print(f'{student_name} is not registered')

#use while loop to continuously prompt user for input
while True:
    #get input from user
    student_name = input('enter student name (or "quit" to exit): ').strip()

    #check if user wants to quit
    if student_name.lower() == 'quit':
        break

    #check if student's name is registered
    check_registration(student_name)

'''try---except example 2 ZeroDivisionError'''
try:
    numerator = int(input('enter the numerator: '))
    denominator = int(input('enter the denominator: '))

    result = numerator/ denominator
    print('result of division: ', result)

except ZeroDivisionError:
    print('error: cannot divide by zero')
except ValueError:
    print('error: invalid input. please enter an integer')

'''try---except example 3 multiple exceptions one except'''
try:
    numerator = int(input('enter the numerator: '))
    denominator = int(input('enter the denominator: '))

    result = numerator/ denominator
    print('result of division: ', result)

except (ZeroDivisionError, ValueError):
    print('error: invalid input or division by zero')

'''try---except example 4 using another function'''
def inner_function():
    #division by zero will raise a ZeroDivisionError
    result = 1 / 0

def outer_function():
    try:
        #call inner function within try block
        inner_function()
    except ZeroDivisionError:
        print('zero division error caught in outer function')

try:
    #call outer function
    outer_function()
except ZeroDvisionError:
    print('zero division error caught in top level code')

'''try---except---else'''
def divide_numbers(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        print('error: cannot divide by zero')
    else:
        print('division successful')
        return result

#example usage
numerator = 10
denominator = 2
result = divide_numbers(numerator, denominator)
if result is not None:
    print('result: ', result)

'''try---except---else---finally'''
def divide_numbers(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        print('error: cannot divide by zero')
    else:
        print('division successful')
        return result
    finally: #regardless of whether exception occurs code inside finally is always executed
        print('finally block executed, cleaning up resources...')

#example usage
numerator = 10
denominator = 2
result = divide_numbers(numerator, denominator)
if result is not None:
    print('result: ', result)
