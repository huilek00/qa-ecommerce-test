# tests/api/test_api_products.py

import unittest
import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from utils.api_client import APIClient

class ProductsAPITest(unittest.TestCase):
    
    def setUp(self):
        self.api_client = APIClient()
    
    def test_get_all_products_list(self):
        """Test API: Get All Products List"""
        response = self.api_client.get_products_list()
        
        # Verify response
        self.assertEqual(response['status_code'], 200)
        self.assertTrue(response['success'])
        
        # Verify response contains products
        self.assertIn('products', response['data'])
        products = response['data']['products']
        self.assertIsInstance(products, list)
        self.assertGreater(len(products), 0, "Products list should not be empty")
        
        # Verify product structure
        first_product = products[0]
        expected_keys = ['id', 'name', 'price', 'brand', 'category']
        for key in expected_keys:
            self.assertIn(key, first_product, f"Product should have '{key}' field")
        
        print(f"Total products found: {len(products)}")
        print(f"First product: {first_product['name']}")
    
    def test_search_product(self):
        """Test API: Search Product with valid term"""
        search_term = "top"
        response = self.api_client.search_product(search_term)
        
        # Verify response
        self.assertEqual(response['status_code'], 200)
        self.assertTrue(response['success'])
        
        # Verify search results
        response_data = response['data']
        self.assertEqual(response_data['responseCode'], 200)
        self.assertIn('products', response_data)
        products = response_data['products']
        self.assertIsInstance(products, list)
        
        # Verify search results contain the search term
        if len(products) > 0:
            found_relevant = False
            for product in products:
                if search_term.lower() in product['name'].lower():
                    found_relevant = True
                    break
            self.assertTrue(found_relevant, 
                          f"Search results should contain products with '{search_term}'")
        
        print(f"Search results for '{search_term}': {len(products)} products")
    
    def test_search_product_empty_query(self):
        """Test search with empty query - should return all products"""
        response = self.api_client.search_product("")
        
        # Verify response - API returns 200 and all products for empty search
        self.assertEqual(response['status_code'], 200)
        self.assertTrue(response['success'])
        
        response_data = response['data']
        self.assertEqual(response_data['responseCode'], 200)
        
        # Empty search returns all products (34 total based on your output)
        products = response_data.get('products', [])
        self.assertIsInstance(products, list)
        self.assertGreater(len(products), 0, "Empty search should return all products")
        
        print(f"Empty search returned all products: {len(products)} products")
    
    def test_search_nonexistent_product(self):
        """Test search for product that doesn't exist"""
        response = self.api_client.search_product("nonexistentproduct123")
        
        # Verify response - should be 200 with search results
        self.assertEqual(response['status_code'], 200)
        self.assertTrue(response['success'])
        
        # Should return empty results for non-existent product
        response_data = response['data']
        self.assertEqual(response_data['responseCode'], 200)
        products = response_data.get('products', [])
        self.assertIsInstance(products, list)
        
        # Non-existent product should return no results
        self.assertEqual(len(products), 0, "Non-existent product search should return no results")
        
        print(f"Search for non-existent product returned: {len(products)} results")
    
    def test_get_brands_list(self):
        """Test API: Get All Brands List"""
        response = self.api_client.get_brands_list()
        
        # Verify response
        self.assertEqual(response['status_code'], 200)
        self.assertTrue(response['success'])
        
        # Verify response contains brands
        self.assertIn('brands', response['data'])
        brands = response['data']['brands']
        self.assertIsInstance(brands, list)
        self.assertGreater(len(brands), 0, "Brands list should not be empty")
        
        # Verify brand structure
        first_brand = brands[0]
        expected_keys = ['id', 'brand']
        for key in expected_keys:
            self.assertIn(key, first_brand, f"Brand should have '{key}' field")
        
        print(f"Total brands found: {len(brands)}")
        print(f"First brand: {first_brand['brand']}")
    
    def test_search_product_case_insensitive(self):
        """Test that search is case insensitive"""
        # Test both lowercase and uppercase
        response_lower = self.api_client.search_product("top")
        response_upper = self.api_client.search_product("TOP")
        
        # Both should succeed
        self.assertEqual(response_lower['status_code'], 200)
        self.assertEqual(response_upper['status_code'], 200)
        
        # Should return same number of results
        products_lower = response_lower['data']['products']
        products_upper = response_upper['data']['products']
        
        self.assertEqual(len(products_lower), len(products_upper), 
                        "Case insensitive search should return same number of results")
        
        print(f"Case insensitive test: '{products_lower[0]['name']}' found with both 'top' and 'TOP'")

if __name__ == "__main__":
    unittest.main()