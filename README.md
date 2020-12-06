# RsocFemServer
## Win10环境
1.	安装anaconda https://www.anaconda.com/  
2.	安装git（  https://git-scm.com/downloads） 
3.	Win+R 打开运行，输入powershell按回车，打开powershell命令行  
4.	添加anaconda国内源https://blog.csdn.net/sinat_28442665/article/details/86658593  
5.	创建名为rsoc的python3.8环境，输入conda create -n rsoc python=3.8  
6.	输入conda init powershell，重启powershell，输入conda activate rsoc激活环境  
7.	输入conda install flask sfepy , 安装flask, sfepy有限元库  
8.	输入git clone https://gitee.com/zongzh/rsoc-fem-server.git ,克隆项目文件夹到用户文档  
9.	输入cd  rsoc-fem-server进入项目文件目录，输入python main.py  
10.	浏览器打开 http://localhost/，可以看到项目网站  
## 文件说明
1.	main.py 文件是flask服务器的主文件，用于渲染html文件和运行sofc_sfepy_data3d.py中的有限元程序（flask官网https://flask.palletsprojects.com/）  
2.	templates文件夹中是网页文件，采用bootstrap4模板（bootstrap4官网https://getbootstrap.com/）  
3.	sofc_sfepy_data3d.py是sfepy有限元程序（sfepy官网http://www.sfepy.org/）  
## 后处理
采用paraview或者postproc.py程序  
