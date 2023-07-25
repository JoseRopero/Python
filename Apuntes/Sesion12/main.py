import smtplib
import datetime as dt

my_email = "pruebapython83@gmail.com"
password = "password"  # Te lo da el proveedor de correo, una contraseña para apps.

with smtplib.SMTP("smtp.gmail.com") as connection:  # Creamos un objeto de la clase SMTP
    connection.starttls()  # TLS -> Transport Layer Security. Asegurar la conexión con nuestro servidor
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="pruebapython84@yahoo.com",
                        msg="Subject:hola\n\nEste es el cuerpo de mi correo")

# ------------------------------------------------------------------------------------------------------ #


now = dt.datetime.now()  # Nos da la fecha actual con mucha precisión
year = now.year
month = now.month
day_of_week = now.weekday()  # Nos da un número como dia de la semana
print(day_of_week)

date_of_birth = dt.datetime(year=1983, month=3, day=9)  # Fijamos una fecha en la variable
