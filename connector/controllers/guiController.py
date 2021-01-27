from flask_restful import Resource
from flask import jsonify
from probes import guiProbe


class gui(Resource):
    def get(self, method):
        if method == "getUrlWebGuiDefault":
            obj = guiProbe.gui()
            ans = obj.getUrlWEBGuiDefault()
            return jsonify(ans)
        else:
            return {"name_teste": "Doesnt Exist", "response": "none"}