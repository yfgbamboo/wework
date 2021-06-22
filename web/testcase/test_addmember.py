import pytest

from web.package.main_page import MainPage


class TestAddmember:
    def setup(self):
        # 对主页实例化
        self.main = MainPage()

    def teardown(self):
        pass

    @pytest.mark.parametrize("name,id,phone",[("张三18","050820","18000050820"),
                                              ("张三19","050821","18000050821")])
    def test_addmember(self,name,id,phone):
        # name = "zhangsan9"
        # id = "050809"
        # phone = "18000050809"
        # 链式调用
        # 主页-通讯录页面-点击添加成员-添加成员-获取成员信息
        ele=self.main.goto_contact().click_add_member().add_member(name,id,phone).get_member()
        print(ele)
        # 断言新增手机是否在成员信息里欸包
        assert phone in ele