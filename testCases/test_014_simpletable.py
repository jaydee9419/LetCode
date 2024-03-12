from pageObjects.BasePage import BasePage
from pageObjects.SimpleTablePage import SampleTablePage
from utilities.readProperties import ReadConfig
import time


class Test_SliderPage:
    url = ReadConfig.getApplicationURL()

    def test_sliderpage(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.bp = BasePage(self.driver)
        self.bp.clickSimpleTable()

        self.stp = SampleTablePage(self.driver)
        totals = self.stp.getTableTotalValues()
        if totals == 858:
            print(totals)
            assert True
        else:
            print(totals)
            assert False

        names = self.stp.getName()

        if "Koushik Chatterjee" in names:
            print("Name found: Koushik Chatterjee")
            assert True
        else:
            print("Name not found: Koushik Chatterjee")
            assert False

        # Optional: Add a short delay if needed
        time.sleep(2)

        self.stp.sortingTableData()
        time.sleep(10)
