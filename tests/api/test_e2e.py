from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as chrome_service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver_path=ChromeDriverManager().install()
driver_service=chrome_service(driver_path)
chrome_options = Options()
capabilities = DesiredCapabilities.CHROME.copy()

# set chrome configuration

chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")  
chrome_options.add_argument("--disable-dev-shm-usage") 
capabilities['acceptInsecureCerts'] = True

def test_page_load():
   try:
        driver = webdriver.Chrome(service=driver_service, options=chrome_options, desired_capabilities=capabilities)
        driver.get("https://localhost:5000")

        # check title
        assert "Amit's Project EShop" in driver.title  # Check page title

        # Add more assertions as needed for your specific page ??

    finally:
        # Close the WebDriver session
        driver.quit()
