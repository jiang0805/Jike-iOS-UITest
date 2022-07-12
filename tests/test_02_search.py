import pytest
from pageObject import init, search
from pageObject.init import init
from common.decorator import *



@pytest.mark.jw
@allure.description("搜索页面")
class TestSearch(Base):
    @classmethod
    def setup_class(cls):
        log.i("启动app")
        init().activate_app()
        log.i("检查是否登录")
        init().check_login_status()
        log.i("检查是否进入主页")
        init().check_home_state()

    @classmethod
    def setup_class(cls):
        pass

    @allure.description("检查搜索圈子")
    @case
    def test_00_search_circle(self):
        search.check_search_circle()

    @allure.description("检查搜索用户")
    @case
    def test_01_search_user(self):
        search.check_search_user()

    @allure.description("检查搜索动态")
    @case
    def test_02_search_comment(self):
        search.check_search_comment()

    @allure.description("检查搜索综合")
    @case
    def test_03_search_default(self):
        search.check_search_default()


