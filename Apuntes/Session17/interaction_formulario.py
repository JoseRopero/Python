from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, 'fName')
first_name.send_keys('Juan')

last_name = driver.find_element(By.NAME, 'lName')
last_name.send_keys('Rodriguez')

email = driver.find_element(By.NAME, 'email')
email.send_keys('prueba@pepe.es')

button = driver.find_element(By.CLASS_NAME, 'btn')
button.click()
