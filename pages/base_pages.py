from utils.mobile_utils import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class BasePages:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def page_locator(self, locator):
        return (By.XPATH, locator)

    # CLICK
    def click(self, locator):
        return click_element(self.driver, locator)

    # TEXT INPUT
    def type(self, locator, text):
        return input_text(self.driver, locator, text)

    # GET TEXT / NAME
    def get_text(self, locator):
        return get_text_element(self.driver, locator)
    
    def get_value(self, locator):
        return get_value_element(self.driver, locator)

    # VERIFY VISIBLE
    def should_be_visible(self, locator):
        return is_element_visible(self.driver, locator)

    # SCROLL TO ELEMENT
    def scroll_to(self, locator):
        return scroll_to_element(self.driver, locator)

    # CHECK IF ELEMENT VISIBLE → True/False (tanpa fail)
    def is_visible(self, locator):
        try:
            is_element_visible(self.driver, locator)
            return True
        except:
            return False
    
    def upload_first_image(self):
        return select_first_photo(self.driver)
    
    def press_action_keyboard(self):
        return press_keyboard_action(self.driver)
