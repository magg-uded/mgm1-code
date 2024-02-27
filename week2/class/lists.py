#lists#

#list of 3 numbers
numbers = [1, 2, 3]
print(numbers)

#empty list
my_list =[]

#list with mixed data types
my_list = [1, "Hello", 3.4] #int, str, float

##accessing items in a list

#using positive index
languages = ["Python", "swift", "C++"]
print(languages[0]) #Python
print(languages[0][2]) #Third letter in Python

#using negative index
languages = ["Python", "swift", "C++"]
print(languages[-1]) #C++
print(languages[-1][-3]) #Third letter in reverse in C++

##slicing - access a section of items in a list

my_list = ['p','r','o','g','r','a','m','i']
#items from index 2dn to 4th index
print(my_list[2:5]) #['o','g','r']
#items from 5th index to end
print(my_list[5:])
#items from start to end
print(my_list[:])
#items from beginning to 4th index
print(my_list[:5])

##manipulating lists using methods - since lists are mutable

#using append() - add one item at end of list
numbers = [21, 33, 54, 32]
print("Before append: ", numbers) #before appending
numbers.append(32) #append
print("After append: ", numbers) #after appending

#extend() - add all items of a list to another
prime_numbers = [2,3,5]
print("List1: ", prime_numbers)
even_numbers = [2,4,6]
print("List2: ", even_numbers)
prime_numbers.extend(even_numbers) #join List2 to List1
print("List after extend: ", prime_numbers)

#replacing items
languages = ["Python", "swift", "C++"]
languages[2] = "Java"
print(languages) #replace C++ with Java

#del - deletes item at specified position
languages = ["Python", "swift", "C++", "c", "Kotlin", "Dart", "JS", "Django"]

del languages[1]
print(languages) #removes Swift

del languages[-1]
print(languages) #now removes Django at end note it's sequential operation

del languages[0:2]
print(languages) #now removes from Python to Kotlin

#remove() - removes first item with specified value
languages = ["Python", "swift", "C++", "c", "Kotlin", "Dart", "JS", "Django"]

languages.remove("Python")
print(languages)

#insert() - adds element at specified position
languages = ["Python", [4, 5, 6.77], "swift", "C++", "c", "Kotlin", "Dart", "JS", "Django"]
languages.insert(0, 0) #Insert 0 at the first index
print(languages)

languages = ["Python", [4, 5, 6.77], "swift", "C++", "c", "Kotlin", "Dart", "JS", "Django"]
languages.insert(len(languages), True) #Inserting boolean at end
print(languages)

#pop()- removes item at specified position
fruits = ["Apple", "Orange", "Lemon"]
fruits.pop(0) #removes Apple
print(fruits)

#clear() - removes all items from list
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()
print(fruits)

#index() - Returns the index of the first element with the specified value
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)

#reverse() - reverses the order of the list
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)

#sort() - sorts the list
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)

#copy() - make a copy of a list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

##iterating through a list
languages = ["Python", "swift", "C++", "c", "Kotlin", "Dart", "JS", "Django"]

for language in languages:
    print(language)
    
##check if item exists in list
languages = ["Python", "swift", "C++", "c", "Kotlin", "Dart", "JS", "Django"]
print("c" in languages) #True
print("C" in languages) #False

##list size
languages = ["Python", "swift", "C++", "c", "Kotlin", "Dart", "JS", "Django"]
print("Total elements: ", len(languages))

##list comprehension - elegant way of creating lists

#making a list with each item increasing by power of 2
numbers = [number*number for number in range(0,7)]
print(numbers)

numbers = [] #Create an empty list
for x in range(1,7):
    numbers.append(x*x) #Append numbers to empty list using operation 
    print(numbers) #Is similar to above
    

