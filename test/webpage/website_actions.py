import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


email_adress = "test4@test.com"



def new_user_registration(self):
    self.driver.find_element(By.ID, 'gender-male').click()
    self.driver.find_element(By.ID, 'FirstName').send_keys('John')
    self.driver.find_element(By.ID, 'LastName').send_keys('Doe')
    self.driver.find_element(By.NAME, 'DateOfBirthDay').click()
    self.driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/div/div/div[2]/form/div[1]/div[2]/div[4]/div/select[1]/option[11]').click()
    self.driver.find_element(By.NAME, 'DateOfBirthMonth').click()
    self.driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/div/div/div[2]/form/div[1]/div[2]/div[4]/div/select[2]/option[10]').click()
    self.driver.find_element(By.NAME, 'DateOfBirthYear')
    self.driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/div/div/div[2]/form/div[1]/div[2]/div[4]/div/select[3]/option[77]').click()
    self.driver.find_element(By.ID, 'Email').send_keys(email_adress)
    self.driver.find_element(By.ID, 'Password').send_keys('secretpassword')
    self.driver.find_element(By.ID, 'ConfirmPassword').send_keys('secretpassword')
    self.driver.find_element(By.ID, 'register-button').click()

def successful_login(self):
        self.driver.find_element(By.ID, 'Email').send_keys(email_adress)
        self.driver.find_element(By.ID, 'Password').send_keys('secretpassword')
        self.driver.find_element(By.CSS_SELECTOR, '.button-1.login-button').click()


# Find Asus N551JK-XO076H Laptop, add it to cart
def serch_for_laptop(self):
        mouse_action = ActionChains(self.driver)
        nav_menu= self.driver.find_element(By.LINK_TEXT, "Computers")
        mouse_action.move_to_element(nav_menu).perform()
        
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/ul[1]/li[1]/ul/li[2]/a").click()

        self.driver.find_element(By.ID, 'attribute-option-7').click()
        
        time.sleep(1)
        page_move = ActionChains(self.driver)
        add_to_cart_button= self.driver.find_element(By.CSS_SELECTOR, '.button-2.product-box-add-to-cart-button')
        page_move.move_to_element(add_to_cart_button).perform()
        self.driver.find_element(By.LINK_TEXT, "Asus N551JK-XO076H Laptop").click()

        page_move = ActionChains(self.driver)
        add_to_cart_button2= self.driver.find_element(By.CSS_SELECTOR, '#add-to-cart-button-5')
        page_move.move_to_element(add_to_cart_button2).perform()        
        self.driver.find_element(By.ID, 'add-to-cart-button-5').click()

if __name__ == '__main__':
   pytest.main()