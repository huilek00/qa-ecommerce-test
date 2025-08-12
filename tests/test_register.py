# tests/test_register.py

import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.register_page import RegisterPage


class TestRegisterUser(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.get("https://automationexercise.com/")

    def test_register_user(self):
        register = RegisterPage(self.driver)

        # Verify home page visible
        self.assertTrue(register.is_home_page_visible())

        # Click on 'Signup / Login' button
        register.go_to_signup_page()

        # Verify 'New User Signup!' is visible
        self.assertTrue(register.is_new_user_signup_visible())

        # Enter name, email, click 'Signup'
        # Use timestamp to create unique email
        unique_email = f"testuser{int(time.time())}@example.com"
        register.enter_name_email("Test User", unique_email)
        register.click_signup_button()

        # Add a small wait to let the page load
        time.sleep(2)

        # Verify 'ENTER ACCOUNT INFORMATION' is visible
        self.assertTrue(register.is_account_info_visible())

        # Fill account details
        register.fill_account_details(
            title="Mr",
            password="password123",
            day="1", month="January", year="2000",
            first_name="Test", last_name="User",
            company="Test Company", address1="123 Test Street",
            address2="Suite 100", country="Canada",
            state="Ontario", city="Toronto",
            zipcode="M5A 1A1", mobile_number="1234567890"
        )

        # Click 'Create Account'
        register.click_create_account()

        # Verify 'ACCOUNT CREATED!' is visible
        self.assertTrue(register.is_account_created_visible())

        # Click 'Continue'
        register.click_continue()

        # Verify 'Logged in as username' is visible
        self.assertTrue(register.is_logged_in_as_visible())

        # Click 'Delete Account'
        register.delete_account()

        # Verify 'ACCOUNT DELETED!' is visible
        self.assertTrue(register.is_account_deleted_visible())

        # Click 'Continue' after delete
        register.click_continue_after_delete()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()