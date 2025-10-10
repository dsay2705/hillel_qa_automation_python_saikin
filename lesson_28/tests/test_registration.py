import pytest
# pytest_plugins = "pytest_assume"


class TestUserRegistration:
    
    def test_successful_user_registration(
        self, 
        main_page, 
        registration_modal,
        garage_page,
        open_registration_modal,
        fill_registration_form,
        click_register_button
    ):
        fill_registration_form()
        click_register_button()
        
        garage_title = garage_page.get_garage_title()
        pytest.assume(garage_title.is_displayed(), "Garage title not found")
        pytest.assume("Garage" in garage_title.text, "No 'Garage' in title")
        
        add_car_button = garage_page.get_add_car_button()
        pytest.assume(add_car_button.is_displayed(), "No 'Add car' button")
    
    def test_registration_with_invalid_name(
        self,
        registration_modal,
        open_registration_modal,
        clear_registration_form,
        fill_registration_form
    ):
        clear_registration_form()
        fill_registration_form(name="2705")
        
        name_error = registration_modal.get_name_error()
        pytest.assume(name_error.is_displayed(), "Name validation error not displayed")
        pytest.assume("Name is invalid" in name_error.text, "Name error text not correct")
        
        name_input = registration_modal.get_name_input()
        input_classes = name_input.get_attribute("class")
        pytest.assume("is-invalid" in input_classes, "Name field should have is-invalid class")
    
    def test_registration_with_short_last_name(
        self,
        registration_modal,
        open_registration_modal,
        clear_registration_form,
        fill_registration_form
    ):
        clear_registration_form()
        fill_registration_form(last_name="S")
        
        last_name_error = registration_modal.get_last_name_error()
        pytest.assume(last_name_error.is_displayed(), "Last name validation error not displayed")
        pytest.assume("Last name has to be from 2 to 20 characters long" in last_name_error.text, "Last name error text not correct")
        
        last_name_input = registration_modal.get_last_name_input()
        input_classes = last_name_input.get_attribute("class")
        pytest.assume("is-invalid" in input_classes, "Last name field should have is-invalid class")
    
    def test_registration_with_invalid_email(
        self,
        registration_modal,
        open_registration_modal,
        clear_registration_form,
        fill_registration_form
    ):
        clear_registration_form()
        fill_registration_form(email="invalid-email")
        
        email_error = registration_modal.get_email_error()
        pytest.assume(email_error.is_displayed(), "Email validation error not displayed")
        pytest.assume("Email is incorrect" in email_error.text, "Email error text not correct")
        
        email_input = registration_modal.get_email_input()
        input_classes = email_input.get_attribute("class")
        pytest.assume("is-invalid" in input_classes, "Email field should have is-invalid class")
    
    def test_registration_with_mismatched_passwords(
        self,
        registration_modal,
        open_registration_modal,
        clear_registration_form,
        fill_registration_form
    ):
        clear_registration_form()
        fill_registration_form(password="Password123", repeat_password="DiffPassword123")
        
        name_input = registration_modal.get_name_input()
        name_input.click()
        
        register_button = registration_modal.get_register_button()
        pytest.assume(not register_button.is_enabled(), "Register button not disabled")
        
        repeat_password_error = registration_modal.get_repeat_password_error()
        pytest.assume(repeat_password_error.is_displayed(), "Repeat password validation error not displayed")
        pytest.assume("Passwords do not match" in repeat_password_error.text, "Repeat password error text not correct")
        
        repeat_password_input = registration_modal.get_repeat_password_input()
        input_classes = repeat_password_input.get_attribute("class")
        pytest.assume("is-invalid" in input_classes, "Repeat password field should have is-invalid class")
    
    def test_registration_with_short_password(
        self,
        registration_modal,
        open_registration_modal,
        clear_registration_form,
        fill_registration_form
    ):
        clear_registration_form()
        fill_registration_form(password="27", repeat_password="27")
        
        password_error = registration_modal.get_password_error()
        pytest.assume(password_error.is_displayed(), "No password validation error")
        expected_text = ("Password has to be from 8 to 15 characters long and contain "
                        "at least one integer, one capital, and one small letter")
        pytest.assume(expected_text in password_error.text, "Password error text not correct")
        
        password_input = registration_modal.get_password_input()
        input_classes = password_input.get_attribute("class")
        pytest.assume("is-invalid" in input_classes, "Password field should have is-invalid class")
    
    def test_empty_registration_form_validation(
        self,
        registration_modal,
        open_registration_modal
    ):
        register_button = registration_modal.get_register_button()
        pytest.assume(register_button.is_displayed(), "Register button should be visible")
        pytest.assume(not register_button.is_enabled(), "Register button should be disabled")
        
        name_input = registration_modal.get_name_input()
        name_input.click()
        last_name_input = registration_modal.get_last_name_input()
        last_name_input.click()
        
        name_error = registration_modal.get_name_error()
        pytest.assume(name_error.is_displayed(), "Name validation error not displayed for empty field")
        pytest.assume("Name required" in name_error.text, "Name error text not correct")
        
        email_input = registration_modal.get_email_input()
        email_input.click()
        
        last_name_error = registration_modal.get_last_name_error()
        pytest.assume(last_name_error.is_displayed(), "Last name validation error not displayed for empty field")
        pytest.assume("Last name required" in last_name_error.text, "Last name error text not correct")
        
        password_input = registration_modal.get_password_input()
        password_input.click()
        
        email_error = registration_modal.get_email_error()
        pytest.assume(email_error.is_displayed(), "Email validation error not displayed for empty field")
        pytest.assume("Email required" in email_error.text, "Email error text not correct")
        
        repeat_password_input = registration_modal.get_repeat_password_input()
        repeat_password_input.click()
        
        password_error = registration_modal.get_password_error()
        pytest.assume(password_error.is_displayed(), "Password validation error not displayed for empty field")
        pytest.assume("Password required" in password_error.text, "Password error text not correct")
        
        name_input.click()
        
        repeat_password_error = registration_modal.get_repeat_password_error()
        pytest.assume(repeat_password_error.is_displayed(), "Repeat password validation error not displayed for empty field")
        pytest.assume("Re-enter password required" in repeat_password_error.text, "Repeat password error text not correct")

    def test_registration_modal_close_button(
        self,
        main_page,
        registration_modal,
        open_registration_modal,
        close_registration_modal
    ):
        name_input = registration_modal.get_name_input()
        pytest.assume(name_input.is_displayed(), "Registration modal not opened")
        
        close_registration_modal()
        
        sign_up_button = main_page.get_sign_up_button()
        pytest.assume(sign_up_button.is_displayed(), "Modal not closed")