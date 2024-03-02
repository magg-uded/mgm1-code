#a) using for loop

#create two empty sets
animals = set()
countries = set()

#ask user for input and populate each set respectively
for i in range(5):
    animals.add(input('add your favorite animal: '))
    countries.add(input('add your favorite country: '))
    
print('first set has: ', animals)
print('second set has: ', countries)

z = animals.intersection(countries)
print('both sets share: ', z)

# b)using set comprehension
animals = {input('add your favorite animal: ') for _ in range(5)}
print(animals)

countries = {input('add your favorite country: ') for _ in range(5)}
print(countries)

z = animals.intersection(countries)
print('both sets share: ', z)