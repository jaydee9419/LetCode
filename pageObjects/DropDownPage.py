from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select


class DropDownPage:
    lst_fruits_xpath = "//select[@id='fruits']"
    lst_heros_xpath = "//select[@id='superheros']"
    lst_language_xpath = "//select[@id='lang']"
    lst_country_xpath = "//select[@id='country']"

    def __init__(self, driver):
        self.driver = driver

    def selectFruit(self):
        fruits = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.lst_fruits_xpath))
        )
        apple = Select(fruits)
        apple.select_by_visible_text("Apple")

    def selectHeros(self):
        heros = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.lst_heros_xpath))
        )
        hero = Select(heros)
        hero.select_by_index(0)
        hero.select_by_index(1)
        hero.select_by_index(2)
        hero.select_by_index(3)

    def selectLanguage(self):
        language = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.lst_language_xpath))
        )
        python = Select(language)
        python.select_by_value("py")

    def getCountries(self):
        countries = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.lst_country_xpath))
        )
        country = Select(countries)
        all_countries = country.options

        for item in all_countries:
            print(item.text)




