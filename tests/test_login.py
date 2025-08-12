# tests/test_login.py

import unittest
import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from pages.home_page import HomePage
from utils.screenshot_utils import ScreenshotManager

class LoginTest(unittest.TestCase):
    def setUp(self):
        # Setup Chrome options for cleaner output (optional)
        chrome_options = Options()
        chrome_options.add_argument("--disable-logging")
        chrome_options.add_argument("--log-level=3")
        
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.get("https://automationexercise.com/")
        self.driver.maximize_window()
        
        # Initialize screenshot manager for this test class
        self.screenshot_manager = ScreenshotManager(self.driver, "LoginTest")

    def test_invalid_login(self):
        # Test invalid login
        try:
            login = LoginPage(self.driver)
            
            # Capture screenshot before test
            self.screenshot_manager.capture_step_screenshot("before_invalid_login_test")
            
            login.go_to_login_page()
            
            # Capture screenshot after navigating to login page
            self.screenshot_manager.capture_step_screenshot("login_page_loaded")
            
            login.login("invalid@example.com", "wrongpassword")
            
            # Capture screenshot after login attempt
            self.screenshot_manager.capture_step_screenshot("after_invalid_login_attempt")
            
            warning = login.get_warning()
            self.assertIn("Your email or password is incorrect!", warning)
            
            print("✅ Invalid login test completed successfully")
            
        except Exception as e:
            # Capture screenshot on failure
            self.screenshot_manager.capture_failure_screenshot("test_invalid_login")
            raise
    
    def test_logout_user(self):
        # Logout User
        try:
            home = HomePage(self.driver)
            login = LoginPage(self.driver)
            
            print("\n=== Starting Test Case 4: Logout User ===")
            
            # Capture screenshot at start
            self.screenshot_manager.capture_step_screenshot("test_start_homepage")
            
            # Verify that home page is visible successfully
            self.assertTrue(home.is_home_page_visible(), 
                           "Home page is not visible")
            print("✅ Home page is visible successfully")
            
            # Click on 'Signup / Login' button
            home.click_signup_login()
            print("✅ Clicked on 'Signup / Login' button")
            
            # Small wait for page load
            time.sleep(1)
            
            # Capture screenshot after navigation
            self.screenshot_manager.capture_step_screenshot("signup_login_page_loaded")
            
            # Verify 'Login to your account' is visible
            self.assertTrue(login.is_login_to_account_visible(), 
                           "'Login to your account' text is not visible")
            print("✅ 'Login to your account' is visible")
            
            # Enter correct email address and password
            test_email = "huilek@example.com"
            test_password = "correctpassword"
            
            print(f"✅ Entering email: {test_email}")
            print("✅ Entering password: [hidden]")
            
            # Click 'login' button
            login.login(test_email, test_password)
            print("✅ Clicked 'login' button")
            
            # Small wait for login process
            time.sleep(2)
            
            # Capture screenshot after login
            self.screenshot_manager.capture_step_screenshot("after_login_attempt")
            
            # Verify that 'Logged in as username' is visible
            self.assertTrue(login.is_logged_in_visible(), 
                           "'Logged in as username' is not visible")
            
            logged_in_text = login.get_logged_in_text()
            print(f"✅ '{logged_in_text}' is visible")
            
            # Capture screenshot when logged in
            self.screenshot_manager.capture_step_screenshot("logged_in_successfully")
            
            # Click 'Logout' button
            login.click_logout()
            print("✅ Clicked 'Logout' button")
            
            # Small wait for logout process
            time.sleep(1)
            
            # Capture screenshot after logout
            self.screenshot_manager.capture_step_screenshot("after_logout")
            
            # Verify that user is navigated to login page
            self.assertTrue(login.is_login_page_loaded(), 
                           "User is not navigated to login page")
            print("✅ User is navigated to login page")
            
            print("🎉 SUCCESS: Logout user test completed!")
            
        except Exception as e:
            # Capture screenshot on failure
            self.screenshot_manager.capture_failure_screenshot("test_logout_user")
            raise
    
    def test_valid_login_only(self):
        # Just test valid login without logout
        try:
            home = HomePage(self.driver)
            login = LoginPage(self.driver)
            
            # Capture screenshot at start
            self.screenshot_manager.capture_step_screenshot("valid_login_test_start")
            
            # Navigate to login
            home.click_signup_login()
            time.sleep(1)
            
            # Capture screenshot after navigation
            self.screenshot_manager.capture_step_screenshot("navigated_to_login")
            
            # Verify login page
            self.assertTrue(login.is_login_to_account_visible())
            
            # Login with valid credentials
            login.login("huilek@example.com", "correctpassword")
            time.sleep(2)
            
            # Capture screenshot after login attempt
            self.screenshot_manager.capture_step_screenshot("after_valid_login")
            
            # Verify login success
            self.assertTrue(login.is_logged_in_visible())
            print("✅ Valid login successful")
            
        except Exception as e:
            # Capture screenshot on failure
            self.screenshot_manager.capture_failure_screenshot("test_valid_login_only")
            raise

    
    # def test_force_fail_example(self):
    #     """Intentional failure test to demonstrate screenshot capture"""
    #     try:
    #         # Capture screenshot before failure
    #         self.screenshot_manager.capture_step_screenshot("before_forced_failure")
            
    #         # Navigate to some page to make it more interesting
    #         home = HomePage(self.driver)
    #         home.click_signup_login()
    #         time.sleep(1)
            
    #         # Capture screenshot of the current state
    #         self.screenshot_manager.capture_step_screenshot("at_signup_login_page")
            
    #         # This will definitely fail
    #         self.fail("Forced failure for screenshot test - This demonstrates automatic screenshot capture!")
            
    #     except Exception as e:
    #         # Capture screenshot on failure
    #         self.screenshot_manager.capture_failure_screenshot("test_force_fail_example")
    #         raise

    def tearDown(self):
        time.sleep(1)  # Brief pause to see results
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()