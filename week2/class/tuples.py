#tuples#
    #similar to a list only that a tuple is immutable and
    #created by placing elements inside ()

#empty tuple
my_tuple =()
print(my_tuple)

#nested tuple
my_tuple = ("mouse", [3,4,5],True,(1,2,3))
print(my_tuple)

#tuple with one element
my_tuple1 = ("Hello")
print(type(my_tuple1))

my_tuple2= ("Hello",)
print(type(my_tuple2))

#indexing
letters = ('p','r','o','g','r','a','m','i')

print(letters[:5])
print(letters[2:])
print(letters[-1])

#slicing
letters = ('p','r','o','g','r','a','m','i',4,False)

print(letters[1:4])
print(letters[:-7]) #beginning to 2nd index
print(letters[7:])

##methods - python tuple only has 2 methods
    #does not have methods to add or remove items
letters = ('p','r','o','g','r','a','m','i',4,'o',False)

print(letters.count('o'))
print(letters.index('g'))

##iterating through tuples
cars = ['Ford', 'BMW', 'Volvo']

for car in cars:
    print(car)
    
##check if an item exists in a tuple
cars = ['Ford', 'BMW', 'Volvo']

print('Ford' in cars) #true
print('ford' in cars) #false 
