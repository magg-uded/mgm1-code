#list comprehension

#using normal for loop - inelegant
nums = [4, -11, 69, 53, -65]
doubled = []

for num in nums:
    doubled.append(num * 2)

print(doubled)

#using list comprehension - elegant
nums = [4, -11, 69, 53, -65]
doubled = [num * 2 for num in nums]
print(doubled)

#general expression of list comprehension
#new_list = [<expression> for <element> in <collection>]

#arbitrary keyword arguments **kwargs
#if keyword arguments to be passed in the function are unknown, add ** before the parameter name
def add_ages(**ages):
    sum = 0
    for k, v in ages.items(): #ages.items() returns a view object with a list of a given dictionary's   (key, value) tuple pairs. This allows us to iterate over the key-value pairs in the dictionary
    #for k, v in ages.items() is a for loop tha iterates over each key-value pair in the dictionary ages
    #ducring each iteration, k represents the key and v the value
        sum += v
    return sum
print('total: ', add_ages(mutemi = 23, kim = 22, kerry = 21))
