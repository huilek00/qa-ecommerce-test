# conftest.py - Place this in your project root directory

import pytest
import os
from datetime import datetime

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture screenshots on test failures when using pytest"""
    outcome = yield
    rep = outcome.get_result()
    
    # Only capture screenshot on test failure and during the call phase
    if rep.when == "call" and rep.failed:
        # Get the driver from the test instance if available
        if hasattr(item.instance, 'driver'):
            driver = item.instance.driver
            
            # Create screenshots directory
            screenshot_dir = "reports/screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            
            # Generate screenshot filename
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            test_name = item.name
            filename = f"PYTEST_FAILURE_{test_name}_{timestamp}.png"
            filepath = os.path.join(screenshot_dir, filename)
            
            try:
                # Capture screenshot
                driver.save_screenshot(filepath)
                
                # Also save page source
                source_filename = filename.replace('.png', '_page_source.html')
                source_filepath = os.path.join(screenshot_dir, source_filename)
                
                with open(source_filepath, 'w', encoding='utf-8') as f:
                    f.write(driver.page_source)
                
                print(f"\n📸 Failure screenshot saved: {filepath}")
                print(f"📄 Page source saved: {source_filepath}")
                
                # Add screenshot to pytest-html report
                if hasattr(rep, 'extra'):
                    rep.extra.append(pytest_html.extras.png(filepath))
                
            except Exception as e:
                print(f"❌ Failed to capture screenshot: {str(e)}")

@pytest.fixture(scope="session", autouse=True)
def setup_reports_directory():
    """Create reports directory structure"""
    os.makedirs("reports/screenshots", exist_ok=True)
    os.makedirs("reports/logs", exist_ok=True)