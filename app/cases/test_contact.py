from faker import Faker

from app.page.app import App


class TestContact:
    def setup_class(self):
        self.fake = Faker('zh_CN')
        # 启动app
        self.app = App()

    def setup(self):
        self.main = self.app.start().go_to_main()

    def teardown(self):
        self.app.back()

    def teardown_class(self):
        self.app.stop()

    def test_addcontact(self):
        name = self.fake.name()
        phonenum = self.fake.phone_number()
        result = self.main.goto_contact().click_addmember().click_add_menual().\
            edit_member(name,phonenum).verity_toast()
        assert result

    def test_addcontact1(self):
        name = self.fake.name()
        phonenum = self.fake.phone_number()
        result = self.main.goto_contact().click_addmember().click_add_menual().\
            edit_member(name,phonenum).verity_toast()
        assert result