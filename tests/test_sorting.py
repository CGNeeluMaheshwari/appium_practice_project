import time

import pytest
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.base_test import BaseTest
from utils.data_reader import read_excel


# Test case for sorting items in the inventory using pytest and page object model
class TestSorting(BaseTest):
    def login_user(self, username, password):
        """Reusable method to log in the user."""
        login_page = LoginPage(self.driver)
        login_page.open_login_menu()
        login_page.login(username, password)

    @pytest.mark.parametrize("username,password", read_excel("data/testdata.xlsx", "Sheet1"))
    def test_sort_items_asc_by_name(self, username, password):
        self.login_user(username, password)
        time.sleep(2)
        inventory = InventoryPage(self.driver)
        inventory.sort_asc_by_name()
        self.scroll_down()
        item_names = inventory.get_item_names()
        assert item_names == sorted(item_names), f"Items not sorted alphabetically ascending: {item_names}"
        print("Items sorted in ascending order by name successfully.")

        # items to be sorted in descending order by name
        inventory.sort_dsc_by_name()
        self.scroll_down()
        item_names = inventory.get_item_names()
        assert item_names == sorted(item_names,
                                    reverse=True), f"Items not sorted alphabetically descending: {item_names}"
        print("Items sorted in descending order by name successfully.")

        # items to be sorted in ascending order by price
        inventory.sort_asc_by_price()
        self.scroll_down()
        item_prices = inventory.get_item_prices()
        assert item_prices == sorted(item_prices), f"Items not sorted by price ascending: {item_prices}"
        print("Items sorted in ascending order by price successfully.")

        # items to be sorted in descending order by price
        inventory.sort_dsc_by_price()
        self.scroll_down()
        item_prices = inventory.get_item_prices()
        assert item_prices == sorted(item_prices, reverse=True), f"Items not sorted by price descending: {item_prices}"
        print("Items sorted in descending order by price successfully.")
