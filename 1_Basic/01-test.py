import numpy as np

#creating a 1-D array
array=np.array([1, 2, 3])

#creating a 2-D array
array2=np.array([[1, 2, 3], 
                 [4, 5, 6]])

#creating a 3-D array
array3=np.array([[[1, 2, 3], [4, 5, 6]], 
                 [[7, 8, 9], [10, 11, 12]]])

print("1-D array:")
print(array)
print("2-D array:")
print(array2)
print("3-D array:")
print(array3)   

#indexing of an array
print("Indexing of 1-D array:")
print(array[0]) #prints the first element of the array
print("Indexing of 2-D array:")
print(array2[0,1]) #prints the element at the first row and second column
print("Indexing of 3-D array:")
print(array3[0,1,2]) #prints the element at the first block, second row and third column

#slicing of an array  :   array[start:stop:step]
print("Slicing of 1-D array:")
print(array[0:2]) #prints the first two elements of the array
print("Slicing of 2-D array:")
print(array2[0:2, 1:3]) #prints the elements at the first two rows and second to third columns
print("Slicing of 3-D array:")
print(array3[0:1, 1:3, 2:4]) #prints the elements at the first block, second to third rows and third to fourth columns  
