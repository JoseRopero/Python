import requests  # Nos ayuda a obtener datos desde el EndPoint

response = requests.get(url='http://api.open-notify.org/iss-now.json')  # Nos devuelve un código de respuesta
print(response.status_code)  # Response [200]
response.raise_for_status()  # Nos lanza un error cuando algo va mal en la petición.

# Para ver los datos reales de la petición
datos = response.json()
print(datos)

position = datos["iss_position"]
print(position)

position_longitud = datos["iss_position"]["longitude"]
position_latitud = datos["iss_position"]["latitude"]
iss_position = (position_longitud, position_latitud)  # Creamos una tupla con la posición del iss
print(iss_position)
