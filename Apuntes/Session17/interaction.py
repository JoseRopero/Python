from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Para hacer click en algún elemento de la página
articles = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
print(articles.text)
# articles.click()

# Buscamos por el texto del link y hacemos click
content_portals = driver.find_element(By.LINK_TEXT, 'Content portals')
# content_portals.click()

# Escribimos en el buscador de la página.
search = driver.find_element(By.NAME, 'search')
search.send_keys('Python', Keys.RETURN)
