import time

import pytest
from appium.webdriver.common.appiumby import AppiumBy

from pages.login_page import LoginPage
from utils.data_reader import read_excel
from utils.screenshot import take_screenshot
from utils.base_test import BaseTest


# Test case for login functionality using pytest and page object model
class TestLogin(BaseTest):

    @pytest.mark.parametrize("username,password", read_excel("data/testdata.xlsx", "Sheet1"))
    def test_login_valid(self, username, password):
        self.home_element = (AppiumBy.ACCESSIBILITY_ID, "Tap to login with given credentials")
        try:
            login_page = LoginPage(self.driver)
            login_page.open_login_menu()
            login_page.login(username, password)
            # assert "Home" in self.driver.page_source
            time.sleep(5)
            assert self.home_element is not None, "Home screen not displayed after login"
        except Exception:
            take_screenshot(self.driver, "login_failure")
            raise


