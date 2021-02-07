from __future__ import absolute_import
from sys import path
import imageio

path.append( '.' )
from os import system
import platform

import post_vtk

def run(filename:str, resultformat:str):
    # pass
    system("python simple.py "+filename+" --format "+resultformat)
    post_vtk.run()
    if platform.system()=="Windows":
        system("copy output\\3dcell* static\\")
    else:
        system("cp output/3dcell* static/")
def post(dims:int):
    if dims==3:
        # pass
        system("python postproc.py output/3dcell.vtk  -o static/result3d.png -n --wireframe")
    elif dims==2:
        system("python postproc.py output/2dcell.vtk  -o static/result2d.png -n --wireframe")
    else:
        system("python postproc.py output/1dtest.vtk  -o static/result1d.png -n --wireframe")
    # for i in range(10):
    #     system(f"python postproc.py output/sofc2d_mesh.0{i}.vtk  -o output/result.0{i}.png -n --wireframe")
def mov():
    frames = []
    for i in range(10):
        frames.append(imageio.imread(f"output/result.0{i}.png"))
    imageio.mimsave("static/result.gif", frames, 'GIF', duration=0.5)
    # system("ffmpeg - r 10 - sameq - i output/result. % *.png output/result.mov")
    system("ffmpeg -y -r 2 -f image2 -i output/result.%2d.png -vcodec libx264 output/result.mp4")

def setParams(filename:str, result:dict):
    data = ''
    encode='utf-8'
    if platform.system()=="Windows":
        encode='gbk'
    with open(filename, 'r+', encoding=encode) as f:
        for line in f.readlines():
            if (line.find("V_cell = ")>=0):
                print(line)
                line ="V_cell = "+ str(result["电池电压"])+'    # [V]Cell voltage\n'
                print(line)
            if (line.find("T = ")>=0):
                print(line)
                line ="T = "+ str(result["温度"])+'  # "[K]Temperature"\n'
                print(line)
            if (line.find("k_c = ")>=0):
                print(line)
                line ="k_c = "+ str(result["连接体热导率"])+'\n'
                print(line)
            if (line.find("k_s = ") >= 0):
                print(line)
                line = "k_s = " + str(result["电极热导率"]) + '\n'
                print(line)
            if (line.find("k_l = ") >= 0):
                print(line)
                line = "k_l = " + str(result["电解质热导率"]) + '\n'
                print(line)
            if (line.find("xH2 = ") >= 0):
                print(line)
                line = "xH2 = " + str(result["氢气摩尔分数"]) + '\n'
                print(line)
            if (line.find("pfuel = ") >= 0):
                print(line)
                line = "pfuel = " + str(result["燃料气入口压力"]) + '\n'
                print(line)
            if (line.find("xO2 = ") >= 0):
                print(line)
                line = "xO2 = " + str(result["氧气摩尔分数"]) + '\n'
                print(line)
            if (line.find("pair = ") >= 0):
                print(line)
                line = "pair = " + str(result["空气入口压力"]) + '\n'
                print(line)
            if (line.find("kappa_c = ") >= 0):
                print(line)
                line = "kappa_c = " + str(result["连接体电导率"]) + '\n'
                print(line)
            if (line.find("kappa_s = ") >= 0):
                print(line)
                line = "kappa_s = " + str(result["电子电导率"]) + '\n'
                print(line)
            if (line.find("kappa_m = ") >= 0):
                print(line)
                line = "kappa_m = " + str(result["离子电导率"]) + '\n'
                print(line)
            data += line
    with open(filename, 'r+') as f:
        f.writelines(data)
    f.close()


def setTransient(filename:str,transient:bool):
    data = ''
    with open(filename, 'r+') as f:
        for line in f.readlines():
            if (line.find("ts.simple") >= 0):
                print(line)
                if transient:
                    line ="    'ts': ('ts.simple', {'t0': t0, 't1': t1, 'dt': None, 'n_step': n_step, 'verbose': 1, }),\n"
                else:
                    line = "    # 'ts': ('ts.simple', {'t0': t0, 't1': t1, 'dt': None, 'n_step': n_step, 'verbose': 1, }),\n"
                print(line)
            data += line
        with open(filename, 'r+') as f:
            f.writelines(data)
        f.close()
