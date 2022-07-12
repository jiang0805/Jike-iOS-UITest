
from common.base import Base
from config.read_config import ReadConfig

pkg_name = ReadConfig().get_pkg_name()
# print(pkg_name)

class BasePage(Base):

    def launch_app(self,pkg_name):
        pass

