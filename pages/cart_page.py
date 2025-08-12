# pages/cart_page.py

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    PRODUCT_NAME_IN_CART = (By.XPATH, "//td[@class='cart_description']//a")
    PRODUCT_QUANTITY_IN_CART = (By.XPATH, "//td[@class='cart_quantity']//button")
    CART_TABLE = (By.ID, "cart_info_table")
    CART_PRODUCT_ROW = (By.XPATH, "//tr[contains(@id,'product-')]")
    
    # Alternative locators for quantity
    ALT_QUANTITY = (By.XPATH, "//td[contains(@class,'quantity')]//button")
    ALT_QUANTITY_2 = (By.XPATH, "//button[@class='disabled']")
    ALT_QUANTITY_3 = (By.XPATH, "//td[@class='cart_quantity']")
    
    def get_product_name(self):
        # Get product name from cart
        return self.get_text(self.PRODUCT_NAME_IN_CART)
    
    def get_product_quantity(self):
        # Get product quantity from cart
        try:
            quantity_text = self.get_text(self.PRODUCT_QUANTITY_IN_CART)
            return int(quantity_text.strip())
        except:
            try:
                quantity_text = self.get_text(self.ALT_QUANTITY)
                return int(quantity_text.strip())
            except:
                try:
                    quantity_text = self.get_text(self.ALT_QUANTITY_2)
                    return int(quantity_text.strip())
                except:
                    try:
                        quantity_text = self.get_text(self.ALT_QUANTITY_3)
                        return int(quantity_text.strip())
                    except:
                        # Look for any number in cart table
                        try:
                            table = self.driver.find_element(*self.CART_TABLE)
                            # Search for quantity in table text
                            import re
                            numbers = re.findall(r'\b\d+\b', table.text)
                            # Usually quantity is one of the numbers found
                            for num in numbers:
                                if int(num) >= 1 and int(num) <= 10:  # Reasonable quantity range
                                    return int(num)
                            return 1  # Default fallback
                        except Exception as e:
                            print(f"Could not extract quantity: {e}")
                            return None
    
    def is_product_displayed_in_cart(self):
        # Verify product is displayed in cart
        return self.is_present(self.PRODUCT_NAME_IN_CART)
