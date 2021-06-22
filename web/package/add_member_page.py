from time import sleep
from selenium.webdriver.common.by import By
from web.package.basepage import BasePage

# 添加成员页面
class AddMember(BasePage):
    def add_member(self,name,id,phone):
        #局部导入，避免循环导入
        from web.package.contact_page import Contact
        self.find(By.ID, "username").send_keys(name)
        self.find(By.ID, "memberAdd_acctid").send_keys(id)
        self.find(By.ID, "memberAdd_phone").send_keys(phone)
        self.find_and_click(By.CSS_SELECTOR, ".js_btn_save")
        sleep(2)
        return Contact(self.driver)