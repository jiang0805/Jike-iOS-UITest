from common import *
from common.base import Base
from common.base_page import pkg_name
from common.decorator import *
from pageObject import login
from config.read_config import ReadConfig

phone = ReadConfig().get_phone_number()
password = ReadConfig().get_password_number()

class init(Base):
    @step
    def check_login_status(self):
        # 检查登录状态
        log.i("检查登录状态，登录返回logged，未登录返回notLogin，其余返回other")
        if self.s(name="动态", className="Button").exists:
            print("Login")
            return "logged"
        elif self.s(name="点击查看《用户协议》，《隐私协议》。", className='XCUIElementTypeStaticText').exists or self.s(name="微信登录", className="XCUIElementTypeStaticText").exists:
            print("notLogin")
            return "notLogin"

        else:
            return "other"

    @step
    def login_test_account(self):
        # 检查是否在home页
        state = self.s(text="发现", className="Button").exists and self.s(text="动态", className="Button").exists
        need_login = self.s(name="点击查看《用户协议》，《隐私协议》。", className='XCUIElementTypeStaticText').exists or self.s(name="微信登录", className="XCUIElementTypeStaticText").exists
        if state:
            print("当前为登录状态")
            return "当前为登录状态,不需要登录账号"
        elif need_login:
            login.agreement_agree()
            login.phone_login(phone, password)
            print("登录测试账号")
            return "登录测试账号"
        else:
            raise Exception("fail to get login status")

    @step
    def check_home_state(self):
        # 检查是否在home页
        state = self.s(text="发现", className="Button").exists and self.s(text="动态", className="Button").exists
        if state:
            return True
        else:
            raise Exception("不在Home页")

    @step
    def activate_app(self):
        # 启动即刻app
        self.s.app_activate(pkg_name)

    @step
    def terminate_app(self):
        # 关闭即刻app
        self.s.app_terminate(pkg_name)

    @step
    def click_dynamic_tab(self):
        # 点击动态tab--tabbar操作
        self.s(name="动态", className="XCUIElementTypeButton").click()
        assert self.s(name="动态", className="XCUIElementTypeStaticText").exists, "不在动态页"

    @step
    def click_discovery_tab(self):
        # 点击推荐tab--tabbar操作
        self.s(name="发现", className="XCUIElementTypeButton").click()
        assert self.s(name="动态广场", className="XCUIElementTypeStaticText").exists, "不在发现页"

    @step
    def click_notice_tab(self):
        # 点击通知tab--tabbar操作
        self.s(name="通知", className="XCUIElementTypeButton").click()
        assert self.s(name="我的通知", className="XCUIElementTypeStaticText").exists, "不在通知页"

    @step
    def click_my_tab(self):
        # 点击我tab--tabbar操作
        self.s(name="我", className="XCUIElementTypeButton").click()
        assert self.s(name="编辑", className="XCUIElementTypeButton").exists, "不在我的页"

    @step
    def click_post_tab(self):
        # 点击发布新动态tab--tabbar操作
        self.s.click(0.57, 0.939)
        assert self.s(name="发布新动态", className="XCUIElementTypeStaticText").exists, "不在发布页"

