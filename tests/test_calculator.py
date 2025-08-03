import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
import time


@pytest.fixture
def driver():
    # Set up Appium options
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "Pixel5"
    options.app = "C:/Users/nmaheshw/app/com.hp.primecalculator.free.2.1.apk"
    options.automation_name = "UiAutomator2"
    options.app_wait_activity = "com.hp.primecalculator.activity.*,com.hp.primecalculator.*" # If the app has a splash screen or multiple activities during startup, specify the appWaitActivity to include all possible activities
    options.auto_grant_permissions = True
    options.app_wait_duration = 30000  # If the app takes time to load, increase the appWaitDuration

    # Connect to Appium server
    driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", options=options)
    yield driver
    driver.quit()


def test_install_and_uninstall_app(driver):
    # Wait for the app to launch
    time.sleep(5)
    print("App launched successfully")
    assert driver.is_app_installed("com.hp.primecalculator.free"), "App is not installed"

    # Check if the app is installed then uninstall it
    app_package = "com.hp.primecalculator.free"
    # driver.remove_app(app_package)

    if driver.is_app_installed(app_package):
        driver.remove_app(app_package)
        print("App uninstalled successfully")
        assert not driver.is_app_installed(app_package), "App is still installed"
    else:
        print("App is not installed")
