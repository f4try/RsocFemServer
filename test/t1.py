import pyvista
import numpy as np

x,y,z=np.meshgrid(np.linspace(-5,5,20),
                  np.linspace(-5,5,20),
                  np.linspace(-5,5,5))
points = np.empty((x.size,3))
points[:,0]=x.ravel('F')
points[:,1]=y.ravel('F')
points[:,2]=z.ravel('F')

direction = np.sin(points)**3

plobj = pyvista.Plotter()
plobj.add_arrows(points,direction,0.5)
plobj.show(screenshot='vectorfield.png')