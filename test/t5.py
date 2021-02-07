import pyvista as pv
mesh = pv.read('../output/3dcell.vtk')
mesh.plot(screenshot='3dcell_T.png')