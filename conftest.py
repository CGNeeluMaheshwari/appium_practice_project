import json
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options


@pytest.fixture(scope="class")
def driver(request):
    # Load capabilities from the JSON file
    with open("config/capabilities.json") as f:
        caps = json.load(f)

    # Convert JSON capabilities to UiAutomator2Options
    options = UiAutomator2Options()
    # The UiAutomator2Options object is created, and the capabilities from the JSON file are dynamically set using setattr.
    for key, value in caps.items():
        setattr(options, key, value)

    # Ensure appActivity and appWaitActivity are set correctly
    options.app_activity = "com.saucelabs.mydemoapp.android.view.activities.SplashActivity"
    options.app_wait_activity = "com.saucelabs.mydemoapp.android.view.activities.*"

    # Initialize the Appium driver
    driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)
    request.cls.driver = driver
    yield
    driver.quit()
