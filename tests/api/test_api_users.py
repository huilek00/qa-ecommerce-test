# tests/api/test_api_users.py
import unittest
import sys
import os
import random
import string

# Add the project root to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from utils.api_client import APIClient

class UsersAPITest(unittest.TestCase):
    
    def setUp(self):
        self.api_client = APIClient()
        # Generate random email for testing
        random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        self.test_email = f"testuser{random_suffix}@example.com"
        self.test_password = "testpassword123"
    
    def test_create_account_success(self):
        """Test API: POST To Create/Register User Account"""
        user_data = {
            'name': 'Test User',
            'email': self.test_email,
            'password': self.test_password,
            'title': 'Mr',
            'birth_date': '1',
            'birth_month': '1',
            'birth_year': '1990',
            'firstname': 'Test',
            'lastname': 'User',
            'company': 'Test Company',
            'address1': '123 Test Street',
            'address2': 'Apt 1',
            'country': 'United States',
            'zipcode': '12345',
            'state': 'California',
            'city': 'Los Angeles',
            'mobile_number': '1234567890'
        }
        
        response = self.api_client.create_account(user_data)
        
        # Verify response
        self.assertEqual(response['status_code'], 200)
        self.assertTrue(response['success'])
        
        # Verify success message
        response_data = response['data']
        self.assertIn('responseCode', response_data)
        self.assertEqual(response_data['responseCode'], 201)
        self.assertIn('message', response_data)
        self.assertIn('created', response_data['message'].lower())
        
        print(f"Account created successfully: {response_data['message']}")
    
    def test_create_account_existing_email(self):
        """Test creating account with existing email"""
        user_data = {
            'name': 'Existing User',
            'email': 'huilek@example.com',  # Use your existing test email
            'password': 'password123',
            'title': 'Mr',
            'birth_date': '1',
            'birth_month': '1',
            'birth_year': '1990',
            'firstname': 'Existing',
            'lastname': 'User',
            'company': 'Test Company',
            'address1': '123 Test Street',
            'country': 'United States',
            'zipcode': '12345',
            'state': 'California',
            'city': 'Los Angeles',
            'mobile_number': '1234567890'
        }
        
        response = self.api_client.create_account(user_data)
        
        # Should return error for existing email
        self.assertEqual(response['status_code'], 200)
        response_data = response['data']
        self.assertIn('responseCode', response_data)
        self.assertEqual(response_data['responseCode'], 400)
        self.assertIn('message', response_data)
        self.assertIn('exist', response_data['message'].lower())
        
        print(f"Expected error for existing email: {response_data['message']}")
    
    def test_verify_login_valid_credentials(self):
        """Test API: POST To Verify Login with valid details"""
        response = self.api_client.verify_login('huilek@example.com', 'correctpassword')
        
        # Verify response
        self.assertEqual(response['status_code'], 200)
        self.assertTrue(response['success'])
        
        # Verify login success
        response_data = response['data']
        self.assertIn('responseCode', response_data)
        self.assertEqual(response_data['responseCode'], 200)
        self.assertIn('message', response_data)
        # The actual message is "User exists!" not containing "login"
        self.assertIn('exists', response_data['message'].lower())
        
        print(f"Login successful: {response_data['message']}")
    
    def test_verify_login_invalid_credentials(self):
        """Test API: POST To Verify Login without email parameter"""
        response = self.api_client.verify_login('invalid@example.com', 'wrongpassword')
        
        # Should return error
        self.assertEqual(response['status_code'], 200)
        response_data = response['data']
        self.assertIn('responseCode', response_data)
        self.assertEqual(response_data['responseCode'], 404)
        self.assertIn('message', response_data)
        
        print(f"Expected error for invalid credentials: {response_data['message']}")
    
    def test_verify_login_missing_email(self):
        """Test login without email parameter"""
        # Send request with missing email
        data = {'password': 'somepassword'}
        response = self.api_client.post("verifyLogin", data=data)
        
        # Should return error
        self.assertEqual(response['status_code'], 200)
        response_data = response['data']
        self.assertIn('responseCode', response_data)
        self.assertEqual(response_data['responseCode'], 400)
        
        print(f"Expected error for missing email: {response_data['message']}")
    
    def test_delete_account_valid_credentials(self):
        """Test API: DELETE To Delete User Account"""
        # First create a test account
        user_data = {
            'name': 'Delete Test User',
            'email': self.test_email,
            'password': self.test_password,
            'title': 'Mr',
            'birth_date': '1',
            'birth_month': '1',
            'birth_year': '1990',
            'firstname': 'Delete',
            'lastname': 'Test',
            'company': 'Test Company',
            'address1': '123 Test Street',
            'country': 'United States',
            'zipcode': '12345',
            'state': 'California',
            'city': 'Los Angeles',
            'mobile_number': '1234567890'
        }
        
        # Create account first
        create_response = self.api_client.create_account(user_data)
        if create_response['data']['responseCode'] == 201:
            # Now delete the account
            delete_response = self.api_client.delete_account(self.test_email, self.test_password)
            
            self.assertEqual(delete_response['status_code'], 200)
            response_data = delete_response['data']
            self.assertIn('responseCode', response_data)
            self.assertEqual(response_data['responseCode'], 200)
            
            print(f"Account deleted successfully: {response_data['message']}")

if __name__ == "__main__":
    unittest.main()