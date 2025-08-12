# utils/api_client.py
import requests
import json

class APIClient:
    def __init__(self):
        self.base_url = "https://automationexercise.com/api"
        self.session = requests.Session()
        # Don't set Content-Type globally as APIs expect form data, not JSON
    
    def get(self, endpoint, params=None):
        # Send GET request
        url = f"{self.base_url}/{endpoint}"
        response = self.session.get(url, params=params)
        return self._handle_response(response)
    
    def post(self, endpoint, data=None, json_data=None):
        # Send POST request
        url = f"{self.base_url}/{endpoint}"
        if json_data:
            response = self.session.post(url, json=json_data)
        else:
            response = self.session.post(url, data=data)
        return self._handle_response(response)
    
    def put(self, endpoint, data=None, json_data=None):
        # Send PUT request
        url = f"{self.base_url}/{endpoint}"
        if json_data:
            response = self.session.put(url, json=json_data)
        else:
            response = self.session.put(url, data=data)
        return self._handle_response(response)
    
    def delete(self, endpoint, data=None):
        # Send DELETE request
        url = f"{self.base_url}/{endpoint}"
        if data:
            response = self.session.delete(url, data=data)
        else:
            response = self.session.delete(url)
        return self._handle_response(response)
    
    def _handle_response(self, response):
        # Handle API response
        try:
            # Try to parse JSON response
            json_response = response.json()
            return {
                'status_code': response.status_code,
                'data': json_response,
                'headers': dict(response.headers),
                'success': response.ok
            }
        except json.JSONDecodeError:
            # If not JSON, return text response
            return {
                'status_code': response.status_code,
                'data': response.text,
                'headers': dict(response.headers),
                'success': response.ok
            }
    
    def get_products_list(self):
        # Get all products list
        return self.get("productsList")
    
    def get_brands_list(self):
        # Get all brands list
        return self.get("brandsList")
    
    def search_product(self, search_product):
        # Search for a product
        data = {'search_product': search_product}
        return self.post("searchProduct", data=data)
    
    def create_account(self, user_data):
        # Create user account
        return self.post("createAccount", data=user_data)
    
    def verify_login(self, email, password):
        # Verify user login
        data = {'email': email, 'password': password}
        return self.post("verifyLogin", data=data)
    
    def delete_account(self, email, password):
        # Delete user account
        data = {'email': email, 'password': password}
        return self.delete("deleteAccount", data=data)