import time
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from pages.login_page import LoginPage
from utils.base_test import BaseTest
from utils.screenshot import take_screenshot


# Test case for login functionality with missing fields using pytest and page object model
@pytest.mark.usefixtures("driver")
class TestLoginMissingFields(BaseTest):

    @pytest.mark.parametrize("username,password,expected_error,error_field", [
        ("", "validpass", "Username is required", "com.saucelabs.mydemoapp.android:id/nameErrorTV"),
        ("validuser", "", "Enter Password", "com.saucelabs.mydemoapp.android:id/passwordErrorTV"),
        ("", "", "Username is required", "com.saucelabs.mydemoapp.android:id/nameErrorTV")
    ])
    def test_login_missing_fields(self, username, password, expected_error, error_field):
        try:
            login_page = LoginPage(self.driver)
            login_page.open_login_menu()
            login_page.login(username, password)

            time.sleep(2)

            error_msg = self.driver.find_element(AppiumBy.ID, error_field)

            assert error_msg.is_displayed(), f"Error message not displayed in field {error_field}"
            assert expected_error.lower() in error_msg.text.lower(), f"Expected '{expected_error}', got '{error_msg.text}'"

        except Exception:
            take_screenshot(self.driver, "login_missing_fields_failure")
            raise
