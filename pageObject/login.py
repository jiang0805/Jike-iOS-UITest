# from common.decorator import *
import time

import allure

from common.decorator import step
from common.log import Log
from common.base import Base
from common.base_page import pkg_name
from pageObject.init import init

log = Log()

class Login(Base):
    @allure.step("检查登录协议更新弹窗")
    @step
    def check_agreement_update_popup_window(self):
        # 检查登录页协议更新弹窗
        log.i("检查登录页协议更新弹窗")
        assert self.s(name="点击查看《用户协议》，《隐私协议》。", className='XCUIElementTypeStaticText').get(timeout=5)

    @allure.step('选择不同意并退出')
    @step
    def select_agreement_update_disagree(self):
        # 选择不同意并退出按钮
        log.i("选择不同意并退出")
        self.s(name="不同意并退出", className="XCUIElementTypeStaticText").click()

    @allure.step('选择同意协议')
    @step
    def select_agreement_update_agree(self):
        # 选择同意按钮
        log.i("选择同意协议")
        self.s(name="同意", className="Button").click()

    @allure.step('检查登录页面')
    @step
    def check_login_enter(self):
        # 检查登录入口
        # 检查微信登录入口
        log.i("检查微信登录入口")
        assert self.s(name="微信登录", className="XCUIElementTypeStaticText").exists, "缺少微信登录入口"
        # 检查Apple登录入口
        log.i("检查Apple登录入口")
        assert self.s(name="通过Apple登录", className="XCUIElementTypeStaticText").exists, "缺少Apple登录入口"
        # 检查其他登录方式按钮
        log.i("检查其他登录方式入口")
        assert self.s(name="其他登录方式 ", className="XCUIElementTypeButton").exists, "缺少其他登录入口"
        # 检查QQ登录入口
        log.i("检查QQ登录入口")
        assert self.s(xpath="//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[4]/Button[2]").exists, "缺少QQ登录入口"
        # 检查手机号登录入口
        log.i("检查手机号登录入口")
        assert self.s(xpath="//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[4]/Button[3]").exists, "缺少手机号登录入口"
        # 检查微博登录入口
        log.i("检查微博登录入口")
        assert self.s(xpath="//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[4]/Button[4]").exists, "缺少微博登录入口"

    @allure.step('检查更多登录方式')
    @step
    def select_more_login_window(self):
        # 选择更多登录方式
        log.i("选择更多登录方式")
        self.s(name="其他登录方式 ", className="XCUIElementTypeButton").click(timeout=2)

    @allure.step('勾选已阅读并同意协议按钮')
    @step
    def select_agreement_box(self):
        # 勾选已阅读并同意协议按钮
        log.i("勾选已阅读并同意协议按钮")
        self.s(xpath="//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[3]/Other[1]/Button[1]").click()

    @allure.step('在更多登录方式抽屉中 勾选已阅读并同意协议')
    @step
    def select_agreement_box_window(self):
        # 在更多登录方式抽屉中 勾选已阅读并同意协议
        log.i("在更多登录方式抽屉中 勾选已阅读并同意协议")
        self.s(xpath="//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[4]/Other[2]/Button[1]").click()

    @allure.step('关闭更多登录方式抽屉')
    @step
    def close_login_window(self):
        # 关闭更多登录方式抽屉
        log.i("关闭更多登录方式抽屉")
        self.s(name="ic common old close default", className="XCUIElementTypeButton").click()

    @allure.step('选择手机号登录')
    @step
    def select_phone_login(self):
        # 选择手机号登录
        log.i("选择手机号登录")
        self.s(xpath="//Window/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[4]/Button[3]").click()

    @allure.step('选择账号密码登录')
    @step
    def select_phone_psw_login(self):
        # 选择账号密码登录
        log.i("选择账号密码登录")
        self.s(name="使用密码登录", className="XCUIElementTypeStaticText").click(timeout=2)

    @allure.step('选择国家区号')
    @step
    def select_country_number(self):
        # 选择国家区号
        log.i("选择国家区号")
        self.s(name="+86", className="Button").click()
        self.s(name="+86", className="XCUIElementTypeStaticText").click()

    @allure.step('输入手机号，密码 , 登录账号')
    @step
    def select_phone_password(self, phone, password):
        # 输入手机号，密码 , 登录账号
        log.i("输入手机号，密码 , 登录账号")
        self.s(value="输入手机号码", className="XCUIElementTypeTextField").set_text(phone)
        self.s(value="输入密码", className="XCUIElementTypeSecureTextField").set_text(password)
        self.s(name="登录", className="Button").click()

    @allure.step('根据动态tab和我-编辑按钮，检查是否登录账号')
    @step
    def check_login_status(self):
        # 根据动态tab和我-编辑按钮，检查是否登录账号
        log.i("根据动态tab和我-编辑按钮，检查是否登录账号")
        assert self.s(name="动态", className="Button").exists, "未检查到动态tab, not_login"
        self.s(name="我", className="Button").click(),
        assert self.s(name="编辑", className="Button").exists, "未检测到编辑用户资料按钮, not_login"

    @allure.step('退出登录')
    @step
    def logout(self):
        # 退出登录
        log.i("退出登录")
        self.s(name="我", className="Button").click()
        self.s(name="ic basic hamburger", className="Button").click(timeout=2)
        self.s(name="系统设置", className="XCUIElementTypeStaticText").click(timeout=2)
        self.s.swipe_up()
        self.s(name="退出登录", className="XCUIElementTypeStaticText").click(timeout=2)
        # click点的坐标为iphone12promax上的百分比位置，weditor中看不到系统弹窗的参数
        self.s.click(0.523, 0.867)


page = Login()

def check_agreement():
    page.check_agreement_update_popup_window()
    page.select_agreement_update_disagree()
    # page.check_login_status()
    page.start_app(pkg_name)
    page.check_agreement_update_popup_window()
    page.select_agreement_update_agree()
    # page.check_login_status()

def check_login():
    page.check_login_status()

def agreement_agree():
    page.select_agreement_update_agree()

def phone_login(phone, password):
    # page.select_agreement_update_agree()
    page.select_more_login_window()
    page.select_agreement_box_window()
    page.select_phone_login()
    time.sleep(1)
    page.select_phone_psw_login()
    page.select_phone_password(phone, password)
    time.sleep(2)
    page.check_login_status()

def area_code_button():
    page.select_agreement_update_agree()
    page.select_more_login_window()
    page.select_phone_login()
    page.select_country_number()

def logout():
    page.logout()

def reset_login_status():
    login_status = init().check_login_status()
    if login_status == "notLogin":
        return True
    elif login_status == "logged":
        page.logout()
    else:
        log.i("检查app登录状态出错")
        print("检查app登录状态出错")

