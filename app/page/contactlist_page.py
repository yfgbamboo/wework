from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException

from app.page.add_member_page import AddMemberPage
from app.page.basepage import BasePage


class ContactListPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver



    def click_addmember(self):
        #点击添加成员
        self.swipe_find('添加成员',num=2).click()

        return AddMemberPage(self.driver)