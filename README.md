# RsocFemServer
http://sofc.top/ 
## Linux,  MacOS or Win10
1.	安装anaconda https://www.anaconda.com/  
2.	安装git（  https://git-scm.com/downloads） 
3.	打开terminal(Linux,MacOS)或者powershell命令行(Win10)  
4.	添加anaconda国内源https://blog.csdn.net/sinat_28442665/article/details/86658593  
```sh
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge 

conda config --set show_channel_urls yes
```
5.	创建名为rsoc的python3.8环境，输入conda create -n rsoc python=3.8  
6.	输入```conda init```，重启terminal
7.	输入```conda activate rsoc```激活环境  
8.	输入```conda install flask sfepy imageio traits traitsui vtk mayavi pyvista xvfbwrapper dipy fury```, 安装flask, sfepy有限元库及其他环境  
ubuntu服务器中```sudo apt install xvfb``` 
9.	输入```git clone https://gitee.com/zongzh/rsoc-fem-server.git``` ,或者```git clone https://github.com/f4try/RsocFemServer.git ```克隆项目文件夹到用户文档  
10.	输入```cd  rsoc-fem-server```进入项目文件目录，输入```python main.py```  
11.	浏览器打开 http://localhost/, 可以看到项目网站, 
![输入图片说明](https://images.gitee.com/uploads/images/2020/1206/173722_fd076500_5414822.png "屏幕截图.png")
## 文件说明
1.	main.py 文件是flask服务器的主文件，用于渲染html文件和运行sofc_sfepy_data3d.py中的有限元程序（flask官网https://flask.palletsprojects.com/）  
2.	templates文件夹中是网页文件，采用bootstrap4模板（bootstrap4官网https://getbootstrap.com/）  
3.	sofc_sfepy_data3d.py是sfepy有限元程序（sfepy官网http://www.sfepy.org/ , sofc_sfepy_data.py用来读取参数  
## 后处理
采用paraview或者postproc.py程序  
