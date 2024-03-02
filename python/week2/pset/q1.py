#a) using normal 'for loop'
my_list = [] #create empty list to fill

for i in range(0, 10):
    #get only integers values from user else throw error
    while True:
        try:
            get_list = int(input('give me some numbers: ')) 
            break
        except ValueError:
            print('**please enter integer values only')
    my_list.append(get_list) #append integers to list
    
print(my_list)
    
print(sum(my_list)) #print sum of elements in list
   
#b) using list comprehension
while True:
    try:
        my_list = [int(input('give me some numbers: ')) for _ in range(10)]
        break
    except ValueError:
        print('**please enter integer values only')

print(my_list)
    
print(sum(my_list)) #print sum of elements in list
