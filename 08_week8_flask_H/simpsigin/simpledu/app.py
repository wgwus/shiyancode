
from simpledu.config import configs
from simpledu.models import db,Course,User
from flask_migrate import Migrate
from flask import Flask, render_template
from flask_login import LoginManager

'''
app.config.update(dict(
    SECRET_KEY = 'very secret key',
    SQLALCHEMY_DATABASE_URI='mysql+mysqldb://root@localhost:3306/simpledu?charset=utf8'))
'''
def register_extensions(app):
    db.init_app(app)
    Migrate(app,db)
    login_manager=LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def user_loader(id):
        return User.query.get(id)
    
    login_manager.login_view='front.login'

def register_blueprints(app):
    from .handlers import front,course,admin,user
    app.register_blueprint(front)
    app.register_blueprint(course)
    app.register_blueprint(admin)
    app.register_blueprint(user)


def create_app(config):
    app=Flask(__name__)
    app.config.from_object(configs.get(config))
    db.init_app(app)
    Migrate(app,db)
    register_extensions(app)

    register_blueprints(app)
    return app

'''
    @app.route('/')
    def index():
        courses = Course.query.all()
        return render_template('index.html', courses=courses)


    @app.route('/admin')
    def admin_index():
        return 'admin'
'''
