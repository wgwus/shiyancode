#feng zhuang wtform add token csrf valid
from flask_wtf import FlaskForm

from wtforms import StringField,PasswordField,SubmitField,BooleanField
# form valid fun
from wtforms.validators import Length,Email,EqualTo,Required

from simpledu.models import db,User
#raise error fun
from wtforms import ValidationError


class RegisterForm(FlaskForm):
    def create_user(self):
        user=User()
        user.username = self.username.data
        user.email = self.email.data
        user.password=self.password.data
        db.session.add(user)
        db.session.commit()
        return user
    username=StringField('user',validators=[Required(),Length(3,24)])
    email = StringField('email',validators=[Required(),Email()])
    password = StringField('passwd',validators=[Required(),Length(6,24)])
    
    repeat_password = PasswordField('reptpasswd',validators=[Required(),EqualTo("password")])
    submit = SubmitField('enter')


    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('username exist')
    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('email exist')




class LoginForm(FlaskForm):
    def validate_email(self,field):
        if field.data and not User.query.filter_by(email=field.data).first():
            raise ValidationError('emain not zhuce')
    def validate_password(self,field):
        user = User.query.filter_by(email=self.email.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('passwdwrond')
        
    email = StringField('email',validators=[Required(),Email()])
    password = PasswordField('passwd',validators=[Required(),Length(6,24)])
    remember_me = BooleanField('remberme')
    submit=SubmitField('enter')
