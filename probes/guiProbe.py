from selenium import webdriver

class gui:
    def __init__(self):
        self.ip = []
        self.username = []
        self.password = []

    def getUrlWEBGuiDefault(self):
        PATH = 'C:\chromedriver.exe'
        driver = webdriver.Chrome(PATH)

        try:
            driver.get('http://192.168.15.1')
            return{"name_test": "testeAberturaWEBGui", "Resultado": "Página aberta com SUCESSO!!!"}
        except:
            print('Excecao')
        # driver.quit()