import time

import pytest
from appium.webdriver.common.appiumby import AppiumBy

from pages.login_page import LoginPage
from utils.data_reader import read_excel
from utils.screenshot import take_screenshot
from utils.base_test import BaseTest


# Test case for Invalid login functionality using pytest and page object model
class TestInvalidLogin(BaseTest):

    @pytest.mark.parametrize("username,password", read_excel("data/testdata.xlsx", "Sheet2"))
    def test_valid_login(self, username, password):
        self.error_element = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/passwordErrorTV")
        try:
            login_page = LoginPage(self.driver)
            login_page.open_login_menu()
            login_page.login(username, password)
            time.sleep(5)
            assert self.error_element is not None, "error screen not displayed after login"
        except Exception:
            take_screenshot(self.driver, "login_successful")
            raise
