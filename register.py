import unittest 
import time 
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from webdriver_manager.chrome import ChromeDriverManager 
 
 
class TestLogin(unittest.TestCase): 
 
    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install()) 
    def test_signup (self): 
        # Steps 
            driver = self.browser 
            driver.get("http://barru.pythonanywhere.com/daftar") 
            driver.find_element(By.ID, "signUp").click() 
            time.sleep(1) 
            driver.find_element(By.ID, "name_register").send_keys("ritter1") 
            time.sleep(1) 
            driver.find_element(By.ID, "email_register").send_keys("dentana1@gmail.com") 
            time.sleep(1) 
            driver.find_element(By.ID, "password_register").send_keys("123abc") 
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