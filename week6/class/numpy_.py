'''numpy is a numerical computing library for working with arrays and matrices'''

#create numpy array

import numpy as np

a = np.array([1, 2, 3])
print(a)

#creating a 2D numpy array
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)

#using numpy to perfomr math operations on arrays
a = np.array([1 ,2, 3])
b = np.array([4, 5, 6])

print(a + b) #addition
print(a - b) #subtraction
print(a * b) #multiplication
print(a / b) #division

#slicing and indexing numpy arrays
a = np.array([1, 2, 3, 4, 5])

print(a[0]) #indexing
print(a[-1])

print(a[1:4]) #slicing

#reshaping numpy arrays
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

b = a.reshape((3, 3))
print(b)