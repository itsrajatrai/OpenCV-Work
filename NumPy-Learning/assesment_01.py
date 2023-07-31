# This assessment tests the understanding of NumPy library's array creation, manipulation, sorting, and concatenation functionalities at beginner, intermediate, and advanced levels.


import numpy as np

# Beginner Level:

"""
You are given a positive integer 'n'. Create a NumPy array of size 'n' containing all zeros.
"""
n=4
arr=np.zeros(n)
print(arr)

"""
You are given a positive integer 'n'. Create a NumPy array of size 'n' containing all ones.

"""
arr2=np.ones(n)
print(arr2)

# Intermediate Level:

"""
You are given an integer 'start', 'stop', and 'step'. Create a NumPy array with elements starting from 'start', ending at 'stop' (exclusive), with a step size of 'step'.

"""

start=4
stop=8
step=2

arr3=np.arange(start,stop,step)
print(arr3)


"""
You are given a float 'start', 'stop', and 'num'. Create a NumPy array with 'num' evenly spaced elements from 'start' to 'stop' (inclusive).

"""

start=4.2
stop=9.2
num=2

arr4=np.linspace(start,stop,num)
print(arr4)

# Advanced Level:

"""
You are given a NumPy array of integers. Sort the array in ascending order. 

"""

sample_arr=np.array([78,96,54,12,36,5])
sorted_arr=np.sort(sample_arr)

print(sorted_arr)


"""
You are given two NumPy arrays of the same shape. Concatenate them horizontally (column-wise).

"""

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.concatenate((a, b)))   # WRONG



# Answers

"""
Certainly! Here are the answers to the assessment questions:

**Beginner Level:**

1. You are given a positive integer 'n'. Create a NumPy array of size 'n' containing all zeros.

```python
import numpy as np

n = 5
zeros_array = np.zeros(n)
```

2. You are given a positive integer 'n'. Create a NumPy array of size 'n' containing all ones.

```python
import numpy as np

n = 5
ones_array = np.ones(n)
```

**Intermediate Level:**

1. You are given an integer 'start', 'stop', and 'step'. Create a NumPy array with elements starting from 'start', ending at 'stop' (exclusive), with a step size of 'step'.

```python
import numpy as np

start = 0
stop = 10
step = 2
result_array = np.arange(start, stop, step)
```

2. You are given a float 'start', 'stop', and 'num'. Create a NumPy array with 'num' evenly spaced elements from 'start' to 'stop' (inclusive).

```python
import numpy as np

start = 1.0
stop = 10.0
num = 5
result_array = np.linspace(start, stop, num)
```

**Advanced Level:**

1. You are given a NumPy array of integers. Sort the array in ascending order.

```python
import numpy as np

arr = np.array([5, 2, 8, 1, 3])
sorted_array = np.sort(arr)
```

2. You are given two NumPy arrays of the same shape. Concatenate them horizontally (column-wise).

```python
import numpy as np

array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])
concatenated_array = np.concatenate((array1, array2), axis=1)
```


"""