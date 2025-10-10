from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage):
    SIGN_UP_BUTTON = (By.XPATH, "//button[contains(text(), 'Sign up')]")
    
    def get_sign_up_button(self):
        return self.find_clickable_element(self.SIGN_UP_BUTTON)