import pyvista as pv

def run(filename='static/3dcell.vtk',output='static/',tick='0'):
    mesh = pv.read(filename)
    cpos = [(0.002899468879017831, 0.0017512736510668626, 0.014440441901019573), (-0.004155028698913291, -0.00329445397240560, -0.0031100280101235373), (-0.016391356798300616, 0.9626709824493171, -0.2701775397259686)]

    plotter = pv.Plotter(off_screen=True)
    plotter.add_mesh(mesh,color='tan',show_edges=True)
    plotter.show(cpos=cpos,screenshot=output+'3dcell_mesh_'+tick+'.png')

    plotter = pv.Plotter(off_screen=True)
    plotter.add_mesh(mesh,scalars='phil',cmap='jet')
    plotter.show(cpos=cpos,screenshot=output+'3dcell_phil_'+tick+'.png')

    plotter = pv.Plotter(off_screen=True)
    plotter.add_mesh(mesh,scalars='phis1',cmap='jet')
    plotter.show(cpos=cpos,screenshot=output+'3dcell_phis1_'+tick+'.png')

    plotter = pv.Plotter(off_screen=True)
    plotter.add_mesh(mesh,scalars='phis3',cmap='jet')
    plotter.show(cpos=cpos,screenshot=output+'3dcell_phis3_'+tick+'.png')

    plotter = pv.Plotter(off_screen=True)
    plotter.add_mesh(mesh,scalars='T',cmap='jet')
    plotter.show(cpos=cpos,screenshot=output+'3dcell_T_'+tick+'.png')

    plotter = pv.Plotter(off_screen=True)
    plotter.add_mesh(mesh,scalars='c_h2a',cmap='jet')
    plotter.show(cpos=cpos,screenshot=output+'3dcell_c_h2a_'+tick+'.png')

    plotter = pv.Plotter(off_screen=True)
    plotter.add_mesh(mesh,scalars='c_h2oa',cmap='jet')
    plotter.show(cpos=cpos,screenshot=output+'3dcell_c_h2oa_'+tick+'.png')

    plotter = pv.Plotter(off_screen=True)
    plotter.add_mesh(mesh,scalars='c_n2c',cmap='jet')
    plotter.show(cpos=cpos,screenshot=output+'3dcell_c_n2c_'+tick+'.png')

    plotter = pv.Plotter(off_screen=True)
    plotter.add_mesh(mesh,scalars='c_o2c',cmap='jet')
    plotter.show(cpos=cpos,screenshot=output+'3dcell_c_o2c_'+tick+'.png')

    plotter = pv.Plotter(off_screen=True)
    plotter.add_mesh(mesh,scalars='p1',cmap='jet')
    plotter.show(cpos=cpos,screenshot=output+'3dcell_p1_'+tick+'.png')

    plotter = pv.Plotter(off_screen=True)
    plotter.add_mesh(mesh,scalars='p2',cmap='jet')
    plotter.show(cpos=cpos,screenshot=output+'3dcell_p2_'+tick+'.png')

