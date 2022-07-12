from common.decorator import *
from pageObject.init import init
from common.base import Base

class post(Base):


    @allure.step("点击发布按钮")
    @step
    def click_post(self):
        # 点击发布按钮
        log.i("点击发布按钮")
        self.s(name="发布", className="XCUIElementTypeStaticText").click()
        time.sleep(1)
        assert self.s(name="发送成功", className="XCUIElementTypeStaticText").exists, "[发送成功]toast元素不存在,发送失败"

    @allure.step("检查发布页元素")
    @step
    def check_post_elm(self):
        # 检查发布页元素
        log.i("检查发布页元素")
        assert self.s(name="未选择圈子", className="XCUIElementTypeStaticText").exists, "未发现推荐圈子"
        assert self.s(name="你在哪里?", className="XCUIElementTypeStaticText").exists, "未发现定位按钮"
        # assert self.s(name="当前为beta环境，请切换到正式环境发布", className="XCUIElementTypeStaticText").exists, "未发现beta环境提示"
        assert self.s(name="链接", className="XCUIElementTypeStaticText").exists, "未发现链接选择按钮"
        assert self.s(name="图片", className="XCUIElementTypeStaticText").exists, "未发现图片选择按钮"
        assert self.s(name="视频", className="XCUIElementTypeStaticText").exists, "未发现视频选择按钮"
        assert self.s(name="所有人可评论", className="XCUIElementTypeStaticText").exists, "未发现评论权限选择按钮"

    @allure.step("关闭beta环境提示toast")
    @step
    def close_beta_toast(self):
        # 关闭beta环境提示toast
        log.i("关闭beta环境提示toast")
        toast = self.s(name="当前为beta环境，请切换到正式环境发布", className="XCUIElementTypeStaticText").exists
        if toast:
            self.s(xpath="//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[3]/Other[1]/Other[1]/Other[1]/Button[1]").click()
        else:
            log.i("当前不在beta环境")
            return "当前不在beta环境"


    @allure.step("输入文字")
    @step
    def input_context(self):
        # 输入文字
        log.i("输入文字")
        now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.s.click(0.124, 0.204)  # 点击输入框
        self.s(className="XCUIElementTypeCell", xpath="//Table/Cell[1]").set_text("这是一个无用的流水账动态 \n%s"%(now))

    @allure.step("选择图片")
    @step
    def input_picture(self):
        # 选择图片
        log.i("选择图片")
        self.s(name="图片", className="XCUIElementTypeStaticText").click()
        time.sleep(1)
        self.s(className="XCUIElementTypeCell", xpath="//CollectionView/Cell[2]").click()
        time.sleep(1)
        self.s(name="确定", className="XCUIElementTypeStaticText").click()
        assert self.s(xpath="//Table/Cell[1]/Button[1]").exists, "图片添加失败"

    @allure.step("删除图片")
    @step
    def del_picture(self):
        # 删除图片
        log.i("删除图片")
        self.s.click(0.285, 0.357)
        assert self.s(xpath="//Table/Cell[1]/Button[1]").exists!=True, "图片删除失败"

    @allure.step("选择视频")
    @step
    def input_video(self):
        # 选择视频
        log.i("选择视频")
        self.s(name="视频", className="XCUIElementTypeStaticText").click()
        time.sleep(1)
        self.s(className="XCUIElementTypeCell", xpath="//CollectionView/Cell[2]").click()
        time.sleep(1)
        self.s(name="确定", className="XCUIElementTypeStaticText").click()
        assert self.s(name="ic media old videoplayer feedp", className="XCUIElementTypeButton").exists, "视频添加失败"

    @allure.step("删除视频")
    @step
    def del_video(self):
        # 删除视频
        log.i("删除视频")
        self.s.click(0.285, 0.357)
        assert self.s(name="ic media old videoplayer feedp", className="XCUIElementTypeButton").exists!=True, "视频删除失败"


    @allure.step("输入链接")
    @step
    def input_link(self):
        # 选择链接
        log.i("输入链接")
        self.s(name="链接", className="XCUIElementTypeStaticText").click()
        time.sleep(1)
        self.s.click(0.219, 0.354)
        self.s(className="XCUIElementTypeTextField").set_text( "https://m.okjike.com/originalPosts/62c25d3a13392561e4c4a3f0?s=ewoidSI6ICI1ZWU2NDlkNWFhODgwMDAwMTc2YzhjYWUiCn0=")
        self.s(name="添加", className="XCUIElementTypeStaticText").click()
        time.sleep(1)
        assert self.s(className="XCUIElementTypeOther", xpath="//Table/Cell[1]/Other[2]").exists, "链接解析失败"

    @allure.step("删除链接")
    @step
    def del_link(self):
        # 删除链接
        log.i("删除链接")
        self.s(className="XCUIElementTypeButton", xpath="//Table/Cell[1]/Other[2]/Button[2]").click()
        time.sleep(1)
        assert self.s(xpath="//Table/Cell[1]/Other[2]", className="XCUIElementTypeOther").exists!=True, "链接删除失败"

    @allure.step("添加定位")
    @step
    def input_location(self):
        # 添加定位
        log.i("添加定位")
        self.s(name="你在哪里?", className="XCUIElementTypeStaticText").click()
        time.sleep(1)
        self.s(name="上海市", className="XCUIElementTypeStaticText").click()
        time.sleep(1)
        assert self.s(name="上海市", className="XCUIElementTypeStaticText").exists, "位置添加失败"

    @allure.step("删除定位")
    @step
    def del_link(self):
        # 删除定位
        log.i("删除定位")
        self.s(name="上海市", className="XCUIElementTypeStaticText").click()
        time.sleep(1)
        self.s(name="不显示所在位置", className="XCUIElementTypeStaticText").click()
        time.sleep(1)
        assert self.s(name="你在哪里?", className="XCUIElementTypeStaticText").exists, "删除定位失败"

    @allure.step("添加评论权限")
    @step
    def input_comment_auth(self):
        # 添加评论权限
        log.i("添加评论权限")
        self.s(name="所有人可评论", className="XCUIElementTypeStaticText").click()
        time.sleep(1)
        self.s(name="你关注的人", className="XCUIElementTypeStaticText").click()
        self.s(name="确定", className="XCUIElementTypeStaticText").click()
        time.sleep(1)
        assert self.s(name="部分用户可评论", className="XCUIElementTypeStaticText").exists, "评论权限添加失败"

    @allure.step("删除评论权限")
    @step
    def del_comment_auth(self):
        # 删除评论权限
        log.i("删除评论权限")
        self.s(name="部分用户可评论", className="XCUIElementTypeStaticText").click()
        time.sleep(1)
        self.s(name="你关注的人", className="XCUIElementTypeStaticText").click()
        self.s(name="确定", className="XCUIElementTypeStaticText").click()
        time.sleep(1)
        assert self.s(name="所有人可评论", className="XCUIElementTypeStaticText").exists, "评论权限删除失败"

    @allure.step("删除动态")
    @step
    def del_post(self):
        # 删除动态
        log.i("删除动态")
        if self.s(name="刚刚", className="XCUIElementTypeStaticText").exists:
            self.s(name="我", className="XCUIElementTypeButton").click()
            self.s(name="ic basic more", className="XCUIElementTypeButton").click()
            self.s(name="删除", className="XCUIElementTypeStaticText").click()
            self.s.click(0.675, 0.541)
            time.sleep(1)
            assert self.s(name="删除成功", className="XCUIElementTypeStaticText").wait(timeout=1), "动态删除失败"
        elif self.s(nameContains="发送失败", className="XCUIElementTypeStaticText").exists:
            log.i("动态发送失败")
            return "动态发送失败"
        else:
            log.i("找不到动态")
            return "找不到动态"



