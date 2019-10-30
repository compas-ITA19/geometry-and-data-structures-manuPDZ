# Task 1.1: Create a set of three orthonormal vectors
# Manuel Biedermann

from compas.geometry import Vector

def CalcOrthonormalVectors(a,b):
    c = a.cross(b)
    b = c.cross(a)

    a.unitize()
    b.unitize()
    c.unitize()

    return [a,b,c]

# Test case
a = Vector(-1.0, 0.0, 0.0)
b = Vector(-1.0, 1.0, 0.0)

v1 = CalcOrthonormalVectors(a,b)

print(v1[0])
print(v1[1])
print(v1[2])
print( v1[0].length )
print( v1[1].length )
print( v1[2].length )