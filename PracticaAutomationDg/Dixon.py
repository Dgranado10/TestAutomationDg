from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


# Assuming your chromedriver is in the same directory as your script
chromedriver_path = "chromedriver"  # Replace with the actual path if different

# Create a Chrome service object
service = Service(executable_path=chromedriver_path)

# Create a WebDriver instance
driver = webdriver.Chrome(service=service)

driver.get("https://crmbqa.cgtscorp.com/#/home")

username = driver.find_element(By.XPATH, "//input[@formControlName='username']")
username.send_keys("dixongrana")
time.sleep(3)

password = driver.find_element(By.XPATH, "//input[@formControlName='password']")
password.send_keys("Abcd1234**")
time.sleep(3)

login = driver.find_element(By.XPATH , "/html/body/app-root/app-login/div/div[1]/div[2]/div[4]/button")
login.click()
time.sleep(3)

#Menu 
#Modulo Security
Security = driver.find_element(By.XPATH, "/html/body/app-root/div[1]/div[1]/app-header/div/div/div[2]/app-menu-crmb/div/div/p-menubar/div/p-menubarsub/ul/li[2]/a/span[1]")
Security.click()
time.sleep(3)

#opcion user
user = driver.find_element(By.XPATH, "/html/body/app-root/div[1]/div[1]/app-header/div/div/div[2]/app-menu-crmb/div/div/p-menubar/div/p-menubarsub/ul/li[2]/p-menubarsub/ul/li[1]/a/span")
user.click()
time.sleep(2)

#BtnAddUser
btnAdd = driver.find_element(By.XPATH, "/html/body/app-root/div[1]/div[2]/div/div/app-user-list/div[1]/app-button-add/div/div/button")
btnAdd.click()
time.sleep(3)

#Llenar Formulario 
office = driver.find_element(By.XPATH, "//input[@formControlName='office']")
office.click()
time.sleep(2)
SelectOfficePrincipal = driver.find_element(By.CLASS_NAME, "ng-star-inserted" )
SelectOfficePrincipal.click()
time.sleep(3)


driver.close()