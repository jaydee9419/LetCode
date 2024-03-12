from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class ShadowDOMPage:
    host_fname_id = "open-shadow"
    input_fname_css = "#fname"

    host_lname_class = "field"
    input_lname_css = "#lname"

    host = "close-shadow"
    input= "email"


    def __init__(self, driver):
        self.driver = driver

    def set_fname(self):

        # # Method1:
        # # Find the host element of the Shadow DOM
        # host_element = self.driver.find_element(By.ID, self.host_fname_id)
        #
        # # Execute JavaScript to access the Shadow DOM
        # shadow_dom_script = "return arguments[0].shadowRoot"
        # shadow_dom = self.driver.execute_script(shadow_dom_script, host_element)
        #
        # # Now you can locate elements within the Shadow DOM using regular WebDriver methods
        # shadow_element = shadow_dom.find_element(By.CSS_SELECTOR, self.input_fname_css)
        # shadow_element.send_keys("Rakesh")

        # method2:
        element = "return document.querySelector('#open-shadow').shadowRoot.querySelector('#fname')"
        fname = self.driver.execute_script(element)
        fname.send_keys("Rakesh")


    def set_lname(self):
        element = "return document.querySelector('my-web-component').myRoot.querySelector('#lname').value='Mara'"
        self.driver.execute_script(element)

    def set_email(self):
        close_shadow = self.driver.find_element(By.ID, 'close-shadow')
        email_input = close_shadow.find_element(By.ID, 'email')
        if close_shadow and email_input:
            self.driver.execute_script("arguments[0].value = 'rakesh.mara@gmail.com';", email_input)
        else:
            print("Elements not found.")






