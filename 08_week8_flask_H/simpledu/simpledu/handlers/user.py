from flask import Blueprint,render_template
from simpledu.models import User,Course

user = Blueprint('user',__name__,url_prefix='/user')

@user.route('/<user>')
def user_index(user):
    #user =User.query.filter_by(name=user).first() 
    users=User.query.filter_by(username=user).first() 
    course = Course.query.all()
    
    i = users
    
   # user=user    
    return render_template('user.html',use=i,course=course)
