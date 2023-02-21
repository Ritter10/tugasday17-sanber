import unittest 
import time 
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from webdriver_manager.chrome import ChromeDriverManager 
 
 
class TestLogin(unittest.TestCase): 
 
    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install()) 
 
    def test_success_login(self): 
        # Steps 
        driver = self.browser 
        driver.get("https://www.saucedemo.com/") 
        time.sleep(3) 
        driver.find_element(By.ID, "user-name").send_keys("standard_user") 
        time.sleep(1) 
        driver.find_element(By.ID, "password").send_keys("secret_sauce") 
        time.sleep(1) 
        driver.find_element(By.ID, "login-button").click() 
        time.sleep(1) 
 
        # Validasi 
        response_data = driver.find_element(By.CLASS_NAME, "title").text 
        self.assertIn('PRODUCTS', response_data) 
 
    def test_blank_password(self): 
        # Steps 
        driver = self.browser 
        driver.get("https://www.saucedemo.com/") 
        time.sleep(3) 
        driver.find_element(By.ID, "user-name").send_keys("") 
        time.sleep(1) 
        driver.find_element(By.ID, "password").send_keys("") 
        time.sleep(1) 
        driver.find_element(By.ID, "login-button").click() 
        time.sleep(1) 
 
        # Validasi 
        response_data = driver.find_element( 
            By.CLASS_NAME, "error-message-container").text 
        self.assertIn('Epic sadface: Username is required', response_data) 
    
    def test_username_invalid (self): 
        # Steps 
        driver = self.browser 
        driver.get("https://www.saucedemo.com/") 
        time.sleep(3) 
        driver.find_element(By.ID, "user-name").send_keys("sanber") 
        time.sleep(1) 
        driver.find_element(By.ID, "password").send_keys("secret_sauce") 
        time.sleep(1) 
        driver.find_element(By.ID, "login-button").click() 
        time.sleep(1) 
 
        # Validasi 
        response_data = driver.find_element( 
            By.CLASS_NAME, "error-message-container").text 
        self.assertIn('Epic sadface: Username and password do not match any user in this service', response_data) 

def test_password_invalid (self): 
        # Steps 
        driver = self.browser 
        driver.get("https://www.saucedemo.com/") 
        time.sleep(3) 
        driver.find_element(By.ID, "user-name").send_keys("standard_user") 
        time.sleep(1) 
        driver.find_element(By.ID, "password").send_keys("") 
        time.sleep(1) 
        driver.find_element(By.ID, "login-button").click() 
        time.sleep(1) 
 
        # Validasi 
        response_data = driver.find_element( 
            By.CLASS_NAME, "error-message-container").text 
        self.assertIn('Epic sadface: Password is required',response_data) 

        def test_signup (self): 
        # Steps 
            driver = self.browser 
            driver.get("http://barru.pythonanywhere.com/daftar") 
            driver.find_element(By.ID, "signUp").click() 
            time.sleep(1) 
            driver.find_element(By.ID, "name_register").send_keys("ritter") 
            time.sleep(1) 
            driver.find_element(By.ID, "email_register").send_keys("dentana@gmail.com") 
            time.sleep(1) 
            driver.find_element(By.ID, "password_register").send_keys("12345") 
            time.sleep(1) 
            driver.find_element(By.ID, "signup_register").click() 
            time.sleep(1) 
        # Validasi 
        response_data = driver.find_element(By.CSS_SELECTOR, "#swal2-title").text 
        self.assertIn('berhasil', response_data) 

def tearDown(self): 
        self.browser.quit() 
 
 
if __name__ == "__main__": 
    unittest.main()