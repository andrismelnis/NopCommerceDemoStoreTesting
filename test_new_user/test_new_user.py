import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager




class TestNewUser:
    driver = ''

    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(5)
        self.driver.get('https://demo.nopcommerce.com/')
        self.driver.maximize_window()
       

    def test_new_user(self):
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

        self.driver.find_element(By.ID, 'Email').send_keys('test21@test.com')

        self.driver.find_element(By.ID, 'Password').send_keys('secretpassword')
        self.driver.find_element(By.ID, 'ConfirmPassword').send_keys('secretpassword')

        self.driver.find_element(By.ID, 'register-button').click()

    

        actual_text = self.driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/div/div/div[2]/div[1]').text
        expected_text = 'Your registration completed'
        assert actual_text == expected_text, f"Expected text: '{expected_text}', but actual text: '{actual_text}'"




    def test_new_user_with_existing_email(self):
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

        self.driver.find_element(By.ID, 'Email').send_keys('test21@test.com')

        self.driver.find_element(By.ID, 'Password').send_keys('secretpassword')
        self.driver.find_element(By.ID, 'ConfirmPassword').send_keys('secretpassword')

        self.driver.find_element(By.ID, 'register-button').click()

    

        actual_text = self.driver.find_element(By.CSS_SELECTOR, '.message-error.validation-summary-errors').text
        expected_text = 'The specified email already exists'
        assert actual_text == expected_text, f"Expected text: '{expected_text}', but actual text: '{actual_text}'"

    def test_successful_login(self):
        self.driver.find_element(By.CSS_SELECTOR, '.ico-login').click()
        self.driver.find_element(By.ID, 'Email').send_keys('test20@test.com')
        self.driver.find_element(By.ID, 'Password').send_keys('secretpassword')
        self.driver.find_element(By.CSS_SELECTOR, '.button-1.login-button').click()

        actual_text = self.driver.find_element(By.CSS_SELECTOR, '.ico-account').text
        expected_text = 'My account'
        assert actual_text == expected_text, f"Expected text: '{expected_text}', but actual text: '{actual_text}'"

    def test_failed_login_wrong_user_name(self):
        self.driver.find_element(By.CSS_SELECTOR, '.ico-login').click()
        self.driver.find_element(By.ID, 'Email').send_keys('tes0@test.com')
        self.driver.find_element(By.ID, 'Password').send_keys('secretpassword')
        self.driver.find_element(By.CSS_SELECTOR, '.button-1.login-button').click()

        actual_link = self.driver.current_url
        expected_link = 'https://demo.nopcommerce.com/login?returnurl=%2F'
        assert actual_link == expected_link, f"Expected text: '{expected_link}', but actual text: '{actual_link}'"


    

    def test_failed_login_wrong_password(self):
        self.driver.find_element(By.CSS_SELECTOR, '.ico-login').click()
        self.driver.find_element(By.ID, 'Email').send_keys('test@test.com')
        self.driver.find_element(By.ID, 'Password').send_keys('secretpasword')
        self.driver.find_element(By.CSS_SELECTOR, '.button-1.login-button').click()

        actual_link = self.driver.current_url
        expected_link = 'https://demo.nopcommerce.com/login?returnurl=%2F'
        assert actual_link == expected_link, f"Expected text: '{expected_link}', but actual text: '{actual_link}'"

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