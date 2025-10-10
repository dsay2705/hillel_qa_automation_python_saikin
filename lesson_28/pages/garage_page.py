from selenium.webdriver.common.by import By
from .base_page import BasePage


class GaragePage(BasePage):
    ADD_CAR_BUTTON = (By.XPATH, "//button[contains(text(), 'Add car')]")
    GARAGE_TITLE = (By.XPATH, "//h1[text()='Garage']")
    
    def get_add_car_button(self):
        return self.find_element(self.ADD_CAR_BUTTON)
    
    def get_garage_title(self):
        return self.find_element(self.GARAGE_TITLE)