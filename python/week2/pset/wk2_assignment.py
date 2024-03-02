#week2 assignment

#create empty list
my_list = [] 

#append elements 10, 20, 30, 40 to my_list
list_a = [10, 20, 30, 40]

for i in list_a:
    my_list.append(i)
    
print('appended list: ', my_list)

#insert value 15 at second position in list
my_list.insert(1, 15)

print('inserted list: ', my_list)

#extend list with another list [50, 60, 70]
list_b = [50, 60, 70]
my_list.extend(list_b)

print('extended list: ', my_list)

#remove last element from list
del my_list[-1]

print('deleted list: ', my_list)

#sort list in ascending order
my_list.sort()

print('ascending list: ', my_list)

#find and print index of value 30 in list
x = my_list.index(30)

print(x)