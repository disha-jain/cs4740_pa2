import os
import subprocess
from flask import Flask, render_template, request
from werkzeug import secure_filename
app = Flask(__name__)

@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      s,n = grade()
      return render_template('uploader.html', score=s, submission =n)

def grade():
    subprocess.call("rm -f ./a.out", shell=True)
    retcode = subprocess.call("./test.sh", shell=True)
    s = "Score: " + str(retcode) + " out of 2 correct.\n"
    print ("Score: " + str(retcode) + " out of 2 correct.")
    # s= s+ "*************Original submission************* \n"
    n = ""
    with open('add.go','r') as fs:
        n = n+ fs.read()
    return s,n

if __name__ == '__main__':
    app.run(host="0.0.0.0")
