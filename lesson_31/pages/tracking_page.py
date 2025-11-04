from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..settings import settings

class TrackingPage:
    URL = settings.TRACKING_URL

    INPUT_FIELD = (By.XPATH, '//input[@class="track__form-group-input"]')
    STATUS_TEXT = (By.CSS_SELECTOR, "div.header__status-text")
    SEARCH_BUTTON = (By.ID, "np-number-input-desktop-btn-search-en")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self, url=None):
        url = url or self.URL
        self.driver.get(url)

    def enter_tracking_number(self, number):
        input_field = self.wait.until(
            EC.visibility_of_element_located(self.INPUT_FIELD)
        )
        input_field.clear()
        input_field.send_keys(number)
        input_field.send_keys(Keys.ENTER)

    def click_search_button(self):
        search_button = self.wait.until(
            EC.element_to_be_clickable(self.SEARCH_BUTTON)
        )
        search_button.click()

    def get_status(self):
        status = self.wait.until(
            EC.visibility_of_element_located(self.STATUS_TEXT)
        )
        return status.text.strip()