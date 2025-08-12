# pages/home_page.py

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains

class HomePage(BasePage):
    # locators
    FIRST_PRODUCT = (By.XPATH, "//div[@class='product-image-wrapper'][1]")
    ADD_TO_CART_BTN = (By.XPATH, "//div[@class='product-image-wrapper'][1]//a[text()='Add to cart']")
    CONTINUE_SHOPPING_BTN = (By.XPATH, "//button[text()='Continue Shopping']")
    CART_LINK = (By.XPATH, "//a[@href='/view_cart']")
    
    # locators for verifying product quantity in cart
    HOME_SLIDER = (By.ID, "slider-carousel")
    VIEW_PRODUCT_BUTTONS = (By.XPATH, "//a[contains(text(),'View Product')]")
    FIRST_VIEW_PRODUCT_BTN = (By.XPATH, "(//a[contains(text(),'View Product')])[1]")
    
    # locators for Login/Logout
    SIGNUP_LOGIN_LINK = (By.XPATH, "//a[contains(text(),'Signup') and contains(text(),'Login')]")
    ALT_SIGNUP_LOGIN_LINK = (By.XPATH, "//a[@href='/login']")
    
    def is_home_page_visible(self):
        # Verify that home page is visible
        return self.is_visible(self.HOME_SLIDER)
    
    def click_signup_login(self):
        # Click on 'Signup / Login' button
        try:
            self.click(self.SIGNUP_LOGIN_LINK)
        except:
            self.click(self.ALT_SIGNUP_LOGIN_LINK)
    
    def click_view_product_on_home_page(self):
        # Click 'View Product' for any product on home page
        self.click(self.FIRST_VIEW_PRODUCT_BTN)
    
    def add_first_product_to_cart(self):
        product = self.wait.until(lambda d: d.find_element(*self.FIRST_PRODUCT))
        ActionChains(self.driver).move_to_element(product).perform()
        # JS click to avoid overlay interception
        add_button = self.wait.until(lambda d: d.find_element(*self.ADD_TO_CART_BTN))
        self.driver.execute_script("arguments[0].click();", add_button)
        self.click(self.CONTINUE_SHOPPING_BTN)

    def go_to_cart(self):
        self.click(self.CART_LINK)