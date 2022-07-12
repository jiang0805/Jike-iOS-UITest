import time

import allure

from common.decorator import *
from pageObject.init import init
from common.base import Base


class mine(Base):

    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    @allure.step('判断主客态个人页')
    @step
    def check_mine_status(self):
        # 判断主客态个人页
        log.i("判断主客态个人页")
        if self.s(name="编辑", className="XCUIElementTypeButton").exists:
            return "主态个人主页"
        elif self.s(name="返回", className="XCUIElementTypeButton").exists and self.s(name="ic basic more", className="XCUIElementTypeButton"):
            return "客态个人主页"
        else:
            raise Exception("未检测到编辑，返回按钮和...按钮，不在个人页")

    @allure.step('进入更多（设置）页面')
    @step
    def click_more(self):
        # 进入更多（设置）页面
        log.i("进入更多（设置）页面")
        self.s(name="ic basic hamburger", className="XCUIElementTypeButton").click(timeout=3)
        assert self.s(name="更多", className="XCUIElementTypeStaticText").exists, "未进入到更多页面"

    @allure.step('检查我的页面元素')
    @step
    def check_page_element(self):
        # 检查我的页面元素
        log.i("检查我的页面元素")
        time.sleep(1)
        assert self.s(name="ic basic withcolor jikeyellow", className="XCUIElementTypeButton").exists or self.s(name="开通会员", className="XCUIElementTypeButton").exists, "会员入口不存在"
        assert self.s(name="编辑", className="XCUIElementTypeButton").exists, "编辑按钮不存在"
        assert self.s(name="ic basic share", className="XCUIElementTypeButton").exists, "分享按钮不存在"
        assert self.s(name="动态", className="XCUIElementTypeStaticText").exists, "个人feed 动态tab不存在"
        assert self.s(name="ic basic search outline", className="XCUIElementTypeButton").exists, "个人feed 搜索按钮不存在"

    @allure.step('点击分享按钮')
    @step
    def click_share_mine(self):
        # 点击分享按钮
        log.i("点击分享按钮")
        self.s(name="ic basic share", className="XCUIElementTypeButton").click(timeout=1)
        assert self.s(name="分享个人主页", className="XCUIElementTypeStaticText"), "未进入分享页面"

    @allure.step('点击我的关注')
    @step
    def click_mine_follow(self):
        # 点击我的关注
        log.i("点击我的关注")
        self.s(name="关注", className="XCUIElementTypeStaticText").click(timeout=1)
        assert self.s(name="我关注的人", className="XCUIElementTypeStaticText").exists, "未进入我关注的人页面"

    @allure.step('点击关注我的')
    @step
    def click_follow_me(self):
        # 点击关注我的
        log.i("点击关注我的")
        self.s(name="被关注", className="XCUIElementTypeStaticText").click(timeout=1)
        assert self.s(name="关注我的人", className="XCUIElementTypeStaticText").exists, "未进入关注我的人页面"

    @allure.step('点击夸夸')
    @step
    def click_boast(self):
        # 点击夸夸
        log.i("点击夸夸")
        self.s(name="夸夸", className="XCUIElementTypeStaticText").click(timeout=1)
        assert self.s(name="最新夸我", className="XCUIElementTypeStaticText").exists, "未进夸夸页面"

    @allure.step('进入编辑个人信息页面')
    @step
    def click_edit(self):
        # 进入编辑个人信息页面
        log.i("进入编辑个人信息页面")
        self.s(name="编辑", className="Button").click(timeout=3)
        assert self.s(name="编辑个人信息", className="XCUIElementTypeStaticText").exists, "未进入编辑个人信息页面"

    @allure.step('改测试账号的名字')
    @step
    def edit_name(self):
        # 改测试账号的名字
        log.i("改测试账号的名字")
        self.s(name="昵称", className="XCUIElementTypeStaticText").click()
        assert self.s(name="修改昵称", className="XCUIElementTypeStaticText").exists, "未进入修改昵称页面"

    @allure.step('修改个性签名')
    @step
    def select_edit_introduce(self):
        # 修改个性签名
        log.i("修改个性签名")
        self.s(name="签名", className="XCUIElementTypeStaticText").click()
        assert self.s(name="修改签名", className="XCUIElementTypeStaticText").exists, "未进入修改个性签名页面"

    @allure.step('修改个性签名为auto_test_account')
    @step
    def edit_introduce(self):
        # 修改个性签名为auto_test_account
        log.i("修改个性签名为auto_test_account")
        now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.s(name="签名", className="XCUIElementTypeStaticText").click()
        time.sleep(1)
        self.s(className="XCUIElementTypeTextView", xpath="//TextView").click()
        self.s(className="XCUIElementTypeTextView", xpath="//TextView").tap_hold(3.0)
        self.s(name="全选", className="XCUIElementTypeStaticText").click()
        self.s(className="XCUIElementTypeTextView").clear_text()
        self.s(className="XCUIElementTypeTextView").set_text("auto_test_account  \n%s"%(now))
        self.s(name="保存", className="Button").click()

    @allure.step('修改情感状态')
    @step
    def select_emotion_status(self):
        # 修改情感状态
        log.i("修改情感状态")
        self.s(name="情感", className="XCUIElementTypeStaticText").click()
        assert self.s(name="选择情感状态", className="XCUIElementTypeStaticText").exists, "未进入修改选择情感状态标识页面"

    @allure.step('修改情感状态为一言难尽')
    @step
    def set_emotion_status(self):
        # 修改情感状态为一言难尽
        log.i("修改情感状态为一言难尽")
        self.s(name="一言难尽", className="XCUIElementTypeStaticText").click()
        time.sleep(1)
        assert self.s(name="一言难尽", className="XCUIElementTypeStaticText").exists, "修改情感状态失败"

    @allure.step('修改会员标识')
    @step
    def select_jellow_icon(self):
        # 修改会员标识
        log.i("修改会员标识")
        self.s(name="Yellow 标识", className="XCUIElementTypeStaticText").click()
        assert self.s(name="不展示", className="XCUIElementTypeStaticText").exists, "未进入修改jellow标识页面"

    @allure.step('选择不展示会员标识')
    @step
    def set_jellow_icon(self):
        # 选择不展示会员标识
        log.i("选择不展示会员标识")
        self.s(name="不展示", className="XCUIElementTypeStaticText").click(timeout=1)
        assert self.s(name="不展示", className="XCUIElementTypeStaticText").exists, "修改jellow标识失败"

    @allure.step('选择性别')
    @step
    def select_edit_gender(self):
        # 选择性别
        log.i("选择性别")
        self.s(name="性别", className="XCUIElementTypeStaticText").click()
        assert self.s(name="修改性别", className="XCUIElementTypeStaticText").exists, "未进入修改性别页面"

    @allure.step('选择性别男')
    @step
    def set_gender_man(self):
        # 选择性别男
        log.i("选择性别男")
        self.s(name="男", className="XCUIElementTypeStaticText").click(timeout=1)
        assert self.s(name="男", className="XCUIElementTypeStaticText").exists, "性别修改失败"

    @allure.step('选择生日')
    @step
    def select_edit_birth(self):
        # 选择生日
        log.i("选择生日")
        self.s(name="生日", className="XCUIElementTypeStaticText").click()
        assert self.s(name="修改生日", className="XCUIElementTypeStaticText").exists, "未进入修改生日页面"

    @allure.step('修改学校信息')
    @step
    def select_emotion_status(self):
        # 修改学校信息
        log.i("修改学校信息")
        self.s(name="情感", className="XCUIElementTypeStaticText").click()
        assert self.s(name="选择情感状态", className="XCUIElementTypeStaticText").exists, "未进入修改选择情感状态标识页面"

    @allure.step('修改学校为哈哈+当前日期时间')
    @step
    def set_emotion_status(self):
        # 修改情感状态为一言难尽
        log.i("修改情感状态为一言难尽")
        self.s(name="一言难尽", className="XCUIElementTypeStaticText").click()
        time.sleep(1)
        assert self.s(name="一言难尽", className="XCUIElementTypeStaticText").exists, "修改情感状态失败"

    @allure.step('点击二级页面的返回按钮')
    @step
    def edit_back_button(self):
        # 点击二级页面的返回按钮
        log.i("点击二级页面的返回按钮")
        self.s(name="返回", className="XCUIElementTypeButton").click()



page = mine()

def check_mine_page():
    init().click_my_tab()
    page.check_mine_status()
    page.check_page_element()

def edit_account_introduce():
    init().click_my_tab()
    page.click_edit()
    page.edit_introduce()
    page.edit_back_button()

def edit_account_gender():
    # init().click_my_tab()
    page.click_edit()
    page.select_edit_gender()
    page.set_gender_man()
    page.edit_back_button()

def edit_account_jellow():
    # init().click_my_tab()
    page.click_edit()
    page.select_jellow_icon()
    page.set_jellow_icon()
    page.edit_back_button()

def edit_account_emotion():
    # init().click_my_tab()
    page.click_edit()
    page.select_emotion_status()
    page.set_emotion_status()
    page.edit_back_button()


