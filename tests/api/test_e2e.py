from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def test_page_load():
  # set chrome headless, no sandbox and no shared memory
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")  
    chrome_options.add_argument("--disable-dev-shm-usage") 

    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get("https://localhost:5000")

        # check title
        assert "Amit's Project EShop" in driver.title  # Check page title

        # Add more assertions as needed for your specific page

    finally:
        # Close the WebDriver session
        driver.quit()
