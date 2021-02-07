import pyvista as pv

mesh = pv.read('../output/3dcell.vtk')
cpos = [(0.002899468879017831, 0.0017512736510668626, 0.014440441901019573), (-0.004155028698913291, -0.00329445397240560, -0.0031100280101235373), (-0.016391356798300616, 0.9626709824493171, -0.2701775397259686)]

plotter = pv.Plotter(off_screen=True)
plotter.add_mesh(mesh,color='tan',show_edges=True)
plotter.show(cpos=cpos,screenshot='3dcell_mesh.png')

plotter = pv.Plotter(off_screen=True)
plotter.add_mesh(mesh,scalars='phil',cmap='jet')
plotter.show(cpos=cpos,screenshot='3dcell_phil.png')

plotter = pv.Plotter(off_screen=True)
plotter.add_mesh(mesh,scalars='phis1',cmap='jet')
plotter.show(cpos=cpos,screenshot='3dcell_phis1.png')

plotter = pv.Plotter(off_screen=True)
plotter.add_mesh(mesh,scalars='phis3',cmap='jet')
plotter.show(cpos=cpos,screenshot='3dcell_phis3.png')

plotter = pv.Plotter(off_screen=True)
plotter.add_mesh(mesh,scalars='T',cmap='jet')
plotter.show(cpos=cpos,screenshot='3dcell_T.png')

plotter = pv.Plotter(off_screen=True)
plotter.add_mesh(mesh,scalars='c_h2a',cmap='jet')
plotter.show(cpos=cpos,screenshot='3dcell_c_h2a.png')

plotter = pv.Plotter(off_screen=True)
plotter.add_mesh(mesh,scalars='c_h2oa',cmap='jet')
plotter.show(cpos=cpos,screenshot='3dcell_c_h2oa.png')

plotter = pv.Plotter(off_screen=True)
plotter.add_mesh(mesh,scalars='c_n2c',cmap='jet')
plotter.show(cpos=cpos,screenshot='3dcell_c_n2c.png')

plotter = pv.Plotter(off_screen=True)
plotter.add_mesh(mesh,scalars='c_o2c',cmap='jet')
plotter.show(cpos=cpos,screenshot='3dcell_c_o2c.png')

plotter = pv.Plotter(off_screen=True)
plotter.add_mesh(mesh,scalars='p1',cmap='jet')
plotter.show(cpos=cpos,screenshot='3dcell_p1.png')

plotter = pv.Plotter(off_screen=True)
plotter.add_mesh(mesh,scalars='p2',cmap='jet')
plotter.show(cpos=cpos,screenshot='3dcell_p2.png')