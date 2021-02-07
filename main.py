#encoding:utf-8
from flask import Flask
from flask import request
from flask import render_template
import sofc_sfepy
import time
# import threading

app = Flask(__name__)
# progress_percent = '0'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fem', methods=['GET', 'POST'])
def fem():
    # global progress_percent
    return render_template('fem.html')

@app.route('/result3d',methods = ['POST', 'GET'])
def result():
#    global progress_percent
   if request.method == 'POST':
      result = request.form
      sofc_sfepy.setParams("params.py",result)
    #   progress_percent="20"
      # if "计算暂态" in result.keys():
      #     sofc_sfepy.setTransient("sofc_sfepy_data3d.py",True)
      # else:
      #     sofc_sfepy.setTransient("sofc_sfepy_data3d.py", False)
      sofc_sfepy.run("sofc_sfepy_data3d.py", result["计算结果格式"])
    #   progress_percent="80"
      tick = str(int(time.time()))
      if result["计算结果格式"]=="vtk":
          sofc_sfepy.post(3,tick)
    #   progress_percent="100"
      return render_template("result3d.html",result=result,tick=tick)

@app.route('/docs')
def doc():
    return render_template('docs.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
#   app.debug = True
   app.run(host="0.0.0.0",port=80, threaded=False)
