# # Import `numpy` as `np`
import numpy as np
#
# # Make the array `my_array`
# my_array = np.array([[1,2,3,4], [5,6,7,8]], dtype=np.int64)
#
# # Print `my_array`
# print (my_array)
# Create an array of ones
print(np.ones((3,4)))

# Create an array of zeros
print(np.zeros((2,3,4),dtype=np.int16))

# Create an array with random values
print(np.random.random((2,2)))

# Create an empty array
print(np.empty((3,2)))

# Create a full array
print(np.full((2,2),7))

# Create an array of evenly-spaced values
print(np.arange(10,25,5))

# Create an array of evenly-spaced values
print(np.linspace(0,2,9))
