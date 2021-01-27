from connector import app, api
from flask_restful import Api, Resource
from connector.controllers import networkController
from connector.controllers import cliController
from connector.controllers import guiController

class home(Resource):
    def get(self):
        return {"api" : {
            "connectividade" : "http://localhost:5000/api/v1/network/getUrlGuiDefault",
            "ssh": "http://localhost:5000/api/v1/ssh",
        }}
api.add_resource(home, "/")


api.add_resource(networkController.network, "/api/v1/network/<string:method>/<string:ip>")

api.add_resource(cliController.cli, "/api/v1/cli/<string:method>")

api.add_resource(guiController.gui, "/api/v1/gui/<string:method>")