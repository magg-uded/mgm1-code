#weekly assignment

#1 large power
#declare global variable
base_line = 5000

#declare function that takes two variables
def large_power(base, exponent):
    #calculate result of base to power exponent
    result = base ** exponent

    if result > base_line:
        return True
        #print('number is greater than 5k')
    else:
        return False
        #print('number is not greater than 5k')

print(large_power(20, 4))

#2 divisible by ten
#declare function that takes one variable
def divisible_by_ten(num):
    #check if number is divisible by 10 and return boolean
    if num % 10 == 0:
        return True
    else:
        return False

print(divisible_by_ten(50))

