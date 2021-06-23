'''
启动app,重启，关闭
'''
from appium import webdriver

from app.page.basepage import BasePage
from app.page.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver ==None:
            # 多条用例时，复用driver，提升测试用例的速度
            print("drvier为None，创建driver")
            # 初始化
            caps = {}
            caps["platformName"] = "android"
            # 跳过初始化
            caps["skipDeviceInitialization"] = True
            # 包名+启动页名
            caps["deviceName"] = "127.0.0.1:7555"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["noReset"] = "True"
            caps["ensureWebviewsHavePages"] = True
            # 动态的设置caps参数
            # caps['settings[waitForIdleTimeout]'] = 0
            # 与server建立连接，并打开caps配置的页面
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(5)
        else:
            print("复用driver")
            # 启动app
            self.driver.launch_app()

        return self # return self，可再调用当前模块的其他方法

    def restart(self):
        # 关闭
        self.driver.close()
        # 启动app
        self.driver.launch_app()
        # self.driver.start_activity(app_package) 可启动其他app
    def stop(self):
        # 资源销毁
        self.driver.quit()

    def go_to_main(self)->MainPage: # ->指定返回的数据类型
        # 入口
        return MainPage(self.driver)