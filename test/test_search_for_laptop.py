import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time

class TestSearchForLaptop:
    driver = ''

    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(5)
        self.driver.get('https://demo.nopcommerce.com/')
        self.driver.maximize_window()

    

    def test_search_for_laptop(self):
        mouse_action = ActionChains(self.driver)
        nav_menu= self.driver.find_element(By.LINK_TEXT, "Computers")
        mouse_action.move_to_element(nav_menu).perform()
        
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/ul[1]/li[1]/ul/li[2]/a").click()
        
        self.driver.implicitly_wait(10)
        page_move = ActionChains(self.driver)
        needed_laptop= self.driver.find_element(By.CSS_SELECTOR, '.button-2.product-box-add-to-cart-button')
        page_move.click(needed_laptop).perform()


        time.sleep(3)      



    def teardown_method(self):
        self.driver.quit()

if __name__ == '__main__':
   pytest.main()