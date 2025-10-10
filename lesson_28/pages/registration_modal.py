from selenium.webdriver.common.by import By
from .base_page import BasePage


class RegistrationModal(BasePage):
    NAME_INPUT = (By.ID, "signupName")
    LAST_NAME_INPUT = (By.ID, "signupLastName") 
    EMAIL_INPUT = (By.ID, "signupEmail")
    PASSWORD_INPUT = (By.ID, "signupPassword")
    REPEAT_PASSWORD_INPUT = (By.ID, "signupRepeatPassword")
    REGISTER_BUTTON = (By.XPATH, "//button[@class='btn btn-primary' and text()='Register']")
    CLOSE_BUTTON = (By.XPATH, "//button[@class='close']")
    
    NAME_ERROR = (By.XPATH, "//input[@id='signupName']/../div[contains(@class, 'invalid-feedback')]")
    LAST_NAME_ERROR = (By.XPATH, "//input[@id='signupLastName']/../div[contains(@class, 'invalid-feedback')]")
    EMAIL_ERROR = (By.XPATH, "//input[@id='signupEmail']/../div[contains(@class, 'invalid-feedback')]")
    PASSWORD_ERROR = (By.XPATH, "//input[@id='signupPassword']/../div[contains(@class, 'invalid-feedback')]")
    REPEAT_PASSWORD_ERROR = (By.XPATH, "//input[@id='signupRepeatPassword']/../div[contains(@class, 'invalid-feedback')]")
    
    def get_name_input(self):
        return self.find_element(self.NAME_INPUT)
    
    def get_last_name_input(self):
        return self.find_element(self.LAST_NAME_INPUT)
    
    def get_email_input(self):
        return self.find_element(self.EMAIL_INPUT)
    
    def get_password_input(self):
        return self.find_element(self.PASSWORD_INPUT)
    
    def get_repeat_password_input(self):
        return self.find_element(self.REPEAT_PASSWORD_INPUT)
    
    def get_register_button(self):
        return self.find_element(self.REGISTER_BUTTON)
    
    def get_register_button_clickable(self):
        return self.find_clickable_element(self.REGISTER_BUTTON)
    
    def get_close_button(self):
        return self.find_clickable_element(self.CLOSE_BUTTON)
    
    def get_name_error(self):
        return self.find_element(self.NAME_ERROR)
    
    def get_last_name_error(self):
        return self.find_element(self.LAST_NAME_ERROR)
    
    def get_email_error(self):
        return self.find_element(self.EMAIL_ERROR)
    
    def get_password_error(self):
        return self.find_element(self.PASSWORD_ERROR)
    
    def get_repeat_password_error(self):
        return self.find_element(self.REPEAT_PASSWORD_ERROR)