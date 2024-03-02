#while loop
count = 0
while count <= 2:
    print(count)
    count += 1
    print(' ')

#break - terminates loop once specific condition is met
colors = ['blue', 'green', 'white', 'yellow', 'brown', 'cream']
my_color = 'brown'

length = len(colors) #checks how many times we need to iterate based on collection size
i = 0 #to compare against length

while i < length:
    print(colors[i])

    if colors[i] == my_color:
        print('i got what i wanted')
        break
    i += 1
