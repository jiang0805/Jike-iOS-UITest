import wda


class Base():
    @classmethod
    def set_driver(cls):
        print("wda usb 设备连接")
        cls.s = wda.USBClient().session()

    def get_driver(self):
        return self.s

    @classmethod
    def start_app(cls, pkg_name):
        print('启动指定的App')
        cls.s.app_start(pkg_name)

    def stop_app(self, pkg_name):
        print('终止指定App')
        self.s.app_terminate(pkg_name)

    @classmethod
    def set_path(cls, ps):
        cls.path = ps

    def get_path(self):
        return self.path



