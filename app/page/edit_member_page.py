from appium.webdriver.common.mobileby import MobileBy

from app.page.add_member_page import AddMemberPage
from app.page.basepage import BasePage


class EditMemberPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver

    def edit_member(self,name,phonenum):
        self.find(MobileBy.XPATH, '//*[contains(@text,"姓名")]//../*[@text="必填"]').send_keys(name)
        self.find(MobileBy.XPATH, '//*[contains(@text,"手机")]//..//*[@text="必填"]').send_keys(phonenum)
        self.find_and_click(MobileBy.XPATH, '//*[@text="保存"]')
        # self.driver.find_element(MobileBy.XPATH,'//*[@text="添加成功"]')
        # sleep(2)
        return AddMemberPage(self.driver)