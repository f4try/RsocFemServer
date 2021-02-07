from pyvista import examples
mesh = examples.load_ant()
print(mesh)
submesh = mesh.subdivide(3,'linear')
print(submesh)
submesh.plot()