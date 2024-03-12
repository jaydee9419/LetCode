import os.path

from pageObjects.BasePage import BasePage
from pageObjects.EditPage import EditPage
from utilities.readProperties import ReadConfig
import time


class Test_EditForm:
    url = ReadConfig.getApplicationURL()

    def test_editform(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.bp = BasePage(self.driver)
        self.bp.clickEdit()

        self.ep = EditPage(self.driver)
        self.ep.setName()

        value = self.ep.getValue()
        if value == "ortonikc":
            print(value)
            assert True
        else:
            print("Test case failed: Value is not matching")
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\editpage.png")
            assert False

        self.ep.clearData()
        status = self.ep.ckeckEnableStatus()
        print(status)
        self.driver.quit()


