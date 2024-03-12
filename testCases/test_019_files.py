from pageObjects.BasePage import BasePage
from pageObjects.UploadAndDownloadPage import FilesPage
from utilities.readProperties import ReadConfig
import time


class Test_FilesPage:
    url = ReadConfig.getApplicationURL()

    def test_filespage(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.bp = BasePage(self.driver)
        self.bp.clickFiles()

        self.fp = FilesPage(self.driver)
        self.fp.uploadFiles()

        self.fp.excelFileDownload()
        time.sleep(1)

        self.fp.pdfFileDownload()
        time.sleep(1)

        self.fp.textFileDownload()

        time.sleep(10)


