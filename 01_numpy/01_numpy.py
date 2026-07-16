# numpy 
import numpy as np 

# creating numpy array using python list
lst = [1,2,3,4,5]
print(type(lst))
print(lst)
arr = np.array(lst)
print(type(arr))
print(arr)

# using numpy array instead of python list because it is less time taking and more memory efficient then list also it provides us (vectorization) and (broadcasting) that help us not to use loops, list comprehension, map or filter over list that takes more time and memory

# we can also create 1D, 2D, 3D and more dimentions of numpy array

oned = np.array([1,2,3,4,5])
print(oned)
print(oned.shape)

twod = np.array([[1,2,3],
			    [4,5,6]])
print(twod)
print(twod.shape)

threed = np.array(
	[[[10,20,30,40],
	  [11,21,31,41],
	  [12,22,32,42]],

	 [[50,60,70,80], 
	  [51,61,71,81],
	  [52,62,72,82]]])
print(threed)
print(threed.shape)

# *shape is a property of numpy that returns a tuple which contains the dimentions of the array 
# 1D - (columns,)
# 2D - (rows, columns)
# 3D - (depth, rows, columns)

# vectorization

lst = [1,2,3,4,5] # python list
arr = np.array(lst) # numpy array

# python list (loop-based) 
lst_squares = [i ** 2 for i in lst]
print(lst_squares)
# takes more time and memory (less efficient over large data sets)

# numpy array (vectorization)
np_squares = arr ** 2
print(np_squares)
# takes less time and memory (give fast resutls very efficient over large data sets also easy to apply operations on)

# some useful numpy methods 

# *zeros - this takes a tuple of (depth, rows, columns) and return a array of zeros only of the perticular dimention
zeros = np.zeros((2,3))
print(zeros)

# *ones - this also take tuple as dimentions and return an array of ones only
ones = np.ones((3,2))
print(ones)

# *full - this takes a tuple and a number and return an array of only that number of the perticular dimention
full = np.full((3,3), 8)
print(full)

# *eye - takes a number and return an identity matrix
eye = np.eye(3)
print(eye)
# identity matrix is a square martix in which the principle digonal is of 1s and all other are 0s

# *arange - takes three arguments as numbers (start, stop, step)
arange = np.arange(1,10,2)
print(arange)
# its like range() function in python

# *linspace - this takes three arguments as numbers (start, stop, intervels/spaces) this returns an arrary of evely spaced between start number and stop number
linspace = np.linspace(10, 100, 10)
print(linspace)

# some useful array properties

arr = np.array([[1,2,3,4],
				[5,6,7,8]])

print('Shape:', arr.shape) # tuple of dimentsion mentioned earilar
print('Size:', arr.size) # totle number of elements
print('Dimenstions:', arr.ndim) # dimention - 1,2,3,etc
print('Data Type:', arr.dtype) # type of elements - int, str, etc

# changing data type in numpy array

lst = [1,2,3] # int elements
# explicit typecasting (during the making of array)
arr = np.array(lst, dtype = np.float32)
print(arr, arr.dtype)

# *astype - numpy function used for implicit typecasting
arr_int = arr.astype(np.int32)
print(arr_int, arr_int.dtype)

# reshaping and flatting arrays

arr = np.array([[1,2,3],
				[4,5,6]])
print(arr)
print(arr.shape)

# *reshape - numpy method takes tuple of dimentions as arrgument to reshape an array only if the product of dimention of original array it equal to the reshaped one
reshaped_arr = arr.reshape((3,2))
print(reshaped_arr)
print(reshaped_arr.shape)

# *flatten - numpy method to convert higher dimention to lower dimention 
flatted_arr = arr.flatten() # converts 2D to 1D
print(flatted_arr)
print(flatted_arr.shape)

# idexing and slicing

# in numpy the indexing and slicing of array is almost same as python

lst = [1,2,3,4,5,6,7]
arr = np.array(lst)
print(arr[0])
print(arr[-1])

print(arr[2:6]) # [a:b-1]
print(arr[:5])
print(arr[5:])

print(arr[::2])
print(arr[::-1])

# slicing returns a view of original array not a copy that means changes affect the original array
part = arr[1:5]
part[0] = 999
print(arr) # [  1 999   3   4   5   6   7]
print(part) # [999   3   4   5]

# whereas python list create copies when sliced
part = lst[1:5]
part[0] = 999
print(lst) # [1, 2, 3, 4, 5, 6, 7]
print(part) # [999, 3, 4, 5]

# *copy() - we can use copy if we need an independent copy
part = arr[1:5].copy()
part[0] = 999
print(arr) # [1 2 3 4 5 6 7]
print(part) # [999   3   4   5]

# fancy indexing and boolean masking
arr = np.array([1,2,3,4,5,6])

# *fancy indexing - in this we can give array a list of indices to select the perticular element
idx = [1,5,3]
print(arr[idx]) # [2 6 4]

# *boolean masking - in this we can give array a condition it selects only those elements that satisfies that condition 
mask = arr > 3
print(arr[mask]) # [4 5 6]

