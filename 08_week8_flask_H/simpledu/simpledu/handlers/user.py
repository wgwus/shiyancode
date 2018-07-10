from flask import Blueprint,render_template,Flask
from simpledu.models import User,Course

user = Blueprint('user',__name__,url_prefix='/user')


@user.errorhandler(404)
def note_found(error):
    return render_template('404.html'),404

@user.route('/<user>')
def user_index(user):
    #user =User.query.filter_by(name=user).first() 
    users=User.query.filter_by(username=user).first() 
    course = Course.query.all()
    if users:
        i = users
    else:
        return note_found(404) 
    
   # user=user    
    return render_template('user.html',use=i,course=course)
