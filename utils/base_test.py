import pytest
from appium.webdriver.common.appiumby import AppiumBy


@pytest.mark.usefixtures("driver")
class BaseTest:

    def scroll_down(driver):
        """Scroll down in the app."""
        driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true)).scrollForward()'
        )

    def scroll_up(driver):
        """Scroll up in the app."""
        driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true)).scrollBackward()'
        )

    def scroll_to_element_by_accessibility_id(self, accessibility_id):
        """Scroll to an element with the specified ACCESSIBILITY_ID."""
        return self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiScrollable(new UiSelector().scrollable(true)).'
            f'scrollIntoView(new UiSelector().description("{accessibility_id}"))'
        )


# import json
# import pytest
# from appium import webdriver
#
#
# @pytest.fixture(scope="class")
# def init_driver(request):
#     with open("config/capabilities.json") as f:
#         caps = json.load(f)
#     driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
#     request.cls.driver = driver
#     yield
#     driver.quit()

