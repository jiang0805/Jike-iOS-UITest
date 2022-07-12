import logging

from common.decorator import *
from pageObject.init import init
from common.base import Base

class search(Base):
    @allure.step("点击搜索框")
    @step
    def click_search(self):
        # 点击搜索框
        log.i("点击搜索框")
        self.s.click(0.223, 0.08)
        assert self.s(name="热点", className="XCUIElementTypeStaticText").exists, "未发现搜索页热点,不在搜索页面"

    @allure.step("搜索 today 圈子")
    @step
    def search_circle(self):
        # 搜索 today 圈子
        log.i("搜索 today 圈子")
        self.s(className="XCUIElementTypeTextField").set_text("today")
        self.s(name="Search", className="XCUIElementTypeButton").click(timeout=1)
        time.sleep(1)
        assert self.s(name="已加入", className="XCUIElementTypeButton").exists, "搜索结果没有today圈子"

    @allure.step("搜索用户，当前账号的名称")
    @step
    def search_user(self):
        # 搜索用户，桂冠诗人
        log.i("搜索用户，桂冠诗人")
        self.s(className="XCUIElementTypeTextField").set_text("桂冠诗人")
        self.s(name="Search", className="XCUIElementTypeButton").click(timeout=1)
        time.sleep(1)
        self.s(className="XCUIElementTypeStaticText", name="用户").click()
        assert self.s(name="桂冠诗人", className="XCUIElementTypeStaticText").exists, "搜索结果没有桂冠诗人用户"

    @allure.step("搜索动态，鸡蛋")
    @step
    def search_default(self):
        # 搜索，展示默认搜索结果"
        log.i("搜索，展示默认搜索结果")
        self.s(className="XCUIElementTypeTextField").set_text("鸡蛋")
        self.s(name="Search", className="XCUIElementTypeButton").click()
        time.sleep(1)
        assert self.s(name="查看更多圈子", className="XCUIElementTypeStaticText").exists, "搜索结果异常"

    @allure.step("搜索动态，按最新发布排序")
    @step
    def search_moments_by_update(self):
        # 搜索动态，按最新发布排序，按cell的xpath判断是否有搜索结果"
        log.i("搜索动态，按最新发布排序")
        self.s(name="动态", className="XCUIElementTypeStaticText").click()
        time.sleep(1)
        self.s(name="最新发布", className="XCUIElementTypeStaticText").click()
        time.sleep(1)
        assert self.s(xpath="//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/ScrollView[1]/Other[1]/Table[1]/Cell[1]").exists, "最新发布动态，搜索失败"

    @allure.step("搜索动态，综合搜索结果（默认）")
    @step
    def search_moments_default(self):
        # 搜索动态，按默认综合搜索结果展示"
        log.i("搜索动态，按默认综合搜索结果展示")
        self.s(name="动态", className="XCUIElementTypeStaticText").click()
        self.s(name="默认", className="XCUIElementTypeStaticText").click()
        time.sleep(1)
        assert self.s(xpath="//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/ScrollView[1]/Other[1]/Table[1]/Cell[1]").exists, "动态-默认搜索，搜索失败"

    @allure.step("搜索动态，最多互动搜索结果")
    @step
    def search_moments_by_comment(self):
        # 搜索动态，最多互动搜索结果，"
        log.i("搜索动态，最多互动搜索结果")
        self.s(name="动态", className="XCUIElementTypeStaticText").click()
        self.s(name="默认", className="XCUIElementTypeStaticText").click()
        time.sleep(1)
        assert self.s(xpath="//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/ScrollView[1]/Other[1]/Table[1]/Cell[1]").exists, "动态-最多互动，搜索失败"

    @allure.step("搜索动态，按时间搜索-一周")
    @step
    def search_moments_by_week(self):
        # 搜索动态，按时间搜索-一周"
        log.i("搜索动态，按时间搜索-一周")
        self.s(name="动态", className="XCUIElementTypeStaticText").click()
        self.s(name="搜索范围", className="XCUIElementTypeStaticText").click()
        self.s(name="最近一周", className="XCUIElementTypeStaticText").click()
        time.sleep(1)
        assert self.s(xpath="//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/ScrollView[1]/Other[1]/Table[1]/Cell[1]").exists, "动态-搜索范围-最近一周，搜索失败"

    @allure.step("搜索动态，按时间搜索-一月")
    @step
    def search_moments_by_month(self):
        # 搜索动态，按时间搜索-一月"
        log.i("搜索动态，按时间搜索-一月")
        self.s(name="搜索范围", className="XCUIElementTypeStaticText").click()
        self.s(name="最近30天", className="XCUIElementTypeStaticText").click()
        time.sleep(1)
        assert self.s(xpath="//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/ScrollView[1]/Other[1]/Table[1]/Cell[1]").exists, "动态-搜索范围-最近30天，搜索失败"

    @allure.step("搜索动态，按时间搜索-半年")
    @step
    def search_moments_by_half_year(self):
        # 搜索动态，按时间搜索-半年"
        log.i("搜索动态，按时间搜索-半年")
        self.s(name="搜索范围", className="XCUIElementTypeStaticText").click()
        self.s(name="最近半年", className="XCUIElementTypeStaticText").click()
        time.sleep(1)
        assert self.s(xpath="//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/ScrollView[1]/Other[1]/Table[1]/Cell[1]").exists, "动态-搜索范围-最近半年，搜索失败"

    @allure.step("搜索页面返回按钮")
    @step
    def search_back_button(self):
        # 搜索页面返回按钮"
        log.i("搜索页面返回按钮")
        self.s(name="返回", className="XCUIElementTypeStaticText").click()
        assert self.s(name="发现", className="XCUIElementTypeButton").exists, "返回上级页面失败"


page = search()

def check_search_circle():
    init().click_discovery_tab()
    page.click_search()
    page.search_circle()
    page.search_back_button()

def check_search_user():
    init().click_discovery_tab()
    page.click_search()
    page.search_user()
    page.search_back_button()

def check_search_default():
    init().click_discovery_tab()
    page.click_search()
    page.search_default()
    page.search_back_button()

def check_search_comment():
    init().click_discovery_tab()
    page.click_search()
    page.search_moments_default()
    page.search_moments_by_update()
    page.search_moments_by_comment()
    page.search_moments_by_week()
    page.search_back_button()
    page.click_search()
    page.search_default()
    page.search_moments_by_month()
    page.search_back_button()
    page.click_search()
    page.search_default()
    page.search_moments_by_half_year()
    page.search_back_button()