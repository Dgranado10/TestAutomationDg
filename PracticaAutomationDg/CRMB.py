from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time

# Assuming your chromedriver is in the same directory as your script
chromedriver_path = "chromedriver"  # Replace with the actual path if different

# Create a Chrome service object
service = Service(executable_path=chromedriver_path)

# Create a WebDriver instance
driver = webdriver.Chrome(service=service)

# Rest of your code...
#Abrir pagina
##driver = webdriver.Chrome('chromedriver')
driver.maximize_window()
driver.get("https://crmbqa.cgtscorp.com/#/home")

# Encuentra los elementos del formulario y llena los datos

User = driver.find_element(By.XPATH, "/html/body/app-root/app-login/div/div[1]/div[2]/div[1]/div[1]/div[2]/input") ##User
User.send_keys("dixongrana")
time.sleep(1)
Password = driver.find_element(By.XPATH,"/html/body/app-root/app-login/div/div[1]/div[2]/div[2]/div[1]/div[2]/input")   ##Pass
Password.send_keys("Abcd1234**")
time.sleep(1)
button = driver.find_element(By.XPATH, "/html/body/app-root/app-login/div/div[1]/div[2]/div[4]/button")
time.sleep(1)
button.click()
time.sleep(2)

#Seleccionar menu seguridad

segurida = driver.find_element(By.XPATH, "/html/body/app-root/div[1]/div[1]/app-header/div/div/div[2]/app-menu-crmb/div/div/p-menubar/div/p-menubarsub/ul/li[2]/a/span[1]")
time.sleep(1)
segurida.click

time.sleep(200)