page = post()
def post_text():
    init().click_post_tab()
    page.close_beta_toast()
    page.check_post_elm()
    page.input_context()
    page.click_post()
    page.del_post()

def post_text_common():
    init().click_post_tab()
    page.close_beta_toast()
    page.check_post_elm()
    page.input_context()
    page.input_comment_auth()
    page.click_post()
    page.del_post()

def post_text_location():
    init().click_post_tab()
    page.close_beta_toast()
    page.check_post_elm()
    page.input_context()
    page.input_location()
    page.click_post()
    page.del_post()

def post_text_common_location():
    init().click_post_tab()
    page.close_beta_toast()
    page.check_post_elm()
    page.input_context()
    page.input_comment_auth()
    page.input_location()
    page.click_post()
    page.del_post()

def post_pic_text():
    init().click_post_tab()
    page.close_beta_toast()
    page.check_post_elm()
    page.input_context()
    page.input_picture()
    page.click_post()
    page.del_post()

def post_pic_text_common():
    init().click_post_tab()
    page.close_beta_toast()
    page.check_post_elm()
    page.input_context()
    page.input_picture()
    page.input_comment_auth()
    page.click_post()
    page.del_post()

def post_pic_text_location():
    init().click_post_tab()
    page.close_beta_toast()
    page.check_post_elm()
    page.input_context()
    page.input_picture()
    page.input_location()
    page.click_post()
    page.del_post()

