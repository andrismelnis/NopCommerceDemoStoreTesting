import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

def setup_method(self):
    self.driver = webdriver.Chrome(ChromeDriverManager().install())
    self.driver.implicitly_wait(5)
    self.driver.get('https://demo.nopcommerce.com/')
    self.driver.maximize_window()

email_adress = "test4@test.com"

def new_user_registration(self):
    self.driver.find_element(By.CSS_SELECTOR, '.ico-register').click()
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
        self.driver.find_element(By.CSS_SELECTOR, '.ico-login').click()
        self.driver.find_element(By.ID, 'Email').send_keys(email_adress)
        self.driver.find_element(By.ID, 'Password').send_keys('secretpassword')
        self.driver.find_element(By.CSS_SELECTOR, '.button-1.login-button').click()

if __name__ == '__main__':
   pytest.main()