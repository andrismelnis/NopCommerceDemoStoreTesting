import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from  webpage.website_actions import serch_for_laptop
from selenium.webdriver.common.action_chains import ActionChains
import time

class TestSearchForLaptop:
    driver = ''
    
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(5)
        self.driver.get('https://demo.nopcommerce.com/')
        self.driver.maximize_window()

    def test_cart(self):
        serch_for_laptop(self)

        self.driver.find_element(By.CSS_SELECTOR, '.close').click()
        mouse_action = ActionChains(self.driver)
        shopping_cart_button= self.driver.find_element(By.CSS_SELECTOR, '.cart-label')
        mouse_action.move_to_element(shopping_cart_button).perform()
        self.driver.find_element(By.CSS_SELECTOR, '.button-1.cart-button').click()


        self.driver.find_element(By.CSS_SELECTOR, '.qty-input').clear()
        self.driver.find_element(By.CSS_SELECTOR, '.qty-input').send_keys('2')
        self.driver.find_element(By.CSS_SELECTOR, '.qty-input').send_keys(Keys.ENTER)
        time.sleep(1)

        mouse_action = ActionChains(self.driver)
        disscount_code= self.driver.find_element(By.CSS_SELECTOR, '.button-1.checkout-button')
        mouse_action.move_to_element(disscount_code).perform()

        self.driver.find_element(By.ID, 'discountcouponcode').send_keys(123)
        self.driver.find_element(By.ID, 'applydiscountcouponcode').click()

        self.driver.find_element(By.ID, 'termsofservice').click()
        self.driver.find_element(By.ID, 'checkout').click()

        time.sleep(3)

    def teardown_method(self):
        self.driver.quit()

if __name__ == '__main__':
   pytest.main()    