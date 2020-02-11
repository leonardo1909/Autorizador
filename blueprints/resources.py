from flask import jsonify, request
from flask_restful import Resource

from ext import database


class UsuarioResource(Resource):
    """
        Resource(View) de usuários.
    """

    def get(self):
        # usuarios = mongo.db.usuarios.find()
        usuarios = database.get_mongo().db.usuarios.find()
        response = []
        for usuario in usuarios:
            usuario['_id'] = str(usuario['_id'])
            response.append(usuario)
        return (jsonify(response), 200)

    def post(self):
        dados = request.get_json()
        # mongo.db.usuarios.insert_one(dados)
        # dados['_id'] = str(dados['_id'])

        return (jsonify(dados), 201)
