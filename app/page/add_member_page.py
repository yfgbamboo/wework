# 添加成员页
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from app.page.basepage import BasePage


class AddMemberPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver

    def click_add_menual(self):
        from app.page.edit_member_page import EditMemberPage
        # click 手动输入添加
        self.find_and_click(MobileBy.XPATH,'//*[@text="手动输入添加"]')
        return EditMemberPage(self.driver)

    def verity_toast(self):
        self.driver.find_element(MobileBy.XPATH,'//*[@text="添加成功"]')
        return True