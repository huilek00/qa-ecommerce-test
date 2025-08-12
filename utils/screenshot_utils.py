# utils/screenshot_utils.py
import os
from datetime import datetime

class ScreenshotManager:
    def __init__(self, driver, test_name="test"):
        self.driver = driver
        self.test_name = test_name
        self.screenshot_dir = "reports/screenshots"
        # Create screenshots directory if it doesn't exist
        os.makedirs(self.screenshot_dir, exist_ok=True)
    
    def capture_failure_screenshot(self, test_method_name):
        """Capture screenshot when test fails"""
        try:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"FAILURE_{self.test_name}_{test_method_name}_{timestamp}.png"
            filepath = os.path.join(self.screenshot_dir, filename)
            
            self.driver.save_screenshot(filepath)
            
            # Also save page source for debugging
            source_filename = filename.replace('.png', '_page_source.html')
            source_filepath = os.path.join(self.screenshot_dir, source_filename)
            
            with open(source_filepath, 'w', encoding='utf-8') as f:
                f.write(self.driver.page_source)
            
            print(f"Screenshot saved: {filepath}")
            print(f"Page source saved: {source_filepath}")
            
            return filepath
            
        except Exception as e:
            print(f"Failed to capture screenshot: {str(e)}")
            return None
    
    def capture_step_screenshot(self, step_name):
        """Capture screenshot for successful steps (optional)"""
        try:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"{self.test_name}_{step_name}_{timestamp}.png"
            filepath = os.path.join(self.screenshot_dir, filename)
            
            self.driver.save_screenshot(filepath)
            print(f"Step screenshot saved: {filepath}")
            
            return filepath
            
        except Exception as e:
            print(f"Failed to capture step screenshot: {str(e)}")
            return None