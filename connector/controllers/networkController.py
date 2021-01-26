from flask_restful import Resource
from flask import jsonify
from probes import networkProbe


class network(Resource):
    def get(self, method, ip):
        if method == "getUrlGuiDefault":
            obj = networkProbe.network()
            ans = obj.getUrlGuiDefault()
            return jsonify(ans)
        elif method == "getUrlGuiCustom":
            obj = networkProbe.network()
            ip_custom = 'http://' + ip + ''
            obj.setip(ip_custom)
            ans = obj.getUrlGuiCustom()
            return jsonify(ans)
        else:
            return {"name_teste": "Doesnt Exist", "response": "none"}