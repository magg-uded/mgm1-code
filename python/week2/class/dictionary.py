##dictionary#
#store data in key-value pairs

#creating dictionary called capital_cities
    #keys are country names
    #values are capital city names
    #both key and values below are of string type
capital_city = {"Uganda":"Kampala", "Kenya":"Nairobi", "Tanzania":"Dodoma", "Nigeria":"Abuja"}
print(capital_city)

#add elements in dictionary - at the end
capital_city = {"Uganda":"Kampala", "Kenya":"Nairobi", "Tanzania":"Dodoma", "Nigeria":"Abuja"}

capital_city["Japan"] = "Tokyo" #assign value to new key
print("Updated dictionary: ", capital_city)

#delete value in dictionary
capital_city = {"Uganda":"Kampala", "Kenya":"Nairobi", "Tanzania":"Dodoma", "Nigeria":"Abuja"}

del capital_city["Uganda"]
print(capital_city)

student_id = {111: "Eric", 112: "Kyle", 113: "Ken", 114: "LilK"}
del student_id[112]
print(student_id)

#replace value
student_id = {111: "Eric", 112: "Kyle", 113: "Ken", 114: "LilK"}
student_id[111] = "Ed"
print(student_id)

#accessing elements - we use keys to access respective values
student_id = {111: "Eric", 112: "Kyle", 113: "Ken", 114: "LilK"}
print(student_id[114])

#remove whole  dictionary
#student_id = {111: "Eric", 112: "Kyle", 113: "Ken", 114: "LilK"}
#del student_id
#print(student_id) #we get error message becase we have deleted the student_id dictionary so it does not exist

#dictionary membership test - see if key is in dictionary
squares = {1: 1, 3: 9, 4: 16, 5: 25}
print(1 in squares) #True
print(6 not in squares) #True
print(9 in squares) #False since membership tests only for keys not values

#iterating through dictionary
squares = {1: 1, 3: 9, 4: 16, 5: 25}

for i in squares:
    print(squares[i]) #outputs each value of a key

##dictionary methods
    
#clear() - removes all elements from dictionary
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1987
    }
car.clear()
print(car)

#copy - returns a copy of the dictionary
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1987
    }
x = car.copy()
print(x)

#fromkeys() - returns a dictionary with specific keys and values
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x,y) #create a dictionary with 3 keys, all with the value 0
print(thisdict)

#get() - returns the value of the specified key
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1987
    }
x = car.get("model")
print(x)

#items() - returns a list containing a tuple for each key-value pair
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1987
    }

x = car.items()
print(x)

#keys() - returns a list containing the dictionary's keys
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1987
    }

x = car.keys()
print(x)

#values() - returns a list of the values in the dictionary
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1987
    }

x = car.values()
print(x)

#pop() - removes the element with the specified key
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1987
    }

car.pop("model")
print(car)

#popitem() - removes the last inserted key-value pair
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1987
    }

car.popitem() #Attach the method to the object
print(car)

#setdefault() - returns the value of the specified key. If key does not exist, insert key with specified value
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1987
    }

x = car.setdefault("model", "Bronco") #returns Mustang since key-value pair exists
print(x)

#update() - updates the dictionary with the specified key-value pairs
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1987
    }
car.update({"color": "White"})
print(car)

