# pages/register_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage


class RegisterPage(BasePage):
    # Locators
    HOME_SLIDER = (By.ID, "slider-carousel")  # Example locator for home page
    SIGNUP_LOGIN_LINK = (By.XPATH, "//a[@href='/login']")
    NEW_USER_SIGNUP_TEXT = (By.XPATH, "//h2[contains(text(), 'New User Signup!')]")
    NAME_FIELD = (By.NAME, "name")
    EMAIL_FIELD = (By.XPATH, "//input[@data-qa='signup-email']")
    SIGNUP_BUTTON = (By.XPATH, "//button[@data-qa='signup-button']")
    ENTER_ACCOUNT_INFO_TEXT = (By.XPATH, "//b[contains(text(),'Enter Account Information')]")
    
    # Error message locator (in case email already exists)
    EMAIL_ERROR = (By.XPATH, "//p[contains(text(), 'Email Address already exist!')]")

    # Account details
    TITLE_MR = (By.ID, "id_gender1")
    TITLE_MRS = (By.ID, "id_gender2")
    PASSWORD_FIELD = (By.ID, "password")
    DOB_DAY = (By.ID, "days")
    DOB_MONTH = (By.ID, "months")
    DOB_YEAR = (By.ID, "years")
    NEWSLETTER_CHECKBOX = (By.ID, "newsletter")
    OFFERS_CHECKBOX = (By.ID, "optin")
    FIRST_NAME = (By.ID, "first_name")
    LAST_NAME = (By.ID, "last_name")
    COMPANY = (By.ID, "company")
    ADDRESS1 = (By.ID, "address1")
    ADDRESS2 = (By.ID, "address2")
    COUNTRY = (By.ID, "country")
    STATE = (By.ID, "state")
    CITY = (By.ID, "city")
    ZIPCODE = (By.ID, "zipcode")
    MOBILE_NUMBER = (By.ID, "mobile_number")

    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[@data-qa='create-account']")
    ACCOUNT_CREATED_TEXT = (By.XPATH, "//b[contains(text(),'Account Created!')]")
    CONTINUE_BUTTON = (By.XPATH, "//a[@data-qa='continue-button']")
    LOGGED_IN_AS_TEXT = (By.XPATH, "//a[contains(text(),'Logged in as')]")
    DELETE_ACCOUNT_LINK = (By.XPATH, "//a[contains(text(),'Delete Account')]")
    ACCOUNT_DELETED_TEXT = (By.XPATH, "//b[contains(text(),'Account Deleted!')]")
    CONTINUE_AFTER_DELETE_BUTTON = (By.XPATH, "//a[@data-qa='continue-button']")

    # Methods
    def is_home_page_visible(self):
        return self.is_visible(self.HOME_SLIDER)

    def go_to_signup_page(self):
        self.click(self.SIGNUP_LOGIN_LINK)

    def is_new_user_signup_visible(self):
        return self.is_visible(self.NEW_USER_SIGNUP_TEXT)

    def enter_name_email(self, name, email):
        self.clear_and_enter_text(self.NAME_FIELD, name)
        self.clear_and_enter_text(self.EMAIL_FIELD, email)

    def click_signup_button(self):
        self.click(self.SIGNUP_BUTTON)

    def is_account_info_visible(self):
        try:
            return self.is_visible(self.ENTER_ACCOUNT_INFO_TEXT)
        except TimeoutException:
            # Check if there's an error message about email already existing
            try:
                if self.is_visible(self.EMAIL_ERROR):
                    print("Error: Email address already exists!")
                    return False
            except TimeoutException:
                pass
            
            # Print current URL for debugging
            print(f"Current URL: {self.driver.current_url}")
            print("Page title:", self.driver.title)
            
            # Try to find any text on the page for debugging
            try:
                page_source = self.driver.page_source
                if "Enter Account Information" in page_source:
                    print("Text 'Enter Account Information' found in page source but element not located")
                else:
                    print("Text 'Enter Account Information' NOT found in page source")
            except:
                pass
            
            raise

    def fill_account_details(self, title, password, day, month, year,
                             first_name, last_name, company, address1,
                             address2, country, state, city, zipcode, mobile_number):
        if title.lower() == "mr":
            self.click(self.TITLE_MR)
        else:
            self.click(self.TITLE_MRS)
        
        self.clear_and_enter_text(self.PASSWORD_FIELD, password)

        # Handle dropdowns for date of birth
        self.select_dropdown(self.DOB_DAY, day)
        self.select_dropdown(self.DOB_MONTH, month)
        self.select_dropdown(self.DOB_YEAR, year)

        # Check checkboxes
        self.click(self.NEWSLETTER_CHECKBOX)
        self.click(self.OFFERS_CHECKBOX)

        # Fill address information
        self.clear_and_enter_text(self.FIRST_NAME, first_name)
        self.clear_and_enter_text(self.LAST_NAME, last_name)
        self.clear_and_enter_text(self.COMPANY, company)
        self.clear_and_enter_text(self.ADDRESS1, address1)
        self.clear_and_enter_text(self.ADDRESS2, address2)
        
        # Handle country dropdown
        self.select_dropdown(self.COUNTRY, country)
        
        self.clear_and_enter_text(self.STATE, state)
        self.clear_and_enter_text(self.CITY, city)
        self.clear_and_enter_text(self.ZIPCODE, zipcode)
        self.clear_and_enter_text(self.MOBILE_NUMBER, mobile_number)

    def click_create_account(self):
        self.click(self.CREATE_ACCOUNT_BUTTON)

    def is_account_created_visible(self):
        return self.is_visible(self.ACCOUNT_CREATED_TEXT)

    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)

    def is_logged_in_as_visible(self):
        return self.is_visible(self.LOGGED_IN_AS_TEXT)

    def delete_account(self):
        self.click(self.DELETE_ACCOUNT_LINK)

    def is_account_deleted_visible(self):
        return self.is_visible(self.ACCOUNT_DELETED_TEXT)

    def click_continue_after_delete(self):
        self.click(self.CONTINUE_AFTER_DELETE_BUTTON)