import time

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Appium server URL
appium_server_url = "http://127.0.0.1:4723/wd/hub"

# Desired capabilities for the Android device
capabilities = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "com.android.settings",
    "appActivity": ".Settings",
    "automationName": "UiAutomator2",
    "language": "en",
    "locale": "US"
}


@pytest.fixture
def driver():
    # Initialize the Appium driver
    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    yield driver
    driver.quit()


def test_find_connected_devices(driver):
    # Wait for the "Connected devices" option to be visible and click it
    connected_devices = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@text="Connected devices"]'))
    )
    assert connected_devices.is_displayed(), "Connected devices option is not displayed"
    connected_devices.click()

    # Take a screenshot to debug the app's state
    driver.save_screenshot("before_back_button.png")

    # Wait for the "Back" button to be visible and click it
    back = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, '//android.widget.ImageButton[@content-desc="Back"]'))
    )
    back.click()
    assert back.is_displayed(), "Back button is not displayed after clicking it"


def test_find_battery_and_app_notification(driver):
    el = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')

    assert el.is_displayed(), "Battery option is not displayed"
    el.click()
    time.sleep(5)
    # Take a screenshot to debug the app's state
    driver.save_screenshot("before_back_button.png")
    back = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, '//android.widget.ImageButton[@content-desc="Back"]')))

    assert back.is_displayed(), "Back button is not displayed"
    back.click()
    time.sleep(5)
    el2 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@text="Apps & notifications"]'))
    )
    el2.click()
