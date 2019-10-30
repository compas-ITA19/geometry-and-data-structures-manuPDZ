# Task 2: Define a function for traversing the mesh from boundary to boundary in a "straight" line
# Please note: I recreated the function based on the solution file to understand how it works.

import compas
from compas.datastructures import Mesh
from compas_plotters import MeshPlotter

mesh = Mesh.from_obj(compas.get('faces.obj'))

def TraverseMesh(mesh, start):
   
    path = [start]
    neighbors = mesh.vertex_neighbors(start)

    index = start
    for n in neighbors:
        if not mesh.is_vertex_on_boundary(n):
            previous = index
            index = n
            break

    while True:
        path.append(index)
        if mesh.is_vertex_on_boundary(index):
            break
        neighbors = mesh.vertex_neighbors(index, ordered=True)
        i = neighbors.index(previous)
        previous = index
        index = neighbors[i + 2]

    return path

# Test

start = 3
path = TraverseMesh(mesh, start)
print(path)

plotter = MeshPlotter(mesh, figsize=(4, 4))
plotter.draw_vertices(
    radius=0.4, text='key', keys=path, facecolor=(100, 100, 0))
plotter.draw_edges()
plotter.draw_faces()
plotter.show()