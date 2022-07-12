import configparser
import os

# 获取当前文件路径
prodir = os.path.split(os.path.realpath(__file__))[0]
# 拼接路径与文件名
configPath = os.path.join(prodir, "config.ini")


class ReadConfig:
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath, encoding='UTF-8')

    def get_method(self):
        value = self.cf.get("DEVICE", "method")
        return value

    def get_server_url(self):
        value = self.cf.get("DEVICES", "server")
        return value

    def get_server_token(self):
        value = self.cf.get("DEVICES", "token")
        return value

    def get_server_udid(self):
        value = self.cf.get("DEVICES", "udid")
        return value.split('|')

    def get_devices_ip(self):
        value = self.cf.get("DEVICES", "IP")
        return value.split('|')

    def get_apk_url(self):
        value = self.cf.get("APP", "apk_url")
        return value

    def get_apk_path(self):
        value = self.cf.get("APP", "apk_path")
        return value

    def get_pkg_name(self):
        value = self.cf.get("APP", "pkg_name")
        return value

    def get_phone_number(self):
        value = self.cf.get("TESTDATA", "phone")
        return value

    def get_password_number(self):
        value = self.cf.get("TESTDATA", "password")
        return value


