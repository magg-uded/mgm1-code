#python function
#modular code that can be used repeatedly
#block of code that is executed when called from somewhere in the program
#has a return value

#structure of functions without parameters
#def <function_name>:
#    <task to complete>

#structure of functions with parameters
#def <function_name(a, b)>:
#    <task to complete>

#example without parameters
def add_nums():
    print(2 + 13) #to get add_nums function to give an output we must call it
                  #to call add_nums we use add_nums()
add_nums()

#example taking parameters
def add_nums(a, b):
    answer = a + b
    return answer

#assign function call to varable called total
total = add_nums(2, 13)
print('total: ', total)

#arbitrary arguments *args
#if you DON'T know how many arguments are going to be passed in your argument add * before the parameter name in the function
def add_nums(*nums):
    sum = 0
    for num in nums:
        sum += num
    return sum
print('total: ', add_nums(2, 5, 6, 7, 8, 13))

