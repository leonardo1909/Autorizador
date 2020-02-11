from flask import Flask
from ext import configuration, database

import blueprints

app = Flask(__name__)
configuration.init_app(app)
database.init_app(app)

blueprints.init_app(app)
# app.config["MONGO_URI"] = "mongodb://localhost:27017/Autenticador"
