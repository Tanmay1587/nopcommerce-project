import configparser

config=configparser.RawConfigParser()
configPath=r'C:\Users\Tanmay.Gupta\PycharmProjects\nopcommerce\Configurations\config.ini'
config.read(configPath)

class ReadConfig:

    @staticmethod
    def getAppURL():
        url = config.get('common info','baseURL')
        return url

    @staticmethod
    def getusername():
        un = config.get('common info','username')
        return un

    @staticmethod
    def getpassword():
        ps = config.get('common info','password')
        return ps