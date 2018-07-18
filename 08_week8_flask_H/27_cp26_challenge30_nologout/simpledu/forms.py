#feng zhuang wtform add token csrf valid
from flask_wtf import FlaskForm

from wtforms import StringField,PasswordField,SubmitField,BooleanField
# form valid fun
from wtforms.validators import Length,Email,EqualTo,Required

from simpledu.models import db,User
#raise error fun
from wtforms import ValidationError
import re
from flask import flash
class RegisterForm(FlaskForm):

    username=StringField('user',validators=[Required(),Length(3,24)])
    email = StringField('email',validators=[Required(),Email()])
    password = StringField('passwd',validators=[Required(),Length(6,24)])
    repeat_password = PasswordField('reptpasswd',validators=[Required(),EqualTo("password")])
    submit = SubmitField('enter')
    def create_user(self):
        user=User()
        user.username = self.username.data
        user.email = self.email.data
        user.password=self.password.data
        db.session.add(user)
        db.session.commit()
        return user


    def validate_username(self,field):
     

        if User.query.filter_by(username=field.data).first():

            raise ValidationError('username exist')
        elif not (re.search(r'(\w)+|(\d)+',field.data).group()==field.data):
            flash('username false ,only words and num')
            raise ValidationError()

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('email exist')




class LoginForm(FlaskForm):
    username=StringField('username',validators=[Required(),Length(3,24)])
        
#    email = StringField('email',validators=[Required(),Email()])
    password = PasswordField('passwd',validators=[Required(),Length(6,24)])
    remember_me = BooleanField('remberme')
    submit=SubmitField('enter')
    def validate_email(self,field):
        if field.data and not User.query.filter_by(username=field.data).first():
            raise ValidationError('email not zhuce')
    def validate_password(self,field):
        user = User.query.filter_by(username=self.username.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('passwdwrond')