def post_video_text():
    init().click_post_tab()
    page.close_beta_toast()
    page.check_post_elm()
    page.input_context()
    page.input_video()
    page.click_post()
    page.del_post()

def post_video_text_common():
    init().click_post_tab()
    page.close_beta_toast()
    page.check_post_elm()
    page.input_context()
    page.input_video()
    page.input_comment_auth()
    page.click_post()
    page.del_post()

def post_video_text_location():
    init().click_post_tab()
    page.close_beta_toast()
    page.check_post_elm()
    page.input_context()
    page.input_video()
    page.input_location()
    page.click_post()
    page.del_post()

def post_link_text():
    init().click_post_tab()
    page.close_beta_toast()
    page.check_post_elm()
    page.input_context()
    page.input_link()
    page.click_post()
    page.del_post()

def post_link_text_common():
    init().click_post_tab()
    page.close_beta_toast()
    page.check_post_elm()
    page.input_context()
    page.input_link()
    page.input_comment_auth()
    page.click_post()
    page.del_post()

def post_link_text_location():
    init().click_post_tab()
    page.close_beta_toast()
    page.check_post_elm()
    page.input_context()
    page.input_link()
    page.input_location()
    page.click_post()
    page.del_post()

def post_link_text_location_common():
    init().click_post_tab()
    page.close_beta_toast()
    page.check_post_elm()
    page.input_context()
    page.input_link()
    page.input_location()
    page.input_comment_auth()
    page.click_post()
    page.del_post()


def post_pic_location():
    init().click_post_tab()
    page.close_beta_toast()
    page.check_post_elm()
    page.input_picture()
    page.input_location()
    page.click_post()
    page.del_post()

def post_video_location():
    init().click_post_tab()
    page.close_beta_toast()
    page.check_post_elm()
    page.input_video()
    page.input_location()
    page.click_post()
    page.del_post()

def post_link_location():
    init().click_post_tab()
    page.close_beta_toast()
    page.check_post_elm()
    page.input_link()
    page.input_location()
    page.click_post()
    page.del_post()

def post_pic_common():
    init().click_post_tab()
    page.close_beta_toast()
    page.check_post_elm()
    page.input_picture()
    page.input_comment_auth()
    page.click_post()
    page.del_post()

def post_video_common():
    init().click_post_tab()
    page.close_beta_toast()
    page.check_post_elm()
    page.input_video()
    page.input_comment_auth()
    page.click_post()
    page.del_post()

def post_link_common():
    init().click_post_tab()
    page.close_beta_toast()
    page.check_post_elm()
    page.input_link()
    page.input_comment_auth()
    page.click_post()
    page.del_post()

def post_del():
    init().click_post_tab()
    page.close_beta_toast()
    page.check_post_elm()
    page.input_context()
    page.input_video()
    page.del_video()
    page.input_picture()
    page.del_picture()
    page.input_link()
    page.del_link()







