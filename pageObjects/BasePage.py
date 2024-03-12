import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    btn_edit_link = "Edit"
    btn_click_link = "Click"
    btn_dropdown_link = "Drop-Down"
    btn_alerts_link = "Dialog"
    btn_frames_link = "Inner HTML"
    btn_radiobuttons_link = "Toggle"
    btn_windows_link = "Tabs"
    btn_elements_link = "Find Elements"
    btn_dragdrop1_link = "AUI - 1"
    btn_dragdrop2_link = "AUI - 2"
    btn_dragdrop3_link = "AUI - 3"
    btn_dragdrop4_link = "AUI - 4"
    btn_dragdrop5_link = "AUI - 5"
    btn_simpletable_link = "Simple table"
    btn_advancetable_link = "Advance table"
    btn_calendar_xpath = "Date & Time"
    btn_wait_link = "Timeout"
    btn_files_link = "File management"
    btn_shadowdom_link = "DOM"

    def __init__(self, driver):
        self.driver = driver

    def clickEdit(self):
        edit = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, self.btn_edit_link))
        )
        edit.click()

    def clickClicks(self):
        click = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, self.btn_click_link))
        )
        click.click()

    def clickDropDown(self):
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, self.btn_dropdown_link))
        )
        dropdown.click()

    def clickAlerts(self):
        alert = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, self.btn_alerts_link))
        )
        alert.click()

    def clickFrames(self):
        frames = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, self.btn_frames_link))
        )
        frames.click()

    def clickRadioButtons(self):
        radiobutton = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, self.btn_radiobuttons_link))
        )
        radiobutton.click()

    def clickWindows(self):
        windows = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, self.btn_windows_link))
        )
        windows.click()


    def clickElements(self):
        elements = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, self.btn_elements_link))
        )
        elements.click()

    def clickDrag(self):
        drag = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, self.btn_dragdrop1_link))
        )
        drag.click()

    def clickDrop(self):
        drop = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, self.btn_dragdrop2_link))
        )
        drop.click()

    def clickSort(self):
        drop = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, self.btn_dragdrop3_link))
        )
        drop.click()

    def clickSelect(self):
        drop = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, self.btn_dragdrop4_link))
        )
        drop.click()

    def clickSlider(self):
        drop = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, self.btn_dragdrop5_link))
        )
        drop.click()

    def clickSimpleTable(self):
        drop = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, self.btn_simpletable_link))
        )
        drop.click()

    def clickAdvanceTable(self):
        drop = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, self.btn_advancetable_link))
        )
        drop.click()


    def clickCalendar(self):
        drop = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, self.btn_calendar_xpath))
        )
        drop.click()

    def clickWait(self):
        drop = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, self.btn_wait_link))
        )
        drop.click()

    def clickFiles(self):
        drop = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, self.btn_files_link))
        )
        drop.click()

    def clickShadowDOM(self):
        drop = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, self.btn_shadowdom_link))
        )
        drop.click()

