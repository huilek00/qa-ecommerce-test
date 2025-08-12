# pages/checkout_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    # Cart page elements
    PROCEED_TO_CHECKOUT_BUTTON = (By.XPATH, "//a[contains(text(),'Proceed To Checkout')]")
    
    # Checkout page elements
    ADDRESS_DETAILS_TITLE = (By.XPATH, "//h2[contains(text(),'Address Details')]")
    REVIEW_ORDER_TITLE = (By.XPATH, "//h2[contains(text(),'Review Your Order')]")
    COMMENT_TEXT_AREA = (By.NAME, "message")
    PLACE_ORDER_BUTTON = (By.XPATH, "//a[contains(text(),'Place Order')]")
    
    # Payment page elements
    NAME_ON_CARD_FIELD = (By.NAME, "name_on_card")
    CARD_NUMBER_FIELD = (By.NAME, "card_number")
    CVC_FIELD = (By.NAME, "cvc")
    EXPIRY_MONTH_FIELD = (By.NAME, "expiry_month")
    EXPIRY_YEAR_FIELD = (By.NAME, "expiry_year")
    PAY_CONFIRM_BUTTON = (By.ID, "submit")
    
    # Success page elements
    SUCCESS_MESSAGE = (By.XPATH, "//p[contains(text(),'Your order has been placed successfully!')]")
    CONTINUE_BUTTON = (By.XPATH, "//a[contains(text(),'Continue')]")
    DOWNLOAD_INVOICE_BUTTON = (By.XPATH, "//a[contains(text(),'Download Invoice')]")
    
    def proceed_to_checkout(self):
        # Click Proceed To Checkout button from cart page
        self.click(self.PROCEED_TO_CHECKOUT_BUTTON)
    
    def is_address_details_visible(self):
        # Verify Address Details section is visible
        return self.is_visible(self.ADDRESS_DETAILS_TITLE)
    
    def is_review_order_visible(self):
        # Verify Review Your Order section is visible
        return self.is_visible(self.REVIEW_ORDER_TITLE)
    
    def enter_comment(self, comment):
        # Enter description in comment text area
        self.enter_text(self.COMMENT_TEXT_AREA, comment)
    
    def click_place_order(self):
        # Click Place Order button
        self.click(self.PLACE_ORDER_BUTTON)
    
    def enter_payment_details(self, name_on_card, card_number, cvc, expiry_month, expiry_year):
        # Enter payment details
        self.enter_text(self.NAME_ON_CARD_FIELD, name_on_card)
        self.enter_text(self.CARD_NUMBER_FIELD, card_number)
        self.enter_text(self.CVC_FIELD, cvc)
        self.enter_text(self.EXPIRY_MONTH_FIELD, expiry_month)
        self.enter_text(self.EXPIRY_YEAR_FIELD, expiry_year)
    
    def click_pay_and_confirm_order(self):
        # Click Pay and Confirm Order button
        self.click(self.PAY_CONFIRM_BUTTON)
    
    def is_success_message_visible(self):
        # Verify success message 'Your order has been placed successfully!' is visible
        return self.is_visible(self.SUCCESS_MESSAGE)
    
    def is_order_placed_successfully(self):
        # Alternative method to verify order success by checking URL and title
        return ("payment_done" in self.driver.current_url and 
                "Order Placed" in self.driver.title)
    
    def click_continue(self):
        # Click Continue button to go back to home page
        self.click(self.CONTINUE_BUTTON)
    
    def click_download_invoice(self):
        # Click Download Invoice button
        self.click(self.DOWNLOAD_INVOICE_BUTTON)