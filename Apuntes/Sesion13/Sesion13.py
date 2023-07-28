import requests  # Nos ayuda a obtener datos desde el EndPoint
import datetime as dt
import smtplib
import time

response = requests.get(url='http://api.open-notify.org/iss-now.json')  # Nos devuelve un código de respuesta
print(response.status_code)  # Response [200]
response.raise_for_status()  # Nos lanza un error cuando algo va mal en la petición.

# Para ver los datos reales de la petición
datos = response.json()
print(datos)

position = datos["iss_position"]
print(position)

position_longitud = float(datos["iss_position"]["longitude"])
position_latitud = float(datos["iss_position"]["latitude"])
iss_position = (position_longitud, position_latitud)  # Creamos una tupla con la posición del iss
print(iss_position)

# ---------------------------------------------------------------------------------------------------- #

MY_LAT = 36.720707369369975
MY_LNG = -4.35975358353041
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0  # En la documentación de la API viene este parámetro para cambiar al formato de 24 horas.
}

response_sun = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
response_sun.raise_for_status()
datos_sun = response_sun.json()
print(datos_sun)
print()
# Cogemos solo la parte de la hora de los datos. Para eso usamos 'split' y separamos el string por la 'T' y por los ':'
sunrise = int(datos_sun['results']['sunrise'].split("T")[1].split(":")[0])
sunset = int(datos_sun['results']['sunset'].split("T")[1].split(":")[0])

time_now = dt.datetime.now().time()
hora_amanecer = sunrise
hora_anochecer = sunset
hora_actual = time_now.hour
print()


# ---------- Comparamos los datos para que nos envie un correo si el iss pasa por encima y es de noche ------------ #

def position_iss():
    iss_lat_round = round(position_latitud)
    iss_lng_round = round(position_longitud)
    # Comprobamos que esté en un rango de -5 y +5 respecto mi posición
    lat_home_min = round(MY_LAT) - 5
    lat_home_max = round(MY_LAT) + 5
    lng_home_min = round(MY_LNG) - 5
    lng_home_max = round(MY_LNG) + 5

    # print(f"lat_home_min= {lat_home_min}, lat_home_max= {lat_home_max}, iss_lat_round= {iss_lat_round}")
    # print(f"lng_home_min= {lng_home_min}, lng_home_max= {lng_home_max}, iss_lng_round= {iss_lng_round}")

    if lat_home_min <= iss_lat_round >= lat_home_max and lng_home_min <= iss_lng_round >= lng_home_max:
        return True
    else:
        return False


def comprobar_hora():
    if hora_actual >= hora_anochecer or hora_actual <= hora_amanecer:
        return True
    else:
        return False


MY_EMAIL = "pruebapython83@gmail.com"
PASSWORD = "password"

while True:
    time.sleep(60)
    if position_iss() and comprobar_hora():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs="pruebapython84@yahoo.com",
                                msg=f"Subject:iss en el cielo\n\nYa puedes mirar al cielo")
