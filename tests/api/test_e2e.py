from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as chrome_service
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver_path=ChromeDriverManager().install()
driver_service=chrome_service(driver_path)
chrome_options = Options()



# set chrome configuration
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")  
chrome_options.add_argument("--disable-dev-shm-usage") 
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(service=driver_service, options=chrome_options)

driver.get("http://127.0.0.1:5000")

def test_website_title():
   pass
