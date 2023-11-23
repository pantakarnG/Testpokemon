from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest
from selenium.webdriver.chrome.service import Service

class PokemonSearchTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Initialize the Chrome WebDriver
        chrome_driver_path = "D:/634259022/chd/chromedriver.exe"
        cls.service = Service(chrome_driver_path)
        cls.driver = webdriver.Chrome(service=cls.service)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        # Close the browser
        cls.driver.quit()

    def test_pokemon_search(self):
        # Open the Pokemon website
        self.driver.get("https://veekun.com/dex/pokemon/search")

        # Find the search box element and enter a query
        search_box_element = self.driver.find_element(By.XPATH, '//*[@id="content"]/form/div[1]/div[1]/dl/dd[1]/input')
        search_box_element.send_keys("Charizard")
        time.sleep(5)

        # Scroll to the bottom of the page
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

        # Find and click the submit button
        submit_element = self.driver.find_element(By.XPATH, '//*[@id="content"]/form/p[6]/button[1]')
        submit_element.click()

        # Wait for the search results to load (you can use WebDriverWait here)
        try:
            WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="content"]/h1[1]'), "3 results (1 species)")
        )
            # Success message
            print("Search for Charizard was successful. Page title: ", self.driver.title)
        except Exception as e:
            # Failure message
            print("Search for Charizard failed. Error: ", str(e))
            self.fail("Test failed: Search for Charizard")

if __name__ == "__main__":
    unittest.main()
