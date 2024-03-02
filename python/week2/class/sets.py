#Sets#
    #collection of unique data
    #cannot duplicate elements of a set
    #create sets by placing elements inside curly braces {}
    #items can be of different types
    #cannot have mutable elements like lists, sets or dictionaries as elements
    #not ordered

student_id = {111, 112, 113, 115, 116}
print(student_id)

vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print(vowel_letters) #printed not in order

mixed_set = {"Hello", 101, -2.0}
print(mixed_set)

#empty set
empty_set = set()

empty_dictionary = {}
print(type(empty_set))
print(type(empty_dictionary))

#duplicate items in set
numbers = {2,2,4,5,6,6}
print(numbers) #duplicates removed

##methods in sets

#add() - add item to set
numbers = {2,2,4,5,6,6}
numbers.add(4.5)

print("updated set: ", numbers)

#update - update set with other items other than lists, tuples, sets etc collection types
companies = {'Lacoste', 'Gucci'}
tech_companies = {'apple', 'google', 'apple'}
companies.update(tech_companies)

print(companies)

#discard() - to remove element from set
languages = {'swift', 'java', 'python'}
removedValue = languages.discard('java')

print(languages)

#add() - adds element to a set
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

print(fruits)

#clear() - removes all elements from set
fruits = {"apple", "banana", "cherry"}
fruits.clear()

print(fruits)

#copy() - returns a copy of the set
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()

print(x)

#difference() - returns set containing the difference btn two or more sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)

print(z)

#difference_update() - removes items in one set that are also included in another, specified
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)

print(x)

#intersection() - returns a set that is the intersection of two or more sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)

print(z)

#intersection_update() - removes items in one set that are not present in another, specified
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)

print(x)

#isdisjoint() - returns whether two sets intersect or not
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.isdisjoint(y)

print(z) #False since x intersects y on "apple"

#issubset() - returns whether or not another set contains a set or not
x = {'a', 'b', 'c', 'c'}
y = {'f', 'e', 'd', 'c', 'b', 'a'}
z =x.issubset(y)

print(z)

#issuperset() - returns whether set contains another or not
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)

print(z)

#pop() - randomly removes an element from set
fruits = {"apple", "banana", "cherry"}
fruits.pop()

print(fruits)

#remove() - removes specified element
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana") #works similar to discard() method

print(fruits)

#symmetric_difference() - returns set with symmetric diff of two sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y) #returns all other items in both sets except for those present in both

print(z)

#symmetric_difference_update() - remove items present in both sets and inserts those not present in both
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)

print(x)

#union() - returns set with union of sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)

print(z)

#update() - update set with another set or any other iterable
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y)

print(x)