#functions and variable scopes
#there are 4 scopes: local, enclosing, global and built-in

#local scope
#variable declared inside a function
def add_nums(a, b):
    answer = a + b #local variable declared inside a function
    return answer
print(add_nums(2, 13)) #calling our function inside the print statement

#enclosing scope
#function declared inside another function ie nested function
def add_nums(a, b):
    answer = a + b #enclosed variable declared inside a function
    def double_it():
        double = answer * 2 #this variable cannot be accessed from inside the add_nums function
        print(double)
    double_it() #calling our inner function
    return answer
print(add_nums(2, 13)) #calling our function inside print statement

#global scope
#variable is declared outside of a function
#function can be accessed from anywhere
global_var = 13

def add_nums(a, b):
    total = a + b #enclosed scope variable declared inside a function
    print('global_var in outer function: ', global_var)
    def double_it():
        double = total * 2
        print('global_var in inner function: ', global_var)
        print('double: ', double)
    double_it()
    return total

add_nums(13, 5)

#note - call any variables declared
#if function does not take parameters call it without variablein print statement or not
#if function takes parameters call it with parameters in print statement or not
