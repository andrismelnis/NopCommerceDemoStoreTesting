import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from webpage.website_actions import successful_login
from webpage.website_actions import new_user_registration




class TestNewUser:
    driver = ''

    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(5)
        self.driver.get('https://demo.nopcommerce.com/')
        self.driver.maximize_window()
       

# New user registration

    def test_new_user(self):
        new_user_registration(self)    
        actual_text = self.driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/div/div/div[2]/div[1]').text
        expected_text = 'Your registration completed'
        assert actual_text == expected_text, f"Expected text: '{expected_text}', but actual text: '{actual_text}'"


# New user registratioun with already existing e-mail

    def test_new_user_with_existing_email(self):
        new_user_registration(self)
        actual_text = self.driver.find_element(By.CSS_SELECTOR, '.message-error.validation-summary-errors').text
        expected_text = 'The specified email already exists'
        assert actual_text == expected_text, f"Expected text: '{expected_text}', but actual text: '{actual_text}'"

# Successfuly login in account

    def test_successful_login(self):
        successful_login(self)
        actual_text = self.driver.find_element(By.CSS_SELECTOR, '.ico-account').text
        expected_text = 'My account'
        assert actual_text == expected_text, f"Expected text: '{expected_text}', but actual text: '{actual_text}'"


# Fail to login in account - wrong email

    def test_failed_login_wrong_user_name(self):
        self.driver.find_element(By.CSS_SELECTOR, '.ico-login').click()
        self.driver.find_element(By.ID, 'Email').send_keys('tes0@test.com')
        self.driver.find_element(By.ID, 'Password').send_keys('secretpassword')
        self.driver.find_element(By.CSS_SELECTOR, '.button-1.login-button').click()

        actual_link = self.driver.current_url
        expected_link = 'https://demo.nopcommerce.com/login?returnurl=%2F'
        assert actual_link == expected_link, f"Expected text: '{expected_link}', but actual text: '{actual_link}'"


# Fail to login to account - wrong password    

    def test_failed_login_wrong_password(self):
        self.driver.find_element(By.CSS_SELECTOR, '.ico-login').click()
        self.driver.find_element(By.ID, 'Email').send_keys('test@test.com')
        self.driver.find_element(By.ID, 'Password').send_keys('secretpasword')
        self.driver.find_element(By.CSS_SELECTOR, '.button-1.login-button').click()

        actual_link = self.driver.current_url
        expected_link = 'https://demo.nopcommerce.com/login?returnurl=%2F'
        assert actual_link == expected_link, f"Expected text: '{expected_link}', but actual text: '{actual_link}'"



# Fail to login in account - wrong email and password

    def test_failed_login_wrong_user_name_and_password(self):
        self.driver.find_element(By.CSS_SELECTOR, '.ico-login').click()
        self.driver.find_element(By.ID, 'Email').send_keys('test0@test.com')
        self.driver.find_element(By.ID, 'Password').send_keys('secretpasword')
        self.driver.find_element(By.CSS_SELECTOR, '.button-1.login-button').click()

        actual_link = self.driver.current_url
        expected_link = 'https://demo.nopcommerce.com/login?returnurl=%2F'
        assert actual_link == expected_link, f"Expected text: '{expected_link}', but actual text: '{actual_link}'"

    def teardown_method(self):
        self.driver.quit()

if __name__ == '__main__':
   pytest.main()