# mulitdimensional indexing and axis

arr = np.array([[1,2,3],
				[4,5,6],
				[7,8,9]])

print(arr)

# axis - each dimention in a numpy array is called a axe starting from 0:
# 1D - 1 axis (axis 0)
# 2D - 2 axis (axis 0 = rows, axis 1 = columns)
# 3D - 3 axis (axis 0 = depth, axis 1 = rows, axis 2 = columns)

# axis 0 (rows) - operations move down the columns
# axis 1 (columns) - operatoins move across the rows

sum0 = np.sum(arr, axis = 0)
# sum along rows (down each column)
print(sum0) # columns-wise sum
print('dimentions:', sum0.ndim, ', shape:', sum0.shape)

sum1 = np.sum(arr, axis = 1) 
# sum along columns (across each row)
print(sum1) # row-wise sum
print('dimentions:', sum1.ndim, ', shape:', sum1.shape)

# indexing in multidimensional arrays
print(arr, arr.shape) # first we know the array and its shape

# getting an element
print(arr[1,2]) # row index 1, column index 2 - 6

# getting an 1D array
print(arr[0, ::-1]) # row index 0, entire column at step -1 (reverse)
print(arr[2, 1:3]) # row index 2, column index from 1 to 3

# extracting parts from an array
print(arr[1:, :2]) # extracts last 2 rows and first 2 columns
print(arr[0:2, 1:3]) # Extracts first 2 rows and last 2 columns

# changing data along axis
arr[:, 1] = 0
print(arr)

# so this was for 2D, now lets see for 3D
# we already made any 3D array before at line no: 25
print(threed, threed.shape) # first know the array and its shape

# getting an element
print(threed[1, 0, 2]) # depth index 1, row index 0, column index 2

# getting an 2D array
print(threed[1])
print(threed[1, ::-1]) # reverse the elements of the 2D array i.e 1D arrays
print(threed[1, ::-1, ::-1]) # now also reverse the elements of the 1D arrays
print(threed[1, :, ::-1]) # just only reverse the 1D array elements

# getting an 1D array
print(threed[1,2])
print(threed[1,2, ::2]) # make the elements at step to

# extracing parts 
print(threed[:, 1:3, 2:]) # select a part from all depths, from row index 1 to 2 , and column index from 2 to last

# changing data along axis
# lets say i only want to change 31, 32, 71, 72 into 99, here how i do it
threed[:, 1:3, 2] = 99 # from all depths, from row index 1 to 2, column index 2 is equals to 99
print(threed)

# data types in numpy
# do it later (because no need ig)

# broadcasting in numpy (very important just like vectorization)

# difference btw broadcasting and vectorization
# Vectorization replaces explicit loops with array-wide operations (fast, same-shape arrays); broadcasting is the rule that lets NumPy do those operations on arrays of *different* shapes by automatically stretching the smaller one to match.

# we use this to boost the ificiancy in numerical operations 

arr = np.array([1,2,3,4])
result = arr ** 3 # multiples each elements itself 3 times
print('cubes:', result)

result = arr + 10 # add 10 to each element
print('sums:', result)

arr1 = np.array([1,2,3])
arr2 = np.array([10,20,30])

result = arr1 + arr2 # element-wise addtion
print(result)

result = arr1 * arr2 # element-wise mutiplication 
print(result)

# with 2D array
arr3 = np.array([[1,2,3],
				 [4,5,6]])

result = arr3 + arr1
print(result)

result = arr3 - arr1 # element-wise subtraction
print(result)

# real life scenario of applying broadcasting

# Simulating a dataset (5 samples, 3 features)
data = np.array([[10, 20, 30],
[15, 25, 35],
[20, 30, 40],
[25, 35, 45],
[30, 40, 50]])
# Calculating mean and standard deviation for each feature (column)
mean = data.mean(axis=0)
std = data.std(axis=0)
# Normalizing the data using broadcasting
normalized_data = (data - mean) / std
print(normalized_data)

# 18 important built-in mathematical functions/methods in numpy

# few terms that you might not know:
# correation coefficient - Correlation coefficient tells you how strongly two variables move together — ranges from -1 (perfectly opposite) to +1 (perfectly together), with 0 meaning no relationship.

# percentile - Percentile tells you the value below which a given percentage of the data falls — e.g. the 90th percentile is the value that 90% of the data is below.

# n-th difference - n-th difference means applying `diff` (subtracting each element from the next) repeatedly n times — e.g. `np.diff(arr, n=2)` takes the difference of differences, useful for finding rate of change of rate of change.

# cumulative sum - Cumulative sum gives a running total — each element becomes the sum of itself and all elements before it, e.g. `[1,2,3]` → `[1,3,6]`.

arr = np.array([1,2,3,4,5])
arrr = np.array([6,7,8,9,10]) # this another array only of corrcoef

a = np.mean(arr) # compues the mean/average of an array
print(a)

b = np.std(arr) # computes the standard deviation of an array
print(b)

c = np.var(arr) # comutes the variance of an array
print(c)

