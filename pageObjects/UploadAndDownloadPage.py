from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os

class FilesPage:
    file_upload_xpath = "//input[@type='file']"
    file_excel_link = "Download Excel"
    file_pdf_link = "Download Pdf"
    file_text_link = "Download Text"

    def __init__(self, driver):
        self.driver = driver

    def uploadFiles(self):
        file_path = "D:\\Work_Environment\\Python\\Udemy\\Automation_Framework\\LetCode\\testdata\\sample.xlsx"
        upload = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.file_upload_xpath))
        )
        upload.send_keys(file_path)
        print("File uploaded successfully")

    def excelFileDownload(self):
        excel = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, self.file_excel_link))
        )
        excel.click()

    def pdfFileDownload(self):
        pdf = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, self.file_pdf_link))
        )
        pdf.click()

    def textFileDownload(self):
        text = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, self.file_text_link))
        )
        text.click()


