import pytest
from pageObject import init, mine
from pageObject.init import init
from common.decorator import *


@pytest.mark.jw
@allure.description("我的页面")
class TestMine(Base):
    @classmethod
    def setup_class(cls):
        init().activate_app()
        log.i("启动后，检查app登录态")
        init().check_login_status()
        init().login_test_account()
        init().check_home_state()

    @classmethod
    def teardown_class(cls):
        init().click_my_tab()

    @allure.description("检查我的页面元素")
    @case
    def test_00_check_mine(self):
        mine.check_mine_page()

    @allure.description("修改个性签名")
    @case
    def test_01_edit_account_introduce(self):
        mine.edit_account_introduce()

    @allure.description("修改性别")
    @case
    def test_01_edit_account_gender(self):
        mine.edit_account_gender()

    @allure.description("修改会员标识")
    @case
    def test_01_edit_account_jellow(self):
        mine.edit_account_jellow()

