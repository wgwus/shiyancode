from flask import Flask, render_template,abort,redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.orm import relationship

   
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/shiyan'
db = SQLAlchemy(app)
                   
class File(db.Model):
    __tablename__='file'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80),unique=True)
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    category = db.relationship('Category',uselist=False)
    content = db.Column(db.Text)
    def __init__(self,title,created_time,category,content):
        self.title = title
        self.created_time = created_time
        self.category = category
        self.content = content

class Category(db.Model):
    __tablename__='category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    file = db.relationship('File')
    def __init__(self,name):
        self.name = name

class insert_db():
    db.create_all()
    java = Category('Java')
    python = Category('Python')
    file1 = File('Hello Java', datetime.utcnow(), java, 'File Content - Java is cool!')
    file2 = File('Hello Python', datetime.utcnow(), python, 'File Content - Python is cool!')
    db.session.add(java)
    db.session.add(python)
    db.session.add(file1)
    db.session.add(file2)
    db.session.commit()


get_data = File.query.all()

@app.errorhandler(404)
def not_fond(error):
    return render_template('404.html'),404

@app.route("/files/<int:file_id>")
def files (file_id):
    d = File.query.filter_by(id=file_id).first()
    if d:
        d2 = d  

    else:
        return not_fond(404)

    return render_template('file.html',d=d2)
    

@app.route("/")
def index():
    #c = File.query.all()
    return (render_template('index.html',d1=get_data)) 

if __name__=="__main__":
    app.run()
