#deleting attribute
>>> std = Person('Mutemi', 65)

>>> del std.name # deleting attribute

>>> std.name #throws AttributeError: 'Person' object has no attribute 'name'

#deleting object
>>> del std  # deleting object

>>> std.name  #throws NameError: name 'std' is not defined

#deleting class
>>> del Person  # deleting class

>>> std = Person('Mutemi', 65) #throws NameError: name 'Person' is not defined


