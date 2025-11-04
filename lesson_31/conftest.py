import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.main_page import MainPage
from pages.registration_modal import RegistrationModal
from pages.garage_page import GaragePage
import time


@pytest.fixture
def browser():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def navigate_to_site(browser):
    url = "https://guest:welcome2qauto@qauto2.forstudy.space/"
    browser.get(url)
    time.sleep(2)
    return browser


@pytest.fixture
def main_page(navigate_to_site):
    return MainPage(navigate_to_site)


@pytest.fixture
def registration_modal(navigate_to_site):
    return RegistrationModal(navigate_to_site)


@pytest.fixture
def garage_page(navigate_to_site):
    return GaragePage(navigate_to_site)


@pytest.fixture
def open_registration_modal(main_page):
    sign_up_button = main_page.get_sign_up_button()
    sign_up_button.click()
    time.sleep(1)
    return main_page.driver


@pytest.fixture
def fill_registration_form(open_registration_modal, registration_modal):
    def _fill_form(name="Danylo", last_name="Saikin", email=None, password="Password2705", repeat_password=None):
        if email is None:
            timestamp = str(int(time.time()))
            email = f"danylo.saikin.{timestamp}@gmail.com"
        
        if repeat_password is None:
            repeat_password = password
            
        name_input = registration_modal.get_name_input()
        name_input.clear()
        name_input.send_keys(name)
        
        last_name_input = registration_modal.get_last_name_input()
        last_name_input.clear()
        last_name_input.send_keys(last_name)
        
        email_input = registration_modal.get_email_input()
        email_input.clear()
        email_input.send_keys(email)
        
        password_input = registration_modal.get_password_input()
        password_input.clear()
        password_input.send_keys(password)
        
        repeat_password_input = registration_modal.get_repeat_password_input()
        repeat_password_input.clear()
        repeat_password_input.send_keys(repeat_password)
        
        return {
            "name": name,
            "last_name": last_name,
            "email": email,
            "password": password,
            "repeat_password": repeat_password
        }
    
    return _fill_form


@pytest.fixture
def click_register_button(registration_modal):
    def _click():
        register_button = registration_modal.get_register_button_clickable()
        register_button.click()
        time.sleep(2)
    
    return _click


@pytest.fixture
def clear_registration_form(registration_modal):
    def _clear_form():
        fields = [
            registration_modal.get_name_input(),
            registration_modal.get_last_name_input(),
            registration_modal.get_email_input(),
            registration_modal.get_password_input(),
            registration_modal.get_repeat_password_input()
        ]
        
        for field in fields:
            field.clear()
    
    return _clear_form


@pytest.fixture
def close_registration_modal(registration_modal):
    def _close():
        close_button = registration_modal.get_close_button()
        close_button.click()
        time.sleep(1)
    
    return _close


