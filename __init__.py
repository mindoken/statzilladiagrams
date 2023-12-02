from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from database import db_create as db
# from flask_restx import Api


def create_app():
    app_1 = Flask(__name__)
    app_1.config['SECRET_KEY'] = ''
    app_1.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    return app_1
    # app.before_request(self._load_user)


"""api = Api(
    app,
    version='1.0',
    title='Диаграммы',
    description='<I>Диаграммы</I>',
    contact='Мельников Владислав',
    contact_url='https://vk.com/mindoken89',

)"""


def wewe(app_1):
    from auth import auth_1
    app_1.register_blueprint(auth_1)

    from main import main_1
    app_1.register_blueprint(main_1)


app = create_app()
database = db(app)
wewe(app)
app.run(debug=True)
