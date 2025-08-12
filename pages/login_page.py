# pages/login_page.py

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    # locators
    LOGIN_LINK = (By.XPATH, "//a[@href='/login']")
    EMAIL_FIELD = (By.XPATH, "//input[@data-qa='login-email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@data-qa='login-password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@data-qa='login-button']")
    LOGGED_IN_TEXT = (By.XPATH, "//a[contains(text(),'Logged in as')]")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(text(), 'Your email or password is incorrect!')]")
    LOGOUT_LINK = (By.XPATH, "//a[contains(text(),'Logout')]")
    
    # locators for login
    LOGIN_TO_ACCOUNT_TEXT = (By.XPATH, "//h2[contains(text(),'Login to your account')]")
    ALT_LOGIN_TO_ACCOUNT_TEXT = (By.XPATH, "//div[@class='login-form']//h2")
    
    def go_to_login_page(self):
        # Navigate to login page
        self.click(self.LOGIN_LINK)
    
    def is_login_to_account_visible(self):
        # Verify 'Login to your account' is visible
        try:
            return self.is_visible(self.LOGIN_TO_ACCOUNT_TEXT)
        except:
            try:
                return self.is_visible(self.ALT_LOGIN_TO_ACCOUNT_TEXT)
            except:
                return False
    
    def login(self, email, password):
        # Enter email and password and click login
        self.enter_text(self.EMAIL_FIELD, email)
        self.enter_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)
    
    def is_logged_in_visible(self):
        # Verify that 'Logged in as username' is visible
        return self.is_visible(self.LOGGED_IN_TEXT)
    
    def get_logged_in_text(self):
        # Get the logged in text
        return self.get_text(self.LOGGED_IN_TEXT)
    
    def click_logout(self):
        # Click 'Logout' button
        self.click(self.LOGOUT_LINK)
    
    def is_login_page_loaded(self):
        # Verify that user is navigated to login page
        return self.is_login_to_account_visible()
    
    def get_warning(self):
        # Get error/warning message
        return self.get_text(self.ERROR_MESSAGE)