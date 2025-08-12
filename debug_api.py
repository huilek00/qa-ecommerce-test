# debug_api.py - Quick test to see what's happening
import requests

# Test search API directly
url = "https://automationexercise.com/api/searchProduct"
data = {'search_product': 'top'}

response = requests.post(url, data=data)
print(f"Status Code: {response.status_code}")
print(f"Response Headers: {dict(response.headers)}")
print(f"Response Text: {response.text}")

try:
    json_response = response.json()
    print(f"JSON Response: {json_response}")
except:
    print("Not a JSON response")