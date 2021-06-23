from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from app.page.basepage import BasePage
from app.page.contactlist_page import ContactListPage

# 主页
class MainPage(BasePage):
    # def __init__(self,driver:WebDriver): #指定driver类型
    #     self.driver =driver
    _address_list_element = (MobileBy.XPATH, '//*[@text="通讯录"]')
    def goto_contact(self):
        # 点击通讯录
        self.find_and_click(*self._address_list_element)
        return ContactListPage(self.driver)