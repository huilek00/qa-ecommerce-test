# pages/search_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage

class SearchPage(BasePage):
    # Home page elements
    HOME_SLIDER = (By.ID, "slider-carousel")  # Home page identifier
    
    # Navigation elements
    PRODUCTS_LINK = (By.XPATH, "//a[@href='/products']")
    
    # Products page elements
    ALL_PRODUCTS_TITLE = (By.XPATH, "//h2[contains(text(),'All Products')]")
    PRODUCTS_LIST = (By.XPATH, "//div[@class='features_items']")
    
    # Individual product elements
    PRODUCT_ITEMS = (By.XPATH, "//div[@class='productinfo text-center']")
    FIRST_PRODUCT_VIEW_BUTTON = (By.XPATH, "(//a[contains(text(),'View Product')])[1]")
    VIEW_PRODUCT_BUTTONS = (By.XPATH, "//a[contains(text(),'View Product')]")
    
    # Search elements
    SEARCH_BOX = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")
    SEARCHED_PRODUCTS_TITLE = (By.XPATH, "//h2[contains(text(),'Searched Products')]")
    
    # Product detail page elements
    PRODUCT_NAME = (By.XPATH, "//div[@class='product-information']//h2")
    PRODUCT_CATEGORY = (By.XPATH, "//div[@class='product-information']//p[contains(text(),'Category:')]")
    PRODUCT_PRICE = (By.XPATH, "//div[@class='product-information']//span/span")
    PRODUCT_AVAILABILITY = (By.XPATH, "//div[@class='product-information']//p[contains(text(),'Availability:')]")
    PRODUCT_CONDITION = (By.XPATH, "//div[@class='product-information']//p[contains(text(),'Condition:')]")
    PRODUCT_BRAND = (By.XPATH, "//div[@class='product-information']//p[contains(text(),'Brand:')]")
    
    # Alternative locators for product details (multiple strategies)
    ALT_PRODUCT_NAME = (By.XPATH, "//div[contains(@class,'product-details')]//h2")
    ALT_PRODUCT_CATEGORY = (By.XPATH, "//div[contains(@class,'product-details')]//p[1]")
    ALT_PRODUCT_PRICE = (By.XPATH, "//div[contains(@class,'product-details')]//span[contains(text(),'Rs.')]")
    
    # Additional alternative locators for missing fields
    ALT_PRODUCT_AVAILABILITY = (By.XPATH, "//p[contains(text(),'Availability') or contains(text(),'In Stock') or contains(text(),'Out of Stock')]")
    ALT_PRODUCT_CONDITION = (By.XPATH, "//p[contains(text(),'Condition') or contains(text(),'New') or contains(text(),'Used')]")
    ALT_PRODUCT_BRAND = (By.XPATH, "//p[contains(text(),'Brand') or contains(text(),'Polo') or contains(text(),'H&M') or contains(text(),'Madame')]")
    
    # Generic locators to find any product information
    ALL_PRODUCT_INFO_PARAGRAPHS = (By.XPATH, "//div[@class='product-information']//p")
    ALL_PRODUCT_INFO_SPANS = (By.XPATH, "//div[@class='product-information']//span")

    # Navigation and utility methods
    def is_home_page_visible(self):
        # Verify that home page is visible
        return self.is_visible(self.HOME_SLIDER)
    
    def click_products_link(self):
        # Click on Products button from home page
        self.click(self.PRODUCTS_LINK)
    
    def is_all_products_page_visible(self):
        # Verify that ALL PRODUCTS page is visible
        return self.is_visible(self.ALL_PRODUCTS_TITLE)
    
    def is_products_list_visible(self):
        # Verify that the products list is visible
        return self.is_visible(self.PRODUCTS_LIST)
    
    def get_products_count(self):
        # Get count of products visible on the page
        try:
            products = self.wait.until(EC.presence_of_all_elements_located(self.PRODUCT_ITEMS))
            return len(products)
        except TimeoutException:
            return 0
    
    def click_first_product_view(self):
        # Click on 'View Product' of first product
        self.click(self.FIRST_PRODUCT_VIEW_BUTTON)
    
    def is_product_detail_page_loaded(self):
        # Check if user is landed on product detail page
        # Check if any of the product detail elements are visible
        try:
            return (self.is_present(self.PRODUCT_NAME) or 
                   self.is_present(self.ALT_PRODUCT_NAME))
        except:
            return False
    
    # Product detail verification methods
    def get_product_name(self):
        # Get product name from detail page
        try:
            return self.get_text(self.PRODUCT_NAME)
        except:
            try:
                return self.get_text(self.ALT_PRODUCT_NAME)
            except:
                return None
    
    def get_product_category(self):
        # Get product category from detail page
        try:
            return self.get_text(self.PRODUCT_CATEGORY)
        except:
            try:
                return self.get_text(self.ALT_PRODUCT_CATEGORY)
            except:
                return None
    
    def get_product_price(self):
        # Get product price from detail page
        try:
            return self.get_text(self.PRODUCT_PRICE)
        except:
            try:
                return self.get_text(self.ALT_PRODUCT_PRICE)
            except:
                return None
    
    def get_product_availability(self):
        # Get product availability from detail page
        try:
            return self.get_text(self.PRODUCT_AVAILABILITY)
        except:
            try:
                return self.get_text(self.ALT_PRODUCT_AVAILABILITY)
            except:
                # Try to find availability info in any paragraph
                try:
                    paragraphs = self.driver.find_elements(*self.ALL_PRODUCT_INFO_PARAGRAPHS)
                    for p in paragraphs:
                        text = p.text.lower()
                        if 'availability' in text or 'in stock' in text or 'out of stock' in text:
                            return p.text
                except:
                    pass
                return None
    
    def get_product_condition(self):
        # Get product condition from detail page
        try:
            return self.get_text(self.PRODUCT_CONDITION)
        except:
            try:
                return self.get_text(self.ALT_PRODUCT_CONDITION)
            except:
                # Try to find condition info in any paragraph
                try:
                    paragraphs = self.driver.find_elements(*self.ALL_PRODUCT_INFO_PARAGRAPHS)
                    for p in paragraphs:
                        text = p.text.lower()
                        if 'condition' in text or 'new' in text or 'used' in text:
                            return p.text
                except:
                    pass
                return None
    
    def get_product_brand(self):
        # Get product brand from detail page
        try:
            return self.get_text(self.PRODUCT_BRAND)
        except:
            try:
                return self.get_text(self.ALT_PRODUCT_BRAND)
            except:
                # Try to find brand info in any paragraph
                try:
                    paragraphs = self.driver.find_elements(*self.ALL_PRODUCT_INFO_PARAGRAPHS)
                    for p in paragraphs:
                        text = p.text.lower()
                        if 'brand' in text or any(brand in text for brand in ['polo', 'h&m', 'madame', 'biba', 'allen solly']):
                            return p.text
                except:
                    pass
                return None
    
    def verify_all_product_details_visible(self):
        # Verify all product details are visible and return results
        details = {}
        
        # Check each detail and store result
        details['name'] = self.get_product_name()
        details['category'] = self.get_product_category()
        details['price'] = self.get_product_price()
        details['availability'] = self.get_product_availability()
        details['condition'] = self.get_product_condition()
        details['brand'] = self.get_product_brand()
        
        # Check which details are present
        present_details = {key: value for key, value in details.items() if value is not None}
        missing_details = [key for key, value in details.items() if value is None]
        
        return present_details, missing_details
    
    # Search functionality methods
    def search_product(self, product_name):
        # Enter product name in search input and click search button
        self.clear_and_enter_text(self.SEARCH_BOX, product_name)
        self.click(self.SEARCH_BUTTON)
    
    def is_searched_products_visible(self):
        # Verify 'SEARCHED PRODUCTS' title is visible
        return self.is_visible(self.SEARCHED_PRODUCTS_TITLE)
    
    def get_search_results_count(self):
        # Get count of products in search results
        try:
            products = self.wait.until(EC.presence_of_all_elements_located(self.PRODUCT_ITEMS))
            return len(products)
        except TimeoutException:
            return 0