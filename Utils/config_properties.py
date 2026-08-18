import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/commonDetails.ini")

class ReadConfig_CommonDetails():

    def getDevUrl(self):
        return config.get("Server Connection", "dev_url")

    def getUsername(self):
        return config.get("Login Details", "username")

    def getPassword(self):
        return config.get("Login Details", "password")

    def getInvalidUsername(self):
        return config.get("Login Invalid Details", "username")

    def getInvalidPassword(self):
        return config.get("Login Invalid Details", "password")