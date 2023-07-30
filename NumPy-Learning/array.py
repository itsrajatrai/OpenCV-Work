import numpy as np

a=np.array([1,2,3,4,5,6]) # A ID array 

print(a) # Output is [1 2 3 4 5 6]

b=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]) # A 2D array

print(b) 
"""  Output is [[ 1  2  3  4  5]
                [ 6  7  8  9 10]
                [11 12 13 14 15]]
""" 

# Accessing the elements
print(a[2])
print(b[2][2])

# This section covers np.zeros(), np.ones(), np.empty(), np.arange(), np.linspace(), dtype

z=np.zeros(4)
print(z) # [0. 0. 0. 0.]

o=np.ones(4)
print(o) # [1. 1. 1. 1.]

e=np.empty(8)
print(e)  # [0.00000000e+000 0.00000000e+000 0.00000000e+000 0.00000000e+000 0.00000000e+000 1.60077269e-321 8.01097888e-307 2.56761491e-312]  - > Random

ar=np.arange(4)
print(ar) # [0 1 2 3]

ar1=np.arange(4,8,2)
print(ar1) # [4 6]  last limit is not included

l=np.linspace(0, 10, num=5)
print(l) # [ 0.   2.5  5.   7.5 10. ]

x = np.ones(2, dtype=np.int64)
print(x) #[1 1]



