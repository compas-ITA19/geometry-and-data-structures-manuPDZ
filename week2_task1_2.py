# Task 1.2: Use cross product to compute the area of a convex, 2D polygon
# Manuel Biedermann

from compas.geometry import Vector
from compas.geometry import Polygon
from compas.geometry import subtract_vectors
from compas.geometry import cross_vectors
from compas.geometry import length_vector

def CalcAreaPolygon(polygon):

    totalArea = 0.0
    n = len(polygon.points)
    for i in range(0, n):        
        v0 = polygon[i]
        v1 = polygon[(i+1)%n]
        v2 = polygon.centroid
        a = subtract_vectors(v2,v1)
        b = subtract_vectors(v2,v0)
        cross_ab = cross_vectors(a,b)
        area = 0.5 * length_vector(cross_ab)
        totalArea+=area

    return totalArea

# Test case
polygon = Polygon([[0,0,0], [1,0,0], [1,1,0], [0,1,0]])

area = CalcAreaPolygon(polygon)
print(area)
