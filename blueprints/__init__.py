from flask import Blueprint
from flask_restful import Api

from .resources import UsuarioResource

bp = Blueprint("usuarios", __name__, url_prefix='')
api = Api(bp)
api.add_resource(UsuarioResource, "/")


def init_app(app):
    app.register_blueprint(bp)
