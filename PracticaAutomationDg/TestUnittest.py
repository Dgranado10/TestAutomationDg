from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
from selenium.webdriver.common.by import By

class MyTestClass(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


    def test_Login(self):
        driver= self.driver
        driver.get("https://crmbqa.cgtscorp.com/#/home")
        time.sleep(2)
        username = driver.find_element(By.XPATH, "//input[@formControlName='username']")
        username.send_keys("dixongrana")
        time.sleep(3)
        
        password = driver.find_element(By.XPATH, "//input[@formControlName='password']")
        password.send_keys("Abcd1234**")
        time.sleep(3)
        login = driver.find_element(By.XPATH , "/html/body/app-root/app-login/div/div[1]/div[2]/div[4]/button")
        login.click()
        time.sleep(3)
        
        def test_profile(self): 
            Security = driver.find_element(By.XPATH, "/html/body/app-root/div[1]/div[1]/app-header/div/div/div[2]/app-menu-crmb/div/div/p-menubar/div/p-menubarsub/ul/li[2]/a/span[1]")
            Security.click()
            time.sleep(3)

        #opcion user
            user = driver.find_element(By.XPATH, "/html/body/app-root/div[1]/div[1]/app-header/div/div/div[2]/app-menu-crmb/div/div/p-menubar/div/p-menubarsub/ul/li[2]/p-menubarsub/ul/li[1]/a/span")
            user.click()
            time.sleep(2)

    

if __name__ == "__main__":
    unittest.main()
    
 