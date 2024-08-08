from selenium import webdriver
from selenium.webdriver.common.by import By

# webdriver es el controlador que maneja el navegador.

# Para que no se cierre el navegador una vez termine el programa
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

# Cargamos el controlador específico de Chrome
driver = webdriver.Chrome(options=chrome_options)
driver2 = webdriver.Chrome(options=chrome_options)
driver.get('https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1')
driver2.get('https://www.python.org/')

price_dollar = driver.find_element(By.CLASS_NAME, value='a-price-whole')
price_cent = driver.find_element(By.CLASS_NAME, value='a-price-fraction')
print(f'El precio es {price_dollar.text}.{price_cent.text}')

search = driver2.find_element(By.NAME, value='q')
print(search.tag_name)
print(search.get_attribute('placeholder'))
documentation_link = driver2.find_element(By.CSS_SELECTOR, '.documentation-widget a')
print(documentation_link.text)

bug_link = driver2.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

# Queremos crear un diccionario con las claves 'time' y 'name' y los datos recogidos de los últimos eventos de la página

# Primero creamos las dos listas. Una con las fechas y otra con los nombres
time_event = driver2.find_elements(By.CSS_SELECTOR, '.event-widget time')
name_event = driver2.find_elements(By.CSS_SELECTOR, '.event-widget li a')

# Inicializamos el diccionario
event_dict = {}

# Iterar sobre la lista
for i in range(len(time_event)):
    # Guardamos la fecha y el nombre del evento
    event_dict[i] = {
        'time': f'2024-{time_event[i].text}',
        'name': name_event[i].text
    }
print(event_dict)

# driver.close()  # Para cerrar la pestaña activa
driver.quit()  # Para cerrar el navegador
driver2.quit()
