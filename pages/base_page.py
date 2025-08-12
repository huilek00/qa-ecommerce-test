# pages/base_page.py

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import TimeoutException, NoAlertPresentException
from utils.screenshot_utils import ScreenshotManager

class BasePage:
    def __init__(self, driver, test_name="BasePage"):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.screenshot_manager = ScreenshotManager(driver, test_name)

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def enter_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.send_keys(text)
    
    def clear_and_enter_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_visible(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.is_displayed()

    def select_dropdown(self, locator, value):
        dropdown = self.wait.until(EC.visibility_of_element_located(locator))
        Select(dropdown).select_by_visible_text(value)
    
    def is_present(self, locator, timeout=10):
        # Check if element is present in DOM (not necessarily visible)
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def wait_for_alert(self, timeout=10):
        # Wait for alert to appear and return it
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.alert_is_present())
        except TimeoutException:
            return None
    
    def handle_alert(self, action="accept"):
        """Handle JavaScript alert
        Args:
            action (str): 'accept' to click OK, 'dismiss' to click Cancel
        """
        try:
            alert = self.wait_for_alert()
            if alert:
                if action == "accept":
                    alert.accept()
                else:
                    alert.dismiss()
                return True
        except (TimeoutException, NoAlertPresentException):
            pass
        return False
    
    def capture_screenshot(self, step_name):
        # Capture screenshot for debugging
        return self.screenshot_manager.capture_step_screenshot(step_name)