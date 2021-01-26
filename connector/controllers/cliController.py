from flask_restful import Resource
from flask import jsonify
from probes import cliProbe

class cli(Resource):
    def get(self, method):
        if method == 'teste':
            return ("Homenagem ao GUI")
        else:
            return ("Vao olhas os metodos na docuemntacao")

