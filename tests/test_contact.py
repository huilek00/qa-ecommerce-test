# tests/test_contact.py

import unittest
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.contact_page import ContactPage


class TestContactUs(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        # Launch browser and navigate to URL
        self.driver.get("http://automationexercise.com")

    def test_contact_us_form(self):
        contact = ContactPage(self.driver)

        # Verify that home page is visible successfully
        self.assertTrue(contact.is_home_page_visible(), "Home page is not visible")

        # Click on 'Contact Us' button
        contact.click_contact_us()

        # Verify 'GET IN TOUCH' is visible
        self.assertTrue(contact.is_get_in_touch_visible(), "'GET IN TOUCH' text is not visible")

        # Enter name, email, subject and message
        contact.fill_contact_form(
            name="Test User",
            email="testuser@example.com",
            subject="Test Subject",
            message="This is a test message for contact form automation testing."
        )

        # Upload file
        # Create a simple test file if it doesn't exist
        test_file_path = self.create_test_file()
        contact.upload_file(test_file_path)

        # Click 'Submit' button
        contact.click_submit_button()

        # Click OK button (handle alert)
        alert_handled = contact.handle_alert()
        self.assertTrue(alert_handled, "Alert was not found or handled")

        # Small wait for page to process
        time.sleep(2)

        # Verify success message is visible
        self.assertTrue(contact.is_success_message_visible(), 
                       "Success message 'Success! Your details have been submitted successfully.' is not visible")

        # Click 'Home' button and verify that landed to home page successfully
        contact.click_home_button()
        self.assertTrue(contact.verify_back_to_home(), "Did not land back to home page successfully")

        # Clean up test file
        self.cleanup_test_file(test_file_path)

    def create_test_file(self):
        # Create a simple test file for upload
        test_file_path = os.path.join(os.getcwd(), "test_upload_file.txt")
        with open(test_file_path, 'w') as f:
            f.write("This is a test file for contact form upload.\n")
            f.write("Created for automation testing purposes.")
        return test_file_path

    def cleanup_test_file(self, file_path):
        # Remove the test file after test completion
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f"Could not delete test file: {e}")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()