import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

@pytest.fixture(scope="module")
def driver():
    desired_caps = {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "app": "C:/Users/nmaheshw/app/mda-2.2.0-25.apk",
        "automationName": "UiAutomator2"
    }
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    yield driver
    driver.quit()


def test_add_item_and_checkout(driver):
    time.sleep(5)  # Wait for app to load

    # Step 1: Navigate to product list (adjust locator as needed)
    product = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                  'new UiSelector().text("Sauce Labs Backpack")')   #xpath: (//android.widget.ImageView[@content-desc="Product Image"])[1]
    product.click()

    # Step 2: Add to cart
    add_to_cart_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Tap to add product to cart")
    add_to_cart_btn.click()

    # Step 3: Go to cart
    cart_icon = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cartIV")  #xpath: //android.widget.ImageView[@content-desc="Displays number of items in your cart"]
    cart_icon.click()

    # Step 4: Proceed to checkout
    checkout_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Confirms products for checkout")
    checkout_btn.click()

    # Step 5: Verify checkout screen
    confirmation = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                       'new UiSelector().textContains("Checkout")')
    assert confirmation.is_displayed(), "Checkout screen not displayed"
