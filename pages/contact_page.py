# pages/contact_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage


class ContactPage(BasePage):
    # Locators
    HOME_SLIDER = (By.ID, "slider-carousel")  # Home page identifier
    CONTACT_US_LINK = (By.XPATH, "//a[contains(text(),'Contact us')]")
    GET_IN_TOUCH_TEXT = (By.XPATH, "//h2[contains(text(),'Get In Touch')]")
    
    # Contact form fields
    NAME_FIELD = (By.XPATH, "//input[@data-qa='name']")
    EMAIL_FIELD = (By.XPATH, "//input[@data-qa='email']")
    SUBJECT_FIELD = (By.XPATH, "//input[@data-qa='subject']")
    MESSAGE_FIELD = (By.XPATH, "//textarea[@data-qa='message']")
    FILE_UPLOAD = (By.XPATH, "//input[@name='upload_file']")
    SUBMIT_BUTTON = (By.XPATH, "//input[@data-qa='submit-button']")
    
    # Success message and navigation
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class,'status alert') and contains(text(),'Success! Your details have been submitted successfully.')]")
    HOME_BUTTON = (By.XPATH, "//a[contains(text(),'Home')]")

    # Methods
    def is_home_page_visible(self):
        # Verify that home page is visible
        return self.is_visible(self.HOME_SLIDER)

    def click_contact_us(self):
        # Click on 'Contact Us' button
        self.click(self.CONTACT_US_LINK)

    def is_get_in_touch_visible(self):
        # Verify 'GET IN TOUCH' is visible
        return self.is_visible(self.GET_IN_TOUCH_TEXT)

    def fill_contact_form(self, name, email, subject, message):
        # Enter name, email, subject and message
        self.clear_and_enter_text(self.NAME_FIELD, name)
        self.clear_and_enter_text(self.EMAIL_FIELD, email)
        self.clear_and_enter_text(self.SUBJECT_FIELD, subject)
        self.clear_and_enter_text(self.MESSAGE_FIELD, message)

    def upload_file(self, file_path):
        # Upload file
        file_input = self.wait.until(EC.presence_of_element_located(self.FILE_UPLOAD))
        file_input.send_keys(file_path)

    def click_submit_button(self):
        # Click 'Submit' button
        self.click(self.SUBMIT_BUTTON)

    def handle_alert(self):
        # Handle JavaScript alert (Click OK button)
        try:
            # Wait for alert to be present
            alert = self.wait.until(EC.alert_is_present())
            alert.accept()  # Click OK
            return True
        except TimeoutException:
            print("No alert found")
            return False

    def is_success_message_visible(self):
        # Verify success message is visible
        try:
            return self.is_visible(self.SUCCESS_MESSAGE)
        except TimeoutException:
            # Try alternative locator if the first one doesn't work
            alternative_success = (By.XPATH, "//div[contains(text(),'Success! Your details have been submitted successfully.')]")
            try:
                return self.is_visible(alternative_success)
            except TimeoutException:
                print("Success message not found with either locator")
                # Print page source for debugging
                if "Success!" in self.driver.page_source:
                    print("Success text found in page source but element not located")
                return False

    def click_home_button(self):
        # Click 'Home' button
        self.click(self.HOME_BUTTON)

    def verify_back_to_home(self):
        # Verify that landed to home page successfully
        return self.is_home_page_visible()