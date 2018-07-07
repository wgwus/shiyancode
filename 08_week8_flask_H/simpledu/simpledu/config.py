



class BaseConfig(object):
    SECRET_KEY = 'makesure to set a ver secret key'

class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_TEARDOWN = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root@localhost:3306/simpledu?charset=utf8'



class ProductionConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    pass



configs = {
        'development': DevelopmentConfig,
        'procuction':ProductionConfig,
        'testing':TestingConfig}

