from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class ProductDetailPage(BasePage):
    # Product detail page elements
    PRODUCT_NAME = (By.XPATH, "//div[@class='product-information']//h2")
    PRODUCT_PRICE = (By.XPATH, "//div[@class='product-information']//span/span")
    QUANTITY_INPUT = (By.ID, "quantity")
    ADD_TO_CART_BTN = (By.XPATH, "//button[contains(@class,'cart')]")
    VIEW_CART_LINK = (By.XPATH, "//a[contains(@href, 'view_cart') and contains(text(), 'View Cart')]")
    
    # Alternative locators
    ALT_PRODUCT_NAME = (By.XPATH, "//div[contains(@class,'product-details')]//h2")
    ALT_ADD_TO_CART = (By.XPATH, "//button[text()='Add to cart']")
    ALT_VIEW_CART = (By.XPATH, "//p//a[@href='/view_cart']")
    ALT_VIEW_CART_2 = (By.XPATH, "//u[text()='View Cart']")
    
    def is_product_detail_opened(self):
        # Verify product detail page is opened
        try:
            return self.is_present(self.PRODUCT_NAME) or self.is_present(self.ALT_PRODUCT_NAME)
        except:
            return False
    
    def get_product_name(self):
        # Get product name from detail page
        try:
            return self.get_text(self.PRODUCT_NAME)
        except:
            try:
                return self.get_text(self.ALT_PRODUCT_NAME)
            except:
                return None
    
    def increase_quantity_to(self, quantity):
        # Increase quantity to specified number
        try:
            quantity_field = self.wait.until(lambda d: d.find_element(*self.QUANTITY_INPUT))
            # Clear current value and enter new quantity
            quantity_field.clear()
            quantity_field.send_keys(str(quantity))
            print(f"Set quantity to: {quantity}")
        except Exception as e:
            print(f"Could not set quantity: {e}")
            # Alternative approach - select all and replace
            try:
                quantity_field = self.driver.find_element(*self.QUANTITY_INPUT)
                quantity_field.send_keys(Keys.CONTROL + "a")
                quantity_field.send_keys(str(quantity))
                print(f"Alternative method - Set quantity to: {quantity}")
            except Exception as e2:
                print(f"Alternative method also failed: {e2}")
    
    def click_add_to_cart(self):
        # Click 'Add to cart' button
        try:
            self.click(self.ADD_TO_CART_BTN)
            print("Clicked Add to cart button")
        except:
            try:
                self.click(self.ALT_ADD_TO_CART)
                print("Clicked Add to cart button (alternative locator)")
            except:
                # Try JavaScript click as fallback
                try:
                    button = self.driver.find_element(*self.ADD_TO_CART_BTN)
                    self.driver.execute_script("arguments[0].click();", button)
                    print("Clicked Add to cart button (JS click)")
                except:
                    try:
                        button = self.driver.find_element(*self.ALT_ADD_TO_CART)
                        self.driver.execute_script("arguments[0].click();", button)
                        print("Clicked Add to cart button (JS click alternative)")
                    except Exception as e:
                        print(f"Could not click add to cart: {e}")
    
    def click_view_cart(self):
        # Click 'View Cart' button
        try:
            self.click(self.VIEW_CART_LINK)
            print("Clicked View Cart link")
        except:
            try:
                self.click(self.ALT_VIEW_CART)
                print("Clicked View Cart link (alternative)")
            except:
                try:
                    self.click(self.ALT_VIEW_CART_2)
                    print("Clicked View Cart link (alternative 2)")
                except Exception as e:
                    print(f"Could not click view cart: {e}")
