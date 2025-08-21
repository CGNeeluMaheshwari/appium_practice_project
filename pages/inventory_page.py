from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds for elements
        self.sort_button = (AppiumBy.ACCESSIBILITY_ID, "Shows current sorting order and displays available sorting options")
        self.sort_name_asc = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Name - Ascending")')
        self.sort_name_dsc = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Name - Descending")')
        self.sort_price_asc = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Price - Ascending")')
        self.sort_price_dsc = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Price - Descending")')
        self.item_names = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/titleTV")
        self.item_prices = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/priceTV")

    def open_sort_menu(self):
        self.wait.until(EC.element_to_be_clickable(self.sort_button)).click()

    def sort_asc_by_name(self):
        self.open_sort_menu()
        self.wait.until(EC.element_to_be_clickable(self.sort_name_asc)).click()

    def sort_dsc_by_name(self):
        self.open_sort_menu()
        self.wait.until(EC.element_to_be_clickable(self.sort_name_dsc)).click()

    def sort_asc_by_price(self):
        self.open_sort_menu()
        self.wait.until(EC.element_to_be_clickable(self.sort_price_asc)).click()

    def sort_dsc_by_price(self):
        self.open_sort_menu()
        self.wait.until(EC.element_to_be_clickable(self.sort_price_dsc)).click()

    def get_item_names(self):
        return [el.text for el in self.wait.until(EC.presence_of_all_elements_located(self.item_names))]

    def get_item_prices(self):
        return [float(el.text.replace("$ ", "").strip()) for el in self.wait.until(EC.presence_of_all_elements_located(self.item_prices))]