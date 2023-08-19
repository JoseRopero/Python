import requests
import config as co
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

# ---------------------------------Creamos un nuevo usuario en pixela ------------------------------------------

user_params = {
    "token": co.TOKEN_PIXE,
    "username": co.USER_NAME_PIXE,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)  # Te devuelve la respuesta en tipo text
# Una vez creado lo dejo comentado porque me daría error al intentar hacerlo otra vez.

# -------------------------------------------Pasamos a crear un gráfico -------------------------------------

graph_endpoint = f"{pixela_endpoint}/{co.USER_NAME_PIXE}/graphs"
graph_params = {
    "id": "graph1",
    "name": "lectura Graph",
    "unit": "pag",
    "type": "int",
    "color": "sora"
}
# # Esta vez pasamos el token por la cabecera para más seguridad
headers_pixela = {
    "X-USER-TOKEN": co.TOKEN_PIXE
}
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers_pixela)
# print(response.text)

# Una vez creado lo comentamos para pasar al siguiente punto

# ---------------------------------- Postear un pixel ---------------------------------------------------

day = datetime(year=2023, month=8, day=18)  # De esta manera podemos indicar el dia que queramos.
today = datetime.now()  # El dia actual.
day_format = day.strftime("%Y%m%d")  # Para formatear la fecha según nos pidan. En este caso yyyymmdd

post_params = {
    "date": day_format,
    "quantity": "25"
}
# En el parámetro 'quantity' podemos usar 'input' para indicar por teclado la cantidad.
# Ejem -> "quantity": input("Cuantas páginas has leído hoy?:")
post_endpoint = f"{graph_endpoint}/graph1"

# response = requests.post(url=post_endpoint, json=post_params, headers=headers_pixela)
# print(response.text)

# --------------------------------- Actualizar un pixel --------------------------------------------------

put_endpoint = f"{post_endpoint}/{day_format}"

put_params = {
    "quantity": "50"
}

# response = requests.put(url=put_endpoint, json=put_params, headers=headers_pixela)
# print(response.text)

# --------------------------------- Eliminar un pixel ------------------------------------------------

# Voy a eliminar el pixel que he actualizado.
delete_endpoint = f"{put_endpoint}"
response = requests.delete(url=delete_endpoint, headers=headers_pixela)
print(response.text)
