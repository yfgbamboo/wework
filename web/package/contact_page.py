from time import sleep
from selenium.webdriver.common.by import By
from web.package.add_member_page import AddMember
from web.package.basepage import BasePage

# 通讯录页面
class Contact(BasePage):
    def click_add_member(self):

        sleep(5)
        # ele = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
        while True:
            # *ele 解元组 通过bycss_selector的方法定位元素
            self.find_and_click(By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
            ele_num = len(self.finds(By.ID, "username"))
            print(ele_num)
            if ele_num > 0:
                break
        return AddMember(self.driver)

    def get_member(self):
        member_list = []

        eles = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(5)")

        for value in eles:
            member_list.append(value.get_attribute("title"))
        print(member_list)
        return member_list

