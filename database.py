from flask_sqlalchemy import SQLAlchemy


def db_create(app):
    db = SQLAlchemy(app)
    with app.app_context():
        db.create_all()
    return db
