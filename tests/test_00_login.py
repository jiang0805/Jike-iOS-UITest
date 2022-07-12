import allure
import pytest

from common.base import Base
from pageObject import login, init
from config.read_config import ReadConfig
from pageObject.init import init
from common.decorator import *

phone = ReadConfig().get_phone_number()
password = ReadConfig().get_password_number()
@pytest.mark.jw
@allure.feature("登录")
class TestLogin(Base):
    @classmethod
    def setup_method(cls):
        init().activate_app()
        log.i("启动后，检查app登录态")
        login.reset_login_status()

    @classmethod
    def teardown_class(cls):
        log.i("运行完关闭app")
        init().terminate_app()
        init.stop_app()

    @allure.description("检查登录页协议更新弹窗")
    @case
    def test_00_check_agreement(self):
        login.check_agreement()

    @allure.description("登录账号")
    @case
    def test_01_phone_login(self):
        login.phone_login(phone, password)

    @allure.description("登出账号")
    @case
    def test_02_logout(self):
        login.logout()
