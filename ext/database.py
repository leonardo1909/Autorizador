from flask_pymongo import PyMongo

mongo = PyMongo()


def init_app(app):
    global mongo
    mongo = PyMongo(app)


def get_mongo():
    return mongo
