# Task 1.3: Compute cross products of two arrays of vectors
# Manuel Biedermann

from compas.geometry import Vector
from compas.geometry import cross_vectors
from compas.geometry import Vector
import numpy as np

def CrossProductVectorArray(a, b):
    n = len(a)
    crossproducts = []
    c = [0,0,0]
    for i in range(0, n):
        c = cross_vectors(a[i],b[i])
        crossproducts.append(c)

    return crossproducts

def CrossProductVectorArrayNumpy(a, b):
    crossproducts = np.cross(a,b)
    return crossproducts

# Test cases
a = [[1,0,0], [-1,0,0], [1,1,0], [0,1,0]]
b = [[0,1,0], [0,1,0], [1,0,0], [1,1,0]]
print(a)
print(b)

c1 = CrossProductVectorArray(a,b)
print(c1)

c2 = CrossProductVectorArrayNumpy(a,b)
print(c2)
