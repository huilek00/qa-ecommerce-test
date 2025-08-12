# tests/test_cart.py

import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.home_page import HomePage
from pages.product_detail_page import ProductDetailPage
from pages.cart_page import CartPage

class CartTest(unittest.TestCase):
    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://automationexercise.com")
        self.driver.maximize_window()

    def test_add_to_cart(self):
        # add product to cart
        home = HomePage(self.driver)
        cart = CartPage(self.driver)

        home.add_first_product_to_cart()
        home.go_to_cart()

        product_name = cart.get_product_name()
        self.assertTrue(product_name)  # Check it's not empty
        print("Added to cart:", product_name)
    
    def test_verify_product_quantity_in_cart(self):
        # Verify Product quantity in Cart
        home = HomePage(self.driver)
        product_detail = ProductDetailPage(self.driver)
        cart = CartPage(self.driver)
        
        print("\n=== Starting Test Case 13: Verify Product quantity in Cart ===")
        
        # Verify that home page is visible successfully
        self.assertTrue(home.is_home_page_visible(), 
                       "Home page is not visible")
        print("✅ Home page is visible")
        
        # Click 'View Product' for any product on home page
        home.click_view_product_on_home_page()
        print("✅ Clicked 'View Product' on home page")
        
        # Small wait for page load
        time.sleep(2)
        
        # Verify product detail is opened
        self.assertTrue(product_detail.is_product_detail_opened(), 
                       "Product detail page is not opened")
        print("✅ Product detail page is opened")
        
        # Get product name for verification
        product_name = product_detail.get_product_name()
        print(f"✅ Product name: {product_name}")
        
        # Increase quantity to 4
        product_detail.increase_quantity_to(4)
        print("✅ Increased quantity to 4")
        
        # Small wait to ensure quantity is set
        time.sleep(1)
        
        # Click 'Add to cart' button
        product_detail.click_add_to_cart()
        print("✅ Clicked 'Add to cart' button")
        
        # Small wait for add to cart action
        time.sleep(2)
        
        # Click 'View Cart' button
        product_detail.click_view_cart()
        print("✅ Clicked 'View Cart' button")
        
        # Small wait for cart page to load
        time.sleep(2)
        
        # Verify that product is displayed in cart page with exact quantity
        self.assertTrue(cart.is_product_displayed_in_cart(), 
                       "Product is not displayed in cart")
        print("✅ Product is displayed in cart")
        
        cart_product_name = cart.get_product_name()
        cart_quantity = cart.get_product_quantity()
        
        print(f"✅ Cart product name: {cart_product_name}")
        print(f"✅ Cart quantity: {cart_quantity}")
        
        # Verify product is in cart
        self.assertIsNotNone(cart_product_name, "Product name not found in cart")
        
        # Verify quantity is exactly 4
        self.assertEqual(cart_quantity, 4, 
                        f"Expected quantity 4, but found {cart_quantity}")
        
        print("🎉 SUCCESS: Product quantity verification completed!")
        print(f"   - Product: {cart_product_name}")
        print(f"   - Quantity: {cart_quantity}")
    
    def tearDown(self):
        time.sleep(2)  # Brief pause to see results
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
