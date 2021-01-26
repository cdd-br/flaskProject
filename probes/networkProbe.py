import requests

class network:
    def __init__(self):
        self.ip = []
        self.username = []
        self.password = []

    def setip(self, ip):
        self.ip = ip

    def getip(self):
        return self.ip

    def setusername(self, usename):
        self.username = self.username

    def getusername(self):
        return self.username

    def setpassword(self, password):
        self.ip = password

    def getpassword(self):
        return self.getpassword()

    def getUrlGuiDefault(self):
        self.setip('http://192.168.15.1')
        response = requests.get(self.ip)
        if response.status_code == 200:
            return {"name_test": "testeIP", "status": response.status_code}
        else:
            return {"name_test": "testeIP", "status": response.status_code}

    def getUrlGuiCustom(self):
        response = requests.get(self.ip)
        if response.status_code == 200:
            return {"name_test": "testeIP", "status": response.status_code}
        else:
            return {"name_test": "testeIP", "status": response.status_code}


