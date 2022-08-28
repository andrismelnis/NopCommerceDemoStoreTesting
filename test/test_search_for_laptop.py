import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from  webpage.website_actions import serch_for_laptop


class TestSearchForLaptop:
    driver = ''
    
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(5)
        self.driver.get('https://demo.nopcommerce.com/')
        self.driver.maximize_window()



    def test_search_for_laptop(self):
        serch_for_laptop(self)

        actual_text = self.driver.find_element(By.XPATH, '//*[@id="bar-notification"]/div/p/a').text
        expected_text = 'shopping cart'
        assert actual_text == expected_text, f"Expected text: '{expected_text}', but actual text: '{actual_text}'"      



    def teardown_method(self):
        self.driver.quit()

if __name__ == '__main__':
   pytest.main()