d = np.min(arr) # returns the minimum value of an array
print(d)

e = np.max(arr) # returns the maximum value of an array
print(e)

f = np.sum(arr) # computes the sum of all elements of an array
print(f)

g = np.prod(arr) # computes the product of all elements of an array
print(g)

h = np.median(arr) # computes the median of an array
print(h)

i = np.percentile(arr, 50) # for the 50th percentile (median)
print(i)

j = np.argmin(arr) # returns the index of the minimum value of an array
print(j)

k = np.argmax(arr) # retruns the index of the maximum value of an array
print(k)

l = np.corrcoef(arr, arrr) # computes the correation coeficient of an array
print(l)

m = np.unique(arr) # find all the unique element of an array
print(m)

o = np.diff(arr) # computes the n-th difference of an array
print(o)

p = np.cumsum(arr) # computes the cumulative sum of an array
print(p)

q = np.linspace(0, 10, 5) # create an array wit evenly spaced numbers over a specified interevale - in this case 5 numbers from 0 to 10
print(q)

r = np.log(arr) # computes the natural logarithm of an array
print(r)

s = np.exp(arr) # computes the exponential of an array
print(s)

# * expected output of the code *
'''
<class 'list'>
[1, 2, 3, 4, 5]
<class 'numpy.ndarray'>
[1 2 3 4 5]
[1 2 3 4 5]
(5,)
[[1 2 3]
 [4 5 6]]
(2, 3)
[[[10 20 30 40]
  [11 21 31 41]
  [12 22 32 42]]

 [[50 60 70 80]
  [51 61 71 81]
  [52 62 72 82]]]
(2, 3, 4)
[1, 4, 9, 16, 25]
[ 1  4  9 16 25]
[[0. 0. 0.]
 [0. 0. 0.]]
[[1. 1.]
 [1. 1.]
 [1. 1.]]
[[8 8 8]
 [8 8 8]
 [8 8 8]]
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
[1 3 5 7 9]
[ 10.  20.  30.  40.  50.  60.  70.  80.  90. 100.]
Shape: (2, 4)
Size: 8
Dimenstions: 2
Data Type: int64
[1. 2. 3.] float32
[1 2 3] int32
[[1 2 3]
 [4 5 6]]
(2, 3)
[[1 2]
 [3 4]
 [5 6]]
(3, 2)
[1 2 3 4 5 6]
(6,)
1
7
[3 4 5 6]
[1 2 3 4 5]
[6 7]
[1 3 5 7]
[7 6 5 4 3 2 1]
[  1 999   3   4   5   6   7]
[999   3   4   5]
[1, 2, 3, 4, 5, 6, 7]
[999, 3, 4, 5]
[  1 999   3   4   5   6   7]
[999   3   4   5]
[2 6 4]
[4 5 6]
[[1 2 3]
 [4 5 6]
 [7 8 9]]
[12 15 18]
dimentions: 1 , shape: (3,)
[ 6 15 24]
dimentions: 1 , shape: (3,)
[[1 2 3]
 [4 5 6]
 [7 8 9]] (3, 3)
6
[3 2 1]
[8 9]
[[4 5]
 [7 8]]
[[2 3]
 [5 6]]
[[1 0 3]
 [4 0 6]
 [7 0 9]]
[[[10 20 30 40]
  [11 21 31 41]
  [12 22 32 42]]

 [[50 60 70 80]
  [51 61 71 81]
  [52 62 72 82]]] (2, 3, 4)
70
[[50 60 70 80]
 [51 61 71 81]
 [52 62 72 82]]
[[52 62 72 82]
 [51 61 71 81]
 [50 60 70 80]]
[[82 72 62 52]
 [81 71 61 51]
 [80 70 60 50]]
[[80 70 60 50]
 [81 71 61 51]
 [82 72 62 52]]
[52 62 72 82]
[52 72]
[[[31 41]
  [32 42]]

 [[71 81]
  [72 82]]]
[[[10 20 30 40]
  [11 21 99 41]
  [12 22 99 42]]

 [[50 60 70 80]
  [51 61 99 81]
  [52 62 99 82]]]
cubes: [ 1  8 27 64]
sums: [11 12 13 14]
[11 22 33]
[10 40 90]
[[2 4 6]
 [5 7 9]]
[[0 0 0]
 [3 3 3]]
[[-1.41421356 -1.41421356 -1.41421356]
 [-0.70710678 -0.70710678 -0.70710678]
 [ 0.          0.          0.        ]
 [ 0.70710678  0.70710678  0.70710678]
 [ 1.41421356  1.41421356  1.41421356]]
3.0
1.4142135623730951
2.0
1
5
15
120
3.0
3.0
0
4
[[1. 1.]
 [1. 1.]]
[1 2 3 4 5]
[1 1 1 1]
[ 1  3  6 10 15]
[ 0.   2.5  5.   7.5 10. ]
[0.         0.69314718 1.09861229 1.38629436 1.60943791]
[  2.71828183   7.3890561   20.08553692  54.59815003 148.4131591 ]
[Finished in 400ms]
'''