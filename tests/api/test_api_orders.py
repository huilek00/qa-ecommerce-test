# tests/api/test_api_orders.py

import unittest
import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from utils.api_client import APIClient

class OrdersAPITest(unittest.TestCase):
    
    def setUp(self):
        self.api_client = APIClient()
    
    def test_get_products_list_for_order(self):
        """Test getting products list to prepare for order"""
        response = self.api_client.get_products_list()
        
        # Verify we can get products for ordering
        self.assertEqual(response['status_code'], 200)
        self.assertTrue(response['success'])
        self.assertIn('products', response['data'])
        
        products = response['data']['products']
        self.assertGreater(len(products), 0, "Should have products available for ordering")
        
        print(f"Products available for ordering: {len(products)}")
    
    def test_post_invalid_method_to_products_list(self):
        """POST To All Products List (Invalid method)"""
        # This should return method not supported error
        response = self.api_client.post("productsList")
        
        # Verify error response
        self.assertEqual(response['status_code'], 200)
        response_data = response['data']
        self.assertIn('responseCode', response_data)
        self.assertEqual(response_data['responseCode'], 405)
        self.assertIn('message', response_data)
        self.assertIn('method', response_data['message'].lower())
        
        print(f"Expected method error: {response_data['message']}")
    
    def test_post_invalid_method_to_brands_list(self):
        """Test POST To All Brands List (Invalid method)"""
        # This should return method not supported error
        response = self.api_client.post("brandsList")
        
        # Verify error response
        self.assertEqual(response['status_code'], 200)
        response_data = response['data']
        self.assertIn('responseCode', response_data)
        self.assertEqual(response_data['responseCode'], 405)
        
        print(f"Expected method error for brands: {response_data['message']}")
    
    def test_put_invalid_method_to_products_list(self):
        """Test PUT To All Products List (Invalid method)"""
        response = self.api_client.put("productsList")
        
        # Verify error response
        self.assertEqual(response['status_code'], 200)
        response_data = response['data']
        self.assertIn('responseCode', response_data)
        self.assertEqual(response_data['responseCode'], 405)
        
        print(f"Expected PUT method error: {response_data['message']}")
    
    def test_delete_invalid_method_to_products_list(self):
        """Test DELETE To All Products List (Invalid method)"""
        response = self.api_client.delete("productsList")
        
        # Verify error response
        self.assertEqual(response['status_code'], 200)
        response_data = response['data']
        self.assertIn('responseCode', response_data)
        self.assertEqual(response_data['responseCode'], 405)
        
        print(f"Expected DELETE method error: {response_data['message']}")
    
    def test_search_product_without_parameter(self):
        """Test API 8: POST To Search Product without search_product parameter"""
        # Send request without search_product parameter
        response = self.api_client.post("searchProduct", data={})
        
        # Should return error
        self.assertEqual(response['status_code'], 200)
        response_data = response['data']
        self.assertIn('responseCode', response_data)
        self.assertEqual(response_data['responseCode'], 400)
        self.assertIn('message', response_data)
        
        print(f"Expected parameter error: {response_data['message']}")
    
    def test_invalid_endpoint(self):
        """Test accessing non-existent API endpoint"""
        response = self.api_client.get("nonexistentendpoint")
        
        # Should return error
        self.assertIn(response['status_code'], [404, 200])  # Might return 404 or custom error
        
        if response['status_code'] == 200:
            response_data = response['data']
            if isinstance(response_data, dict) and 'responseCode' in response_data:
                self.assertNotEqual(response_data['responseCode'], 200)
        
        print(f"Response for invalid endpoint: {response}")
    
    def test_api_response_structure(self):
        """Test that API responses have consistent structure"""
        response = self.api_client.get_products_list()
        
        # Verify standard response structure
        self.assertIn('status_code', response)
        self.assertIn('data', response)
        self.assertIn('success', response)
        self.assertIn('headers', response)
        
        # Verify API data structure
        api_data = response['data']
        self.assertIsInstance(api_data, dict)
        self.assertIn('responseCode', api_data)
        self.assertIn('products', api_data)
        
        print("API response structure validation passed")
    
    def test_api_performance(self):
        """Basic API performance test"""
        import time
        
        start_time = time.time()
        response = self.api_client.get_products_list()
        end_time = time.time()
        
        response_time = end_time - start_time
        
        # Verify response time is reasonable (less than 5 seconds)
        self.assertLess(response_time, 5.0, "API response time should be under 5 seconds")
        self.assertEqual(response['status_code'], 200)
        
        print(f"API response time: {response_time:.2f} seconds")

if __name__ == "__main__":
    unittest.main()