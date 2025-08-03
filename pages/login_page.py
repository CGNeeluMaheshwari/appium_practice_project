from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        """Initializes the LoginPage with the Appium driver."""
        self.driver = driver
        self.menu_button = (AppiumBy.ACCESSIBILITY_ID, "View menu")  # "com.saucelabs.mydemoapp.android:id/menuIV"
        self.login_menu_item = (AppiumBy.ACCESSIBILITY_ID, "Login Menu Item")
        self.username_field = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/nameET")
        self.password_field = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/passwordET")
        self.login_button = (AppiumBy.ACCESSIBILITY_ID, "Tap to login with given credentials")
        self.twitter = (AppiumBy.ACCESSIBILITY_ID, "test-Twitter"),
        self.facebook = (AppiumBy.ACCESSIBILITY_ID, "test-Facebook"),
        self.linkedIn = (AppiumBy.ACCESSIBILITY_ID, "test-LinkedIn")


    def open_login_menu(self):
        self.driver.find_element(*self.menu_button).click()
        self.driver.find_element(*self.login_menu_item).click()  # Click on the login menu item

    def login(self, username, password):
        wait = WebDriverWait(self.driver, 10)  # Wait up to 10 seconds for elements to appear
        wait.until(EC.presence_of_element_located(self.username_field)).send_keys(username)
        wait.until(EC.presence_of_element_located(self.password_field)).send_keys(password)
        wait.until(EC.element_to_be_clickable(self.login_button)).click()
