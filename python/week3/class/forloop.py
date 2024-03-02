#while and for loop

#for loop

names = ['paul', 'john', 'rich', 'saruni']

for name in names:
    print(f'my name is {name}.')


name = 'mutemi'

for char in name:
    print(char)

#range - gives series of values btn two numeric intervals
welcome_msg = 'welcome to kenya.'

for i in range(5):
    print(welcome_msg)
    print(' ')


num = 12345678
num_cast = str(num)

for char in (num_cast):
    print(char)
    print(' ')

for i in range(1,10, 2):
    print(i)

#break - terminates loop once specific condition is met
colors = ['blue', 'green', 'white', 'yellow', 'brown', 'cream']
my_color = 'brown'

for color in colors:
    if color == my_color:
        print('i got what i wanted')
        break
    print(color)

print(' ')

#continue - skips current iteration of loop and control flow proceeds to next iteration
ages = [13, 24, 17, 36]

for age in ages:
    if age < 21:
        continue
    print(age)

print(' ')

#nested loops
#used to access items of lists inside other lists
    #items selected in outer loop is used as list for inner loop
groups = [['paul', 'john'], ['terry', 'kerry']]
for group in groups: #this loop iterates over the two lists
    for name in group: #this loop iterates over each name in each sub-list
        print(name)
