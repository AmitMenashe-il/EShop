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
   assert "Amit's Project EShop" in driver.title  # Check page title

def test_add_items_to_cart():
    items_to_add = ["28", "29", "30"]  # IDs/names of the items to add
    for item in items_to_add:
        driver.get(f"http://127.0.0.1:5000/#/product/{item}")
        add_to_cart_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/div[1]/div[3]/div/div/div[3]'))
        )
        add_to_cart_button.click()
        time.sleep(5)

    # Verify that the user is redirected to the shipping page
    current_url = driver.current_url
    assert current_url.endswith("/shipping"), "User is not redirected to the shipping page"

    # Check response code for the current URL
    response = requests.get(current_url)
    assert response.status_code == 200, f"Response code is not 200 for {current_url}"

    driver.quit()  # Close the WebDriver

# Call the test function
test_add_items_to_cart()
