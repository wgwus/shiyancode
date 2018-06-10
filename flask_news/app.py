import json
from flask import Flask, render_template,abort,redirect, url_for
import os

app = Flask(__name__)

@app.errorhandler(404)
def not_fond(error):
    return render_template('404.html'),404


@app.route("/files/<filename>")
def json_rea (filename):
# /home/shiyanlou/files/helloworld.json
    path = '/home/shiyanlou/files'
    os.chdir(path)
    filename_has_json = filename+'.json'
    
    if filename in os.listdir(path):
        with open (filename)as f:
            d = json.load(f)
    elif filename_has_json in os.listdir(path):
        with open (filename_has_json) as f:
            d = json.load(f)
    else:
        d = not_fond(404)
    return render_template('file.html',d=d)
    

@app.route("/")
def index():
    path1 = ''
    path = '/home/shiyanlou/files'
    c =[]
    for filename in os.listdir(path):
        os.chdir(path)
        
        with open (filename)as f:
            d = json.load(f)
            c.append(d['title'])
    return (render_template('index.html',d1=c)) 

if __name__=="__main__":
    app.run()
