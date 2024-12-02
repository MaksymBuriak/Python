# 1D Numpy in Python

import numpy as np

separation_line = '-------------------------'

# Create a numpy array
a = np.array([0, 1, 2, 3, 4])
print(a)

print(separation_line)

# Print each element
print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])

print(separation_line)

# Checking NumPy Version
print(np.__version__)

print(separation_line)

# Check the type of the array
print(type(a))

print(separation_line)

# Check the type of the values stored in numpy array
print(a.dtype)

print(separation_line)

# Check the type of the values stored in numpy array
b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])
print(type(b))
b.dtype 

print(separation_line)

### Assign value

# Create numpy array
c = np.array([20, 1, 2, 3, 4])
print(c)

print(separation_line)

# Assign the first element to 100
c[0] = 100
print(c)

print(separation_line)

# Assign the 5th element to 0
c[4] = 0
print(c)

print(separation_line)

# Assign the value 20 for the second element in the given array.
a = np.array([10, 2, 30, 40,50])
a[1] = 20

# Slicing the numpy array
d = c[1:4]

# Set the fourth element and fifth element to 300 and 400
c[3:5] = 300, 400

# We can also define the steps in slicing, like this: [start:end:step].
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2])

print(separation_line)

# If we don't pass start its considered 0
print(arr[:4])
print(separation_line)

#If we don't pass end it considers till the length of array.
print(arr[4:])
print(separation_line)

#If we don't pass step its considered 1
print(arr[1:5:])
print(separation_line)

#Print the even elements in the given array.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr[1:8:2])

print(separation_line)


### Assign Value with List

# Create the index list
select = [0, 2, 3, 4]

# Use List to select elements
d = c[select]

# Assign the specified elements to new value
c[select] = 100000



### Other Attributes


# Create a numpy array
a = np.array([0, 1, 2, 3, 4])

# Get the size of numpy array
a.size

# Get the number of dimensions of numpy array
a.ndim

# Get the shape/size of numpy array
a.shape



### Numpy Statistical Functions

# Create a numpy array
a = np.array([1, -1, 1, -1])

# Get the mean of numpy array
mean = a.mean()

# Get the standard deviation of numpy array
standard_deviation=a.std()

# Create a numpy array
b = np.array([-1, 2, 3, 4, 5])

# Get the biggest value in the numpy array
max_b = b.max()

# Get the smallest value in the numpy array
min_b = b.min()


# Find the sum of maximum and minimum value in the given numpy array
c = np.array([-10, 201, 43, 94, 502])

max_c = c.max()
min_c = c.min()
Sum = (max_c +min_c)
print(Sum)

print(separation_line)

## Numpy Array Operations

# Array Addition
u = np.array([1, 0])
v = np.array([0, 1])

# Numpy Array Addition
z = np.add(u, v)

# Plot numpy arrays
import matplotlib.pyplot as plt
Plotvec1(u, z, v)

### Array Multiplication

# Create a numpy arrays
x = np.array([1, 2])
y = np.array([2, 1])

# Numpy Array Multiplication
z = np.multiply(x, y)

### Array Division
a = np.array([10, 20, 30])
b = np.array([2, 10, 5])
c = np.divide(a, b)

### Dot Product
X = np.array([1, 2])
Y = np.array([3, 2])

# Calculate the dot product
np.dot(X, Y)

#Elements of X
print(X[0])
print(X[1])

#Elements of Y
print(Y[0])
print(Y[1])

### Adding Constant to a Numpy Array
u = np.array([1, 2, 3, -1]) 
u + 1

## Mathematical Functions

# The value of pi
np.pi

# Create the numpy array in radians
x = np.array([0, np.pi/2 , np.pi])

# Calculate the sin of each elements
y = np.sin(x)

## Linspace

# Makeup a numpy array within [-2, 2] and 5 elements
np.linspace(-2, 2, num=5)

# Make a numpy array within [-2, 2] and 9 elements
np.linspace(-2, 2, num=9)


# Make a numpy array within [0, 2π] and 100 elements 
x = np.linspace(0, 2*np.pi, num=100)

# Calculate the sine of x list
y = np.sin(x)

# Plot the result
plt.plot(x, y)

### Iterating 1-D Arrays
arr1 = np.array([1, 2, 3])
print(arr1)

print(separation_